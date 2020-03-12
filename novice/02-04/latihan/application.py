class Application(object):
    def __init__(self):
        pass

#main.py
Application.postgres_connection = PostgresConnection()

#other.py
postgres_connection = Application.postgres_connection
db_data = postgres_connection.fetchone()