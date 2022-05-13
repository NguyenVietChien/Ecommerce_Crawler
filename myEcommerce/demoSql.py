import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='12345',
    database='myecommerce',
)

mycursor = mydb.cursor()

sql = "SELECT product_name FROM myecommerce_tb ORDER BY total_comments DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)