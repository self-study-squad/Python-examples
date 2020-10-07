#Test on Remote connection to Database

import mysql.connector

from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='root',
                                  password='0377122966longpham!',
                                  host='localhost',
                                  database='kvdatabase')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password!")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()