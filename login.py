#!C:\Users\devik\AppData\Local\Microsoft\WindowsApps\python.exe

import cgi
import cgitb
cgitb.enable()

# Parse form data
form = cgi.FieldStorage()

# Get username and password
username = form.getvalue("username")
password = form.getvalue("password")

# Validate credentials (replace with actual validation)
# if username == "admin" and password == "password":
print("Content-type: text/html\n\n")
print("<h1>",username,"</h1>")
print("<h1>",password,"</h1>")
