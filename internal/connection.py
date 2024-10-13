import psycopg2
from psycopg2 import OperationalError
from decouple import config

#PosgteSQLConfig = config('PosgteSQLConfig')

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")

connection = create_connection(
    "booker","root" , "root", "127.0.0.1","5433"
)
select_users = "SELECT guid FROM book_cost_items WHERE id = 5"
users = execute_read_query(connection, select_users)
if '04758184-78c7-455f-91ac-dcb169b9350c' in str(users):
    print('OK')
else: 
    print('error')


connection.close()
