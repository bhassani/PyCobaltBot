#pip install mysql-connector-python
#from mysql.connector import MySQLConnection, Error
#from python_mysql_dbconfig import read_db_config

#pip install pymysql
import pymysql

#https://www.digitalocean.com/community/tutorials/how-to-store-and-retrieve-data-in-mariadb-using-python-on-ubuntu-18-04
#add_data("sample_user")
def add_data(username):
    username = "db_user"
    password = "db_pass"
    connection = database.connect(
    user=username,
    password=password,
    host=localhost,
    database="users")

    cursor = connection.cursor()
    try:
        #https://www.mysqltutorial.org/mysql-insert-ignore/
	    statement = "INSERT IGNORE INTO users (usernames) VALUES (%s)"
	    data = (username)
	    cursor.execute(statement, data)
	    cursor.commit()
	    print("Successfully added entry to database")
    except database.Error as e:
	    print(f"Error adding entry to database: {e}")

#https://www.digitalocean.com/community/tutorials/how-to-store-and-retrieve-data-in-mariadb-using-python-on-ubuntu-18-04
#get_data("sample_user")
def get_data(username):
    #import mysql.connector as database
    username = "db_user"
    password = "db_pass"
    connection = database.connect(
    user=username,
    password=password,
    host=localhost,
    database="users")
    cursor = connection.cursor()
    try:
        statement = "SELECT * FROM users WHERE username=%s"
        data = (username)
        cursor.execute(statement, data)
        for (username) in cursor:
            print(f"Successfully retrieved {username}")
    except database.Error as e:
        print(f"Error retrieving entry from database: {e}")
    connection.close()

#https://www.geeksforgeeks.org/python-mariadb-insert-into-table-using-pymysql/
'''
def mysql_insert(name):
    Host = "localhost"
    # User name of the database server
    User = "db_user"
    # Password for the database user
    Password = "db_pass"
    Database = "users"
    conn = pymysql.connect(host=Host, user=User, password=Password, database=Database)

    # Create a cursor object
    cur = conn.cursor()

    query = f"INSERT INTO USERS (username) VALUES ('{name}')"
    cur.execute(query)
    print(f"{cur.rowcount} details inserted")
    conn.commit()
    conn.close()
'''

#https://www.mysqltutorial.org/python-mysql-insert/
'''
def insert_record(name):
    query = "INSERT INTO users(username) " \
            "VALUES(%s)"
    args = (name)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()
'''

if __name__ == "__main__":
  #read file
  #https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
  with open("example.txt") as file:
    #lines = [line.rstrip() for line in file]
    for line in file:
        print(line.rstrip())
        insert = line.rstrip()
        #add_data(insert)
