import pymysql.cursors
#链接数据库
connection= pymysql.connect(host='localhost' , user='root', passwd='123456', db ='scraping')
#获取游标
cursor = connection.cursor()
#插入数据
cursor.execute("INSERT INTO urls (url, content) VALUES ('www.google.com', 'Google')")
connection.commit()
print('成功插入', cursor.rowcount, '条数据')
#修改数据
cursor.execute("update urls set url='www.baidu.com',content='baidu' where id =4")
connection.commit()
print('成功修改', cursor.rowcount, '条数据')
#查询数据
cursor.execute("select * from urls where id =2")
connection.commit()
print('成功查询', cursor.rowcount, '条数据')
#删除数据
cursor.execute('delete from urls where id>4')
connection.commit()
print('成功删除', cursor.rowcount, '条数据')
try:
    cursor.execute("update urls set url='www.baidu.com',content='baidu' where id =4")
except Exception as e:
    connection.rollback()  # 事务回滚
    print('事务处理失败', e)
else:
    connection.commit()  # 事务提交
    print('事务处理成功', cursor.rowcount)
#关闭链接
cursor.close()
connection.close()