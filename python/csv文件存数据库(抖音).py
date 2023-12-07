import csv
import os
import pymysql


class DataImporter:
    def __init__(self, db_config, db_table, db_author_column):
        self.db_config = db_config
        self.db_table = db_table
        self.db_author_column = db_author_column

    def insert_data_into_database(self, author, csv_file_path, column_indices):
        # 建立数据库连接
        connection = pymysql.connect(**self.db_config)
        try:
            with connection.cursor() as cursor:
                with open(csv_file_path, 'r', encoding='gbk') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    next(csv_reader)  # 跳过CSV文件的标题行
                    for row in csv_reader:
                        data_to_insert = [author.encode('utf-8')] + [row[i] for i in column_indices]
                        # 构建插入数据的SQL语句
                        sql = f"INSERT INTO {self.db_table} (author, Work_id, time, title, Collect, review, give_a_like, Share, Share_link) " \
                              f"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        # 执行插入操作
                        cursor.execute(sql, tuple(data_to_insert))
                # 提交更改到数据库
                connection.commit()
                print("数据插入成功！")
        except Exception as e:
            print("插入数据时出错：", e)
        finally:
            # 关闭数据库连接
            connection.close()


class FolderScanner:
    def __init__(self, db_config, db_table, db_author_column):
        self.db_config = db_config
        self.db_table = db_table
        self.db_author_column = db_author_column

    def list_folders_not_in_db(self, directory):
        missing_folders = []
        csv_files_paths = []
        # 获取指定目录下的所有直接子文件夹名称
        folders = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

        # 连接到MySQL数据库
        connection = pymysql.connect(
            host=self.db_config['host'],
            user=self.db_config['user'],
            password=self.db_config['password'],
            database=self.db_config['database'],
            charset='utf8mb4'
        )

        cursor = connection.cursor()

        existing_folders = set()

        try:
            # 查询数据库中已有的文件夹名称
            query = f"SELECT {self.db_author_column} FROM {self.db_table}"
            cursor.execute(query)

            for row in cursor.fetchall():
                existing_folders.add(row[0])

            # 输出数据库中不存在的文件夹名称和CSV文件路径
            for folder in folders:
                if folder not in existing_folders:
                    missing_folders.append(folder)
                    folder_path = os.path.join(directory, folder)
                    # 获取文件夹的所有CSV文件路径
                    csv_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if
                                 file.lower().endswith('.csv')]
                    csv_files_paths.append(csv_files)

        except pymysql.Error as err:
            print("错误:", err)

        cursor.close()
        connection.close()

        return missing_folders, csv_files_paths


if __name__ == "__main__":
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'hy064872',
        'database': 'tiktok',
    }

    db_table = "douyin"
    db_author_column = "author"

    scanner = FolderScanner(db_config, db_table, db_author_column)
    importer = DataImporter(db_config, db_table, db_author_column)

    path = r"D:\浏览器下载\douyin_spider-main"
    missing_folders, csv_files_paths = scanner.list_folders_not_in_db(path)

    for csv_files in csv_files_paths:
        for csv_file in csv_files:
            path_parts = csv_file.split("\\")
            desired_data = path_parts[3]
            author = desired_data
            print(author)
            column_indices = [0, 1, 2, 4, 5, 6, 7, 8]
            for csv_file_path in csv_files:
                importer.insert_data_into_database(author, csv_file_path, column_indices)
