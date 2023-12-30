import mysql.connector

dataBase = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'myrestapi',
    password = 'password'
)


cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")
print("All Done!")