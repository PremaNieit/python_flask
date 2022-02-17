from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import re
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'roytuts'
 
mysql = MySQL(app)
@app.route('/')
def home():
    cur= mysql.connection.cursor()
    cur.execute("SELECT * FROM users ")
    fetchdata=cur.fetchall()
    cur.close()

    return render_template('new.html' , data = fetchdata)
  
if __name__ == "__main__":
    app.run()