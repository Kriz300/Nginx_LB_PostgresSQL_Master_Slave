from flask import Flask, redirect, url_for, request
import psycopg2
import os

app = Flask(__name__)

conn_master= "host='localhost' dbname='my_database' user='user2' password='password2' port='55432'"
master = psycopg2.connect(conn_master)

conn_slave = "host='localhost' dbname='my_database' user='user2' password='password2' port='65432'"
slave = psycopg2.connect(conn_slave)

@app.route("/hello")
def hello_world():
    return "<p>PID: " + str(os.getpid()) + "</p>"

@app.route("/GetProduct/<name>",methods = ['GET'])
def get(name):
    cur = slave.cursor()
    query = "select * from product where lower(product.name) like '%{}%';".format(name.lower())
    cur.execute(query)
    response = cur.fetchall()
    cur.close()

    return "<p>PID: " + str(response) + "</p>"

@app.route("/AddProduct",methods = ['POST'])
def add():
    cur = master.cursor()
    query = "insert into product(name, price) values ('{}', {});".format(request.form['name'].lower(), request.form['price'])
    cur.execute(query)
    cur.close()
    return "<p>PID: " + os.getpid() + "</p>"
