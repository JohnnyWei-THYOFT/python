import mysql.connector

mysql_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456"
)

cursor = mysql_connection.cursor()
cursor.execute("USE mysql")
cursor.execute("select * from t")
rows = cursor.fetchall()

# 印出結果
for row in rows:
    print(row)

# 關閉 cursor 和連線
cursor.close()
mysql_connection.close()