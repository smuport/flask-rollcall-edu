import pymysql


def connect_db():
    db = pymysql.connect('数据库地址', '用户名', '密码', '数据库名称')
    return db
