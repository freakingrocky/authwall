from hash_pass import hash_password, check_hash
from mysql.connector import Error
from mysql.connector import connect

db_pass = "Rocky123"


def recover_password():
    global cursor
    username = str(input("Enter Username: "))
    cursor.execute(f"select sqone, sqtwo, sqthree, hashcode from info where username='{username}'")
    sq_one = check_hash(cursor.fetchone()[0], str(input("Name of father: ")))
    sq_two = check_hash(cursor.fetchone()[0], str(input("Name of favorite pornstar: ")))
    sq_three = check_hash(cursor.fetchone()[0], str(input("Name of favorite pornsite: ")))
    if sq_one and sq_two and sq_three:
        hashcode = str(hash_password(str(input("Enter New Password: "))))
        password = check_hash(cursor.fetchone()[0], hashcode)
        if password:
            cursor.execute(f"UPDATE info SET hashcode='{hashcode}' WHERE username='{username}'")
            connection.commit()
        else:
            print('loda le le mera')


def delete_user():
    global cursor
    username = str(input("Enter Username: "))
    cursor.execute(f"select hashcode from info where username='{username}'")
    password = check_hash(cursor.fetchone()[0], str(input("Enter PASSWORD: ")))
    if password:
        cursor.execute(f"delete from info where username='{username}'")
        connection.commit()
    else:
        print("You do not have authorization")


def login():
    global cursor
    username = str(input("Enter Username: "))
    cursor.execute(f"select hashcode from info where username='{username}'")
    password = check_hash(cursor.fetchone()[0], str(input("Enter PASSWORD: ")))
    if password:
        print("Succesfully logged in")
    else:
        print("Not Unsuccessful logged in")


def register():
    global cursor
    username = str(input("Enter Username: "))
    hashcode = str(hash_password(str(input("Enter Password: "))))
    print("Security Questions")
    sqone = str(hash_password(str(input("What's your father's name: "))))
    sqtwo = str(hash_password(str(input("Who is your favorite pornstar: "))))
    sqthree = str(hash_password(str(input("What is your favorite pornsite: "))))
    cursor.execute(f"insert into info values ('{username}', '{hashcode}', '{sqone}', '{sqtwo}', '{sqthree}')")
    connection.commit()


if __name__ == '__main__':
    global cursor
    # db_pass = input("For Administrators! (press enter to use default) enter DB password: ")
    connection = connect(
        host='localhost', database='login', user='SuperUser', password=db_pass)

    try:
        if connection.is_connected():
            cursor = connection.cursor()
        cursor = connection.cursor()
        print("\033[A                                               \033[A")
        print("Connected Succesfully")
        print("""Operations:
                1) Register New User
                2) Login
                3) Delete User
                4) Reset Password
                5) Exit""")
        while True:
            operation = int(input("Enter Operation: "))
            if operation == 1:
                register()
            if operation == 2:
                login()
            if operation == 3:
                delete_user()
            if operation == 4:
                recover_password()
            if operation == 5:
                exit()
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")