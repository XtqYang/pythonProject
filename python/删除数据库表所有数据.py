import mysql.connector

# MySQL数据库连接信息
mysql_host = "localhost"
mysql_user = "root"
mysql_password = "hy064872"
mysql_database = "tiktok"


def delete_all_data_from_table():
    """
    删除tiktok表中的所有数据
    """
    try:
        # 连接MySQL数据库
        db = mysql.connector.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_password,
            database=mysql_database
        )
        cursor = db.cursor()

        # 执行DELETE语句删除所有数据
        delete_query = "DELETE FROM douyin"
        cursor.execute(delete_query)

        # 提交更改
        db.commit()

        print("表中的所有数据已成功删除。")

    except Exception as e:
        # 出现错误时回滚
        db.rollback()
        print(f"错误: {str(e)}")

    finally:
        # 关闭游标和数据库连接
        cursor.close()
        db.close()


if __name__ == "__main__":
    # 删除tiktok表中的所有数据
    s = input("输入确认开始删除无法取消:")
    if s == "确认":
        delete_all_data_from_table()
    else:
        print("已取消")
