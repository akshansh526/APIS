from flask import Flask,jsonify,request
import  mysql.connector
from flask_mysqldb import MySQL

mysql = MySQL(app)

cursor = mysql.connection.cursor()

app = Flask(__name__)
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="exams_db"
)
mycursor = mydb.cursor()

@app.route('/ques', methods = ['GET'])
def ReturnJSON_auto(var):
    if(request.method == 'GET'):
        mycursor.execute(sql)
        sql=("Show tables;")
        # mycursor.execute("SELECT * FROM `quiz_2` WHERE 1")
        myresult = mycursor.fetchall()
        return jsonify(myresult)
        
mysql.connection.commit()

# mycursor.execute("Show tables;")
# mycursor.execute("SELECT * FROM quiz")
# myresult = mycursor.fetchall()
 
# for x in myresult:
#     print(x)



# @app.route('/', methods = ['GET', 'POST'])
# def hello_world():
    
#     return 'Hello From Server'

# @app.route('/total_ques')
# def total_ques():
#     return '10'





# @app.route('/ques/', methods = ['GET'])
# def ReturnJSON():
#     # print(request.data )
#     data = request.data
#     if(request.method == 'GET'):
#         # mycursor.execute("Show tables;")
#         mycursor.execute("SELECT * FROM quiz_1 WHERE id=1")
#         myresult = mycursor.fetchall()
#         return jsonify(myresult)

# @app.route('/ques/01', methods = ['GET'])
# def ReturnJSON01():
#     if(request.method == 'GET'):
#         # mycursor.execute("Show tables;")
#         mycursor.execute("SELECT * FROM quiz_1 WHERE id=1")
#         myresult = mycursor.fetchall()
#         return jsonify(myresult)

# @app.route('/ques/02', methods = ['GET'])
# def ReturnJSON02():
#     if(request.method == 'GET'):
#         # mycursor.execute("Show tables;")
#         mycursor.execute("SELECT * FROM quiz_1 WHERE id=2")
#         myresult = mycursor.fetchall()
#         return jsonify(myresult)
 
if __name__ == '__main__':
    app.run()