from cryptography.fernet import Fernet
import mysql.connector

connection=mysql.connector.connect(host="localhost",user="root",password="unni123",database="pass_manages")
cursor=connection.cursor()
key=Fernet.generate_key()
cypher=Fernet(key)
cursor.execute("DESCRIBE users")

# Print results line by line
for row in cursor.fetchall():
    print(row)
def add():
    uname=input("Enter UserName: ")
    passw=input("Enter password: ")
    passw=cypher.encrypt(passw.encode())
    cursor.execute("insert into users(user,password) VALUES (%s, %s)" ,(uname,passw))

def show_all():
    cursor.execute("select user,password from users")

    for i in cursor.fetchall():
        print(f"User name:{i[0]}\nPassword:{cypher.decrypt(i[1]).decode()}\n")
def specific():
    name=input("Enter the user name you want the password for: ")
    cursor.execute("select user,password from users where user= %s",(name,))
    for i in cursor.fetchall():
        print(f"User name:{name}\nPassword:{cypher.decrypt(i[1]).decode()}\n")

while True:
    mode= input("what would you like to do(show_all/specific/add/quit:")
    if mode=="quit":
        break
    if mode=="show_all":
        show_all()
    elif mode=="specific":
        specific()
    elif mode=="add":
        add()

