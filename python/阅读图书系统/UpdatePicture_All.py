import concurrent.futures
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import mysql.connector

"""
这个是更新数据库中所有的链接

table_name：只需要设置你要更新的表
"""


# 定义数据库操作类
class BookDatabase:
    def __init__(self, username, password, database):
        # 初始化时建立数据库连接
        self.connection = self._connect_to_database(username, password, database)

    def _connect_to_database(self, username, password, database):
        try:
            # 尝试连接数据库
            connection = mysql.connector.connect(
                host="localhost",
                user=username,
                password=password,
                database=database
            )
            return connection
        except mysql.connector.Error as e:
            # 若连接失败，打印错误信息并返回空连接
            print("数据库连接错误:", e)
            return None

    def fetch_book_names(self, table_name):
        """
        从数据库中获取书名列表

        Args:
            table_name (str): 数据库表名

        Returns:
            list: 书名列表
        """
        if not self.connection:
            return []

        try:
            # 查询数据库中的书名信息
            with self.connection.cursor() as cursor:
                query = f"SELECT book_name FROM {table_name}"
                cursor.execute(query)
                # 提取查询结果中的书名列表
                book_names = [row[0] for row in cursor.fetchall()]
                return book_names
        except mysql.connector.Error as e:
            # 若查询出错，打印错误信息并返回空列表
            print("查询错误:", e)
            return []

    def close_connection(self):
        """
        关闭数据库连接
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("数据库连接已关闭")


# 定义图片爬取类
class ImageScraper:
    def __init__(self):
        self.base_url = "https://cn.bing.com/images/async"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
        }
        self.batch_size = 35

    def find_image_urls(self, html):
        """
        从HTML页面中提取图片URL

        Args:
            html (str): HTML页面内容

        Returns:
            list: 图片URL列表
        """
        soup = BeautifulSoup(html, 'lxml')
        image_elements = soup.find_all('a', attrs='iusc')
        image_urls = [json.loads(image_element["m"])["murl"] for image_element in image_elements]
        return image_urls

    def get_image_urls(self, keywords, max_number=10000):
        """
        获取图片URL列表

        Args:
            keywords (str): 搜索关键词
            max_number (int, optional): 最大图片数量. Defaults to 10000.

        Returns:
            list: 图片URL列表
        """
        crawled_urls = []

        keywords_str = "&q={}".format(quote(keywords))
        query_url = f"{self.base_url}?count={self.batch_size}" + keywords_str

        def get_image_urls(page):
            image_urls = []
            url = query_url + f"&first={page * self.batch_size}&SFX={page}"
            try:
                response = requests.get(url, headers=self.headers)
                response.raise_for_status()
                image_urls += self.find_image_urls(response.text)
            except requests.RequestException as e:
                print(e)
            return image_urls

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_page = {executor.submit(get_image_urls, page): page for page in
                              range(0, (max_number + self.batch_size) // self.batch_size + 1)}
            for future in concurrent.futures.as_completed(future_to_page):
                page = future_to_page[future]
                try:
                    crawled_urls.extend(future.result())
                except Exception as exc:
                    print(f"第 {page} 页出错: {exc}")

        crawled_urls = list(set(filter(lambda url: url.lower().endswith('.jpg'), crawled_urls)))
        return crawled_urls[:min(len(crawled_urls), max_number)]


# 定义处理书籍的函数
def process_book(book_name, image_scraper, book_db, table_name):
    """
    处理书籍，获取封面URL并更新数据库

    Args:
        book_name (str): 书名
        image_scraper (ImageScraper): 图片爬取实例
        book_db (BookDatabase): 数据库操作实例
        table_name (str): 数据库表名
    """
    res = image_scraper.get_image_urls(book_name, max_number=1)
    print(book_name, res)
    if res:
        new_cover_url = res[0]
        try:
            with book_db.connection.cursor() as cursor:
                update_query = f"UPDATE {table_name} SET coverUrl = %s WHERE book_name = %s"
                cursor.execute(update_query, (new_cover_url, book_name))
                book_db.connection.commit()
                print(f"已更新书籍 {book_name} 的封面URL")
        except mysql.connector.Error as e:
            print(f"无法更新书籍 {book_name} 的封面URL：{e}")


# 定义主逻辑类
class MainLogic:
    def __init__(self):
        self.db_username = "root"
        self.db_password = "hy064872"
        self.db_name = "mybook"
        self.table_name = "appbook01_prettynum"

    def run(self):
        """
        运行主逻辑
        """
        # 创建数据库操作实例
        book_db = BookDatabase(self.db_username, self.db_password, self.db_name)

        try:
            # 获取数据库中的书名列表
            book_names = book_db.fetch_book_names(self.table_name)
            # 创建图片爬取实例
            image_scraper = ImageScraper()

            max_threads = 20
            # 使用线程池并发地处理书籍
            with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
                for book_name in book_names:
                    # 提交处理任务到线程池
                    executor.submit(process_book, book_name, image_scraper, book_db, self.table_name)

        finally:
            # 关闭数据库连接
            book_db.close_connection()


if __name__ == "__main__":
    # 创建主逻辑实例并运行
    main_logic = MainLogic()
    main_logic.run()
