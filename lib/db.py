"""数据库操作"""
#coding:utf-8
import pymysql
import sys
sys.path.append("..")    #提升包的搜索路径到项目下。相对引包路径，方便run_all时方便查找，减少出错。无论哪个文件，最好都从项目根目录下找
from config import config as cf  #引入config并设别名

#封装获取连接操作
def get_conn():
    conn = pymysql.connect(host=cf.db_host,
                           port=cf.db_port,
                           user=cf.db_user,
                           password=cf.db_password,
                           db=cf.db,
                           charset='utf8')
    return conn

#封装查询操作
def db_query(sql):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cf.logging.debug(sql)    #DEBUG大写是个数字常量，小写是个方法
    cf.logging.debug(result)
    cur.close()
    conn.close()
    return  result

#封装修改操作
def db_change(sql):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        cf.logging.error(str(e))
    finally:
        cur.close()
        conn.close()

if __name__ == ("__main__"):
    result = db_query("select * from user where name='张三'")
    print(result)


