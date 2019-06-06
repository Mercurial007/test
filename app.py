from flask import Flask, render_template, redirect, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'

app.config['MYSQL_USER'] = 'root'

app.config['MYSQL_PASSWORD'] = 'root'

app.config['MYSQL_DB'] = 'testdb'

mysql = MySQL(app)

@app.route('/')

def index():

    cur = mysql.connection.cursor()

    cur.execute("SELECT Name FROM records")

    rv = cur.fetchall()

    return str(rv)

if __name__ == '__main__':
    app.run(debug=True)
