import mysql.connector
import mysql.connector
import concurrent.futures

"""
***********该程序用于返回无法访问的图片名称********************
使用需要传入线程数max_workers，和表名table_name
Error_link：返回无法访问的图片名称
max_workers:指定线程数
"""

import requests
import mysql.connector


class DatabaseConnection:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(**self.db_config)
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            print(f"数据库连接错误: {err}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()


class BookProcessor:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    @staticmethod
    def process_book(cover_url, book_name, failed_books):
        try:
            response = requests.get(cover_url)
            response.raise_for_status()

            # 在此处添加处理获得的数据的逻辑

        except requests.exceptions.RequestException as e:
            failed_books.append(book_name)  # 记录无法访问的图书名称
        except Exception as e:
            print(f"处理URL {cover_url} 时发生错误: {e}")


def Error_link(max_workers, table_name):
    print("正在检查链接中....")
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "hy064872",
        "database": "mybook"
    }

    db_connection = DatabaseConnection(db_config)
    db_connection.connect()

    failed_books = []

    select_query = f"SELECT coverUrl, book_name FROM {table_name}"
    db_connection.cursor.execute(select_query)
    rows = db_connection.cursor.fetchall()

    # 使用多线程处理
    with concurrent.futures.ThreadPoolExecutor(max_workers) as executor:
        futures = []
        for row in rows:
            cover_url, book_name = row
            future = executor.submit(BookProcessor.process_book, cover_url, book_name, failed_books)
            futures.append(future)

        # 等待所有线程完成
        concurrent.futures.wait(futures)

    db_connection.close()
    print("检查完成共有" + len(failed_books).__str__() + "个链接不能访问")
    return failed_books
