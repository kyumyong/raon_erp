# DB interface using QtSql
from PyQt5 import QtSql
from PyQt5.QtWidgets import QApplication
import sys

 # def connection_db():
   # db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
   # db.setDatabaseName('sports.db')

# 	app = QApplication(sys.argv)
# 	main_window = MainWindow()
# 	main_window.show()
# 	sys.exit(app.exec_())


# if __name__ == "__main__":
	# connection_db()


# this little monkey has to be here
app = QApplication(sys.argv)

db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
db.setDatabaseName("test")
# db.setDatabaseName("mydb")
# # db.setDatabaseName("C:\\Program Files\\mariadb-5.5.54-winx64\\data\\test\\db.opt")
db.setHostName("localhost")
# # db.setHostName("skenovo.synology.me")
# # db.setHostName("211.63.33.76")
# # db.setPort(5000)
# # db.setPort(80)
# db.setUserName("root")
db.setUserName("kmlee")
db.setPassword("0202")
# db.setPort(3306)
# db.setConnectOptions("ISC_DPB_LC_CTYPE=Latin1");
# db.setConnectOptions("ISC_DPB_LC_CTYPE=utf8");
db.setConnectOptions("CHARACTER_SET=utf8");
# db.setConnectOptions("default_character_set=utf8");
# db.setConnectOptions("ISC_DPB_LC_CTYPE=en_US.UTF-8");
# db.set('utf8')
# charset='utf8'
ok = db.open()
# print(ok)
# print(db.lastError().text())

# # http://skenovo.synology.me:5000/

query = QtSql.QSqlQuery()
# query.exec_("SET character_set_client = utf8")
# query.exec_("SET default_character_set = utf8")
query.exec_("SELECT * FROM Books")
# query.exec_("SELECT\
# 	*\
# 	FROM\
# 	Books")
# query.exec_("SELECT * FROM dept")

while query.next():
	# print(query.value(0).toString())
	print(query.value(1))
# for row in query:
# 	print(row)
db.close()


# # DB interface using pymysql
# import pymysql
# import sys

# print(sys.stdin.encoding)

# connection = pymysql.connect(host='localhost',
#                              user='root',
#                              password='0202',
#                              db='test',
#                              charset='utf8')
#                              # charset='euc-kr')
#                              # charset='cp949')
# # connection = pymysql.connect(host='211.63.33.76',
# #                              user='kmlee')
# #                              # password='0202',
# #                              # db='test')
# #                              # charset='CHAR_SET')

# print(sys.stdin.encoding)

# cursor = connection.cursor()
# # cursor.execute("SHOW DATABASES")
# # cursor.execute("SHOW TABLES")
# # cursor.execute("CREATE TABLE Books (BookID int(11) NOT NULL,Title varchar(100) NOT NULL,CONSTRAINT Books_PK PRIMARY KEY (BookID))")
# # cursor.execute("DESCRIBE Books")
# # cursor.execute("INSERT INTO Books (BookID,Title) VALUES (121,'myBOoK')")
# # cursor.execute("INSERT INTO Books (BookID,Title) VALUES (122,'myBOoK1')")
# # cursor.execute("INSERT INTO Books (BookID,Title) VALUES (124,'myBOoK2')")
# # cursor.execute("INSERT INTO Books (BookID,Title) VALUES (126,'내사랑')")
# cursor.execute("SELECT * FROM Books")
# # cursor.execute("SHOW VARIABLES LIKE 'c%'")

# # cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES")
# # cursor.execute("SHOW VARIABLES LIKE 'performance_schema'")
# # cursor.execute("SELECT * FROM INFORMATION_SCHEMA.ENGINES WHERE ENGINE='PERFORMANCE_SCHEMA'")
# # cursor.execute("USE performance_schema")
# # cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'performance_schema'")

# # data = cursor.fetchmany(3)
# # print(data)
# for row in cursor:
# 	print(row)
# # print("Database version : %s " % data)

# connection.close()

