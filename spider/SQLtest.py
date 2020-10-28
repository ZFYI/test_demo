import sqlite3

conn = sqlite3.connect('test.db')       #打开或创建数据库文件

c = conn.cursor()                   #获取游标

sql = '''
select * from student;
'''

a = c.execute(sql)          #执行SQL语句
# conn.commit()           #提交数据库操作
# conn.close()            #关闭数据库连接

for i in a:
    print(i)
conn.close()