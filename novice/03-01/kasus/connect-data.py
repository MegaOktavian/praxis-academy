import psycopg2 

conn = psycopg2.connect(
    user='root',
    password='',
    host='localhost',
    port=26257,
    database='kasus'
) 

conn.set_session(autocommit=True)
cur = conn.cursor() 

cur.execute("select movie_rented from movie where member_id=1")

rows = cur.fetchall()
print('Janet Jones rent:')
for row in rows: 
    print([str(cell) for cell in row])

cur.close()
conn.close()