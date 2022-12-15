# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password=""
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE newdb")

#If this page is executed with no error, you have successfully created a database.

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password=""
# )

# mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="newdb"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="newdb"
# )

# mycursor = mydb.cursor()

# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#      print(x)

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="newdb"
# )

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers2 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="newdb"
# )

# mycursor = mydb.cursor()

# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="newdb"
# )

# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")
from flask import Flask,jsonify,request

import mysql.connector


app = Flask(__name__)



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="newdb"
)
mycursor = mydb.cursor()

@app.route('/ques/', methods = ['GET'])
def ReturnJSON():
    # print(request.data )
    data = request.data
    if(request.method == 'GET'):
        # mycursor.execute("Show tables;")
        mycursor.execute("SELECT questions FROM quiz_new WHERE id=1")
        myresult = mycursor.fetchall()
        return jsonify(myresult)

# @app.route('/total_ques/', methods = ['GET'])
# def ReturnJSON_2():
#     # print(request.data )
#     data2 = request.data2
#     if(request.method == 'GET'):
#         # mycursor.execute("Show tables;")
#         mycursor.execute("SELECT opt_a FROM quiz_new WHERE id=1")
#         myresult = mycursor.fetchall()
#         return jsonify(myresult)
@app.route('/ques/02', methods = ['GET'])
def ReturnJSON02():
    if(request.method == 'GET'):
        mycursor.execute("Show tables;")
        mycursor.execute("SELECT opt_a FROM quiz_new WHERE id=1")
        myresult = mycursor.fetchall()
        return jsonify(myresult)
 
if __name__ == '__main__':
    app.run()        

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")



# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql, val)

# mydb.commit()

# print("1 record inserted, ID:", mycursor.lastrowid)


# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# mycursor.execute("SELECT name, address FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#      print(x)

# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

# mycursor.execute( "SELECT * FROM customers WHERE address ='Park Lane 38'")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# sql = "SELECT * FROM customers WHERE address LIKE '%Side%'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)
# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# sql = "SELECT * FROM customers ORDER BY name ASC"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)