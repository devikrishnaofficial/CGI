#!C:\Users\devik\AppData\Local\Microsoft\WindowsApps\python.exe
import cgi
import cgitb
import mysql.connector

cgitb.enable()


print("Content-type:text/html\n")

try:
    form = cgi.FieldStorage()  # Get form data
    myDb = mysql.connector.connect(host="localhost", user="root", password="", database="cgi_db")        # Connect to the database
    myCursor = myDb.cursor()   # Create a cursor to execute queries

    action = form.getvalue('action')  # Get the action (Create, Read, Update, Delete)

    # Create operation
    if action == 'Create':
        username = form.getvalue('username')
        password = form.getvalue('password')
        myCursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
        myDb.commit()
        print(f"<p>User {username} created successfully!</p>")

    # Read operation
    elif action == 'Read':
        username = form.getvalue('username')
        myCursor.execute("SELECT * FROM user WHERE username = %s", (username,))
        user_data = myCursor.fetchall()
        if user_data:
            for row in user_data:
                print(f"<p>Username: {row[0]}, Password: {row[1]}</p>")
        else:
            print("<p>No user found.</p>")

    # Update operation
    elif action == 'Update':
        old_username = form.getvalue('old_username')
        new_username = form.getvalue('new_username')
        new_password = form.getvalue('new_password')
        myCursor.execute("UPDATE user SET username = %s, password = %s WHERE username = %s", (new_username, new_password, old_username))
        myDb.commit()
        print(f"<p>User {old_username} updated successfully!</p>")

    # Delete operation
    elif action == 'Delete':
        username = form.getvalue('username')
        myCursor.execute("DELETE FROM user WHERE username = %s", (username,))
        myDb.commit()
        print(f"<p>User {username} deleted successfully!</p>")

    # Handle invalid action
    else:
        print("<p>Invalid action.</p>")

except Exception as e:
    print(f"<p>Error: {e}</p>")

finally:
    myDb.close()  
