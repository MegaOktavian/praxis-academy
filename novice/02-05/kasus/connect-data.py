import mysql.connector

cnx = mysql.connector.connect(user='mega', password='12345',database='kasus')
cursor = cnx.cursor()

query = ("select movies_rented from movie where member_id=1")

cursor.execute(query)
print("Janet Jones rents: ")

for (movies_rented) in cursor:
  print("{}".format(movies_rented))

cursor.close()
cnx.close()