import json
import os
import sys

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import mysql.connector
from concurrent.futures import ThreadPoolExecutor

# 从环境变量或配置文件中读取数据库凭据
DB_USERNAME = os.environ.get("DB_USERNAME", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "hy064872")
DB_NAME = os.environ.get("DB_NAME", "mybook")


class BookDatabase:
    def __init__(self, username, password, database):
        self.connection = self._connect_to_database(username, password, database)

    def _connect_to_database(self, username, password, database):
        connection = mysql.connector.connect(
            host="localhost",
            user=username,
            password=password,
            database=database
        )
        return connection

    def fetch_book_names(self, table_name):
        if not self.connection:
            return []

        with self.connection.cursor() as cursor:
            query = f"SELECT book_name FROM {table_name}"
            cursor.execute(query)
            book_names = [row[0] for row in cursor.fetchall()]
            return book_names

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("数据库连接已关闭")


class ImageScraper:
    def __init__(self):
        self.base_url = "https://cn.bing.com/images/async"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
        }
        self.batch_size = 35

    def find_image_urls(self, html):
        soup = BeautifulSoup(html, 'lxml')
        image_elements = soup.find_all('a', attrs='iusc')
        image_urls = [json.loads(image_element["m"])["murl"] for image_element in image_elements]
        return image_urls

    def get_image_urls(self, keywords, max_number=10000):
        crawled_urls = []
        try:
            keywords_str = "&q={}".format(quote(keywords))
            query_url = f"{self.base_url}?count={self.batch_size}" + keywords_str

            def get_image_urls(page):
                image_urls = []
                url = query_url + f"&first={page * self.batch_size}&SFX={page}"
                response = requests.get(url, headers=self.headers)
                response.raise_for_status()
                image_urls += self.find_image_urls(response.text)
                return image_urls

            for page in range(0, (max_number + self.batch_size) // self.batch_size + 1):
                crawled_urls.extend(get_image_urls(page))

        except requests.RequestException as e:
            print(f"网络请求异常：{e}")

        crawled_urls = list(set(filter(lambda url: url.lower().endswith('.jpg'), crawled_urls)))
        return crawled_urls[:min(len(crawled_urls), max_number)]


def process_book(book_name, image_scraper, db_username, db_password, db_name, table_name):
    book_db = BookDatabase(db_username, db_password, db_name)
    try:
        res = image_scraper.get_image_urls(book_name, max_number=1)
        if res:
            new_cover_url = res[0]
            with book_db.connection.cursor() as cursor:
                update_query = f"UPDATE {table_name} SET coverUrl = %s WHERE book_name = %s"
                cursor.execute(update_query, (new_cover_url, book_name))
                book_db.connection.commit()
                print(f"已更新书籍 {book_name} 的封面URL")
    except mysql.connector.Error as err:
        print(f"数据库错误：{err}")
        sys.exit()
    finally:
        book_db.close_connection()


class MainLogic:
    def __init__(self):
        self.db_username = DB_USERNAME
        self.db_password = DB_PASSWORD
        self.db_name = DB_NAME
        self.table_name = "appbook01_prettynum"
        self.thread_count = 15

    def run(self):
        book_db = BookDatabase(self.db_username, self.db_password, self.db_name)

        try:
            book_names = book_db.fetch_book_names(self.table_name)  # 用fetch_book_names替代了Error_link
            image_scraper = ImageScraper()

            with ThreadPoolExecutor(max_workers=self.thread_count) as executor:
                for book_name in book_names:
                    executor.submit(process_book, book_name, image_scraper, self.db_username, self.db_password,
                                    self.db_name, self.table_name)

        finally:
            book_db.close_connection()


if __name__ == "__main__":
    print("开始更新图片链接")
    main_logic = MainLogic()
    main_logic.run()
    print("更新完成")
