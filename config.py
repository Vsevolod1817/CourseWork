import mysql.connector

mydb = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'port': '3306',
    'database': 'Mydatabase',
    'auth_plugin': 'mysql_native_password'
}

"""mc = mydb.cursor()

mc.execute('SELECT * FROM department')

users = mc.fetchall()

for user in users:
    print(user)"""