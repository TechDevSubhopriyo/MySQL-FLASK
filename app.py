from flask import Flask, redirect, request, render_template
from flask_mysqldb import MySQL
import time

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_DB'] = 'python_test'


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/registration")
def register():
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    age = request.args.get('age')
    language = request.args.get('language')
    cur = mysql.connection.cursor()
    sql = "INSERT INTO `user` (`id`, `First_Name`, `Last_Name`, `Age`, `Language_Preference`, `created_time`) VALUES (NULL, '"+fname+"', '"+lname+"', '"+age+"', '"+language+"', '"+str(time.time())+"');"
    cur.execute(sql)
    return redirect('/', 302, None)

mysql = MySQL(app)
if  __name__ == "__main__" :
    app.run();