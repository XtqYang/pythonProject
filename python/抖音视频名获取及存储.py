import os
import re
import mysql.connector
from datetime import datetime

# MySQL数据库连接信息
mysql_host = "localhost"
mysql_user = "root"
mysql_password = "hy064872"
mysql_database = "tiktok"


class DatabaseHandler:
    @staticmethod
    def create_table():
        """
        创建数据库表（如果不存在）
        """
        create_table_query = """
        CREATE TABLE IF NOT EXISTS wenan (
            id INT AUTO_INCREMENT PRIMARY KEY,
            time DATETIME,
            copywriting VARCHAR(255),
            Blogger_id VARCHAR(255),
            Blogger_name VARCHAR(255)
        )
        """
        db = mysql.connector.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_password,
            database=mysql_database
        )
        cursor = db.cursor()
        cursor.execute(create_table_query)
        cursor.close()
        db.close()

    @staticmethod
    def insert_data(time, copywriting, bi, bn):
        """
        向数据库插入数据
        """
        db = mysql.connector.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_password,
            database=mysql_database
        )
        cursor = db.cursor()
        insert_query = "INSERT INTO wenan (time, copywriting, Blogger_id, Blogger_name) VALUES (%s, %s, %s, %s)"
        values = (time, copywriting, bi, bn)
        cursor.execute(insert_query, values)
        db.commit()
        cursor.close()
        db.close()


class FileHandler:
    def __init__(self, folder_path, bi, bn):
        self.folder_path = folder_path
        self.bi = bi
        self.bn = bn

    def process_files(self):
        """
        处理文件夹中的文件，提取信息并插入数据库
        """
        file_pattern = r"(\d{4}-\d{2}-\d{2} \d{2}\.\d{2}\.\d{2})(.*?)\.mp4"
        for filename in os.listdir(self.folder_path):
            match = re.match(file_pattern, filename)
            if match:
                time_str, copywriting = match.groups()
                time = datetime.strptime(time_str, "%Y-%m-%d %H.%M.%S")
                print("时间:", time, "文案:", copywriting)
                DatabaseHandler.insert_data(time, copywriting, self.bi, self.bn)

    def remove_duplicate_copywriting_rows(self):
        """
        删除数据库中重复的copywriting行
        """
        db = mysql.connector.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_password,
            database=mysql_database
        )
        cursor = db.cursor()

        try:
            # 查找重复的copywriting行
            query = """
                SELECT MIN(id) AS id, time, copywriting, Blogger_id, Blogger_name
                FROM wenan
                GROUP BY time, copywriting, Blogger_id, Blogger_name
                HAVING COUNT(*) > 1
            """

            cursor.execute(query)
            duplicate_rows = cursor.fetchall()

            for row in duplicate_rows:
                id_, time, copywriting, Blogger_id, Blogger_name = row

                # 删除除最小id外的重复行
                delete_query = """
                    DELETE t1
                    FROM wenan t1
                    JOIN wenan t2
                    ON t1.time = t2.time
                    AND t1.copywriting = t2.copywriting
                    AND t1.Blogger_id = t2.Blogger_id
                    AND t1.Blogger_name = t2.Blogger_name
                    WHERE t1.id > t2.id
                    AND t1.time = %s
                    AND t1.copywriting = %s
                    AND t1.Blogger_id = %s
                    AND t1.Blogger_name = %s
                """
                delete_data = (time, copywriting, Blogger_id, Blogger_name)
                cursor.execute(delete_query, delete_data)

            # 提交更改
            db.commit()

            print("重复的copywriting行已成功删除。")

        except Exception as e:
            # 出现错误时回滚
            db.rollback()
            print(f"错误: {str(e)}")

        finally:
            # 关闭游标和数据库连接
            cursor.close()
            db.close()


if __name__ == "__main__":
    # Blogger_id和Blogger_name
    # id
    bi = "Zxz.tian519"
    # 名称
    bn = "Fairy✨治愈馆主"
    # 文件夹路径
    folder_path = r"D:/code/pythonProject/python/TikTokDownload-main/Download/post/" + bn + "/"

    # 创建数据库表（如果不存在）
    DatabaseHandler.create_table()

    # 处理文件并插入数据库
    file_handler = FileHandler(folder_path, bi, bn)
    file_handler.process_files()

    # 删除重复的copywriting行
    # file_handler.remove_duplicate_copywriting_rows()
