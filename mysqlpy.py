import mysql
from mysql.connector import Error


def check():
    username=str(input("Enter Username: "))
    password=str(input("Enter PASSWORD: "))
    cursor.execute(f"select Password from info where Username='{username}'")

    record = cursor.fetchone()
    print(record[0])
    if password==record[0]:
        print('Successfully Logged In!!')
        return
    else:
        print('Please try again..')


connection = mysql.connector.connect(host='localhost',database='login',user='root',password='santa2003')
try:
    if connection.is_connected():
        cursor = connection.cursor()
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        print("You are connected to database")
        check()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")