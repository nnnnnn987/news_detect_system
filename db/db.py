import os
import pandas as pd
from sqlalchemy import create_engine
import pymysql

engine = create_engine('mysql+pymysql://root:123456@192.168.56.101:3306/library')  # 这里直接使用pymysql连接,echo=True，会显示在加载数据库所执行的SQL语句。
# 函数创建一个数据库引擎，连接到 MySQL 数据库。

#定义一个函数 get_models，用于从数据库中获取书籍名称数据。
def get_models():

    # sql 命令
    sql_cmd = "SELECT name  FROM books "

    df = pd.read_sql_table(table_name='books', con=engine)
    return df

#定义另一个函数 get_datasets，用于从数据库中获取书籍分类名称数据。
def get_datasets():
    # sql 命令
    sql_cmd = "SELECT name  FROM book_sort "

    df = pd.read_sql(sql=sql_cmd, con=engine)
    return df

#当前代码中没有处理数据库连接失败或查询错误的情况，这可能会导致程序崩溃或返回不友好的错误信息。我们可以添加异常处理机制，捕获可能的错误并进行适当的处理，如记录日志、返回默认值或重新连接等。
def fetch_data(table_name, columns=['*']):
    try:
        sql_cmd = f"SELECT {', '.join(columns)} FROM {table_name}"
        df = pd.read_sql(sql=sql_cmd, con=engine)
        return df
    except Exception as e:
        print(f"Error fetching data from {table_name}: {e}")
        # 可以选择记录日志、返回空 DataFrame 或重新抛出异常
        return pd.DataFrame()