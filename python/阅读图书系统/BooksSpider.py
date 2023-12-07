import requests
from lxml import html
import pymysql
import threading

"""
仅爬取书籍信息，图片链接默认不能使用，需要执行图片链接更新

"""
class BookScraper:
    def __init__(self, db_config, num_threads=10):
        self.db_config = db_config
        self.num_threads = num_threads

    def __del__(self):
        pass

    def scrape_and_store_range(self, start_serial, end_serial):
        step = (end_serial - start_serial) // self.num_threads
        threads = []

        for i in range(self.num_threads):
            start = start_serial + i * step
            end = start + step if i < self.num_threads - 1 else end_serial
            thread = threading.Thread(target=self._scrape_and_store, args=(start, end))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        deleted_rows = self._delete_long_chinese_names()
        print("已删除的数据：")
        for row in deleted_rows:
            print(row)

    def _scrape_and_store(self, start_serial, end_serial):
        for serial_number in range(start_serial, end_serial + 1):
            url = f"https://www.dushu.com/book/{serial_number}/"
            response = requests.get(url)

            if response.status_code != 200:
                print(f"无法获取图书编号为{serial_number}的数据")
                continue

            tree = html.fromstring(response.content)
            book_data = self._extract_book_data(tree)

            if book_data:
                self._insert_into_database(book_data)

    def _extract_book_data(self, tree):
        book_title_elements = tree.xpath("/html/body/div[6]/div[1]/div[1]/h1")
        if not book_title_elements:
            print("无法提取图书标题")
            return None
        book_title = book_title_elements[0].text_content()
        price_element = tree.xpath("/html/body/div[6]/div[1]/div[3]/div[1]/p/span")[0]
        price_text_cleaned = price_element.text_content().replace("¥", "").strip()
        author = tree.xpath("/html/body/div[6]/div[1]/div[3]/div[1]/table/tbody/tr[1]/td[2]")[0].text_content()
        publisher = tree.xpath("/html/body/div[6]/div[1]/div[3]/div[1]/table/tbody/tr[2]/td[2]")[0].text_content()
        book_number = tree.xpath("/html/body/div[6]/div[1]/div[3]/table/tbody/tr[1]/td[2]")[0].text_content()
        image_url = tree.xpath("/html/body/div[6]/div[1]/div[2]/div[1]/img/@src")[0]

        return {
            "book_title": book_title,
            "price": price_text_cleaned,
            "author": author,
            "publisher": publisher,
            "book_number": book_number,
            "image_url": image_url
        }

    def _insert_into_database(self, book_data):
        connection = pymysql.connect(**self.db_config)
        insert_query = "INSERT INTO appbook01_prettynum (book_name, Price, author, Publishing_house, mobile, coverUrl, region, level, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (book_data["book_title"], book_data["price"], book_data["author"], book_data["publisher"],
                book_data["book_number"], book_data["image_url"], 'A', 4, 1)

        try:
            with connection.cursor() as cursor:
                cursor.execute(insert_query, data)
                connection.commit()
                print(f"图书编号为{book_data['book_number']}的数据插入成功")
        except Exception as e:
            print(f"插入数据失败：{e}")
            connection.rollback()
        finally:
            connection.close()

    def _delete_long_chinese_names(self):
        deleted_rows = []

        connection = pymysql.connect(**self.db_config)
        try:
            with connection.cursor() as cursor:
                select_sql = "SELECT * FROM appbook01_prettynum WHERE CHAR_LENGTH(book_name) > 8"
                cursor.execute(select_sql)
                deleted_rows = cursor.fetchall()

                delete_sql = "DELETE FROM appbook01_prettynum WHERE CHAR_LENGTH(book_name) > 8"
                cursor.execute(delete_sql)

            connection.commit()
        except Exception as e:
            print(f"删除数据失败：{e}")
            connection.rollback()
        finally:
            connection.close()

        return deleted_rows


# 配置数据库连接
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "hy064872",
    "db": "mybook",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor
}

# 创建书籍爬虫对象，指定线程数
book_scraper = BookScraper(db_config, num_threads=40)
# 开始爬取并存储数据
book_scraper.scrape_and_store_range(13992182, 13992382)
