#!C:\Users\devik\AppData\Local\Microsoft\WindowsApps\python.exe
import cgi
import cgitb
import mysql.connector

cgitb.enable()
print("Content-type:text/html\n")
try:
    form=cgi.FieldStorage()
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cgi_db"
    )
    cursor=conn.cursor()
    action=form.getvalue("action")

    if action=="Create":
        username=form.getvalue('username')
        password=form.getvalue('password')
        cursor.execute("INSERT INTO user(username,password) values(%s,%s)",(username,password))
        conn.commit()
        print("Created succesfully")

    elif action=="Update":
        username=form.getvalue('username')
        newusername=form.getvalue('newusername')
        password=form.getvalue('password')
        cursor.execute("UPDATE user SET username=%s,password=%s where username=%s",(username,password,newusername))
        conn.commit()
        print("Updated succesfully")

    elif action=="Read":
        username=form.getvalue('username')
        cursor.execute("SELECT * from user")
        result=cursor.fetchall()
        for i in result:
           print(f"<p>Username:{i[0]},Password:{i[1]}") 

    elif action == 'Delete':
        username = form.getvalue('username')
        cursor.execute("DELETE FROM user WHERE username = %s", (username,))
        conn.commit()
        print(f"<p>User {username} deleted successfully!</p>")

    # Handle invalid action
    else:
        print("<p>Invalid action.</p>")  
except:
    
    conn.close()



sum