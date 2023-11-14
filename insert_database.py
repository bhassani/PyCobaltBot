from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

#https://www.mysqltutorial.org/python-mysql-insert/
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
      
if __name__ == "__main__":
  #read file 
  #https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list
  with open("example.txt") as file:
    #lines = [line.rstrip() for line in file]
    for line in file:
        print(line.rstrip())

        #store in queue

        #worker thread to insert into DB
        insert_record(line)
  
