#!/usr/bin/python
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', password='', database='employees')
cursor = mariadb_connection.cursor()

cursor.execute("SELECT first_name,last_name FROM employees WHERE first_name=%s", (some_name,))

try:
    cursor.execute("some MariaDB query")
except mariadb.Error as error:
    print("Error: {}".format(error))
