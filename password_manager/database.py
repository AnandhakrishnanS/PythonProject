import mysql.connector

connection=mysql.connector.connect(host="localhost",user="root",password="unni123")
cursor=connection.cursor()

cursor.execute("create database if not exists pass_manages")
cursor.execute("use pass_manages")
cursor.execute("create table if not exists users(id int auto_increment primary key,username varchar(20),password varchar(200),masterpass varchar(100))")

connection.commit()
connection.close()