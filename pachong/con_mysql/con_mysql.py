import pymysql

DBHOST = 'localhost'
DBUSER = 'root'
DBPASS = '123456'
DBNAME = 'test_py'

try:
    db = pymysql.connect(host=DBHOST, user=DBUSER, password=DBPASS, db=DBNAME)
    print('数据库连接成功')
except pymysql.Error as e:
    print('数据库连接失败：' + str(e))

cursor = db.cursor()
# sql = """create table user(
#         account char(10) not null,
#         password char(18) not null,
#         name varchar(20))"""
sql = 'insert into user values("10011","123456","张三")'

try:
    cursor.execute(sql)
    db.commit()
    print('完成')
except:
    db.rollback()
    print("失败")

db.close()
