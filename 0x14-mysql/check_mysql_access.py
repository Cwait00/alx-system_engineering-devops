import mysql.connector

def check_mysql_access(host, user, password):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        print("Successfully connected to MySQL server.")
        connection.close()
    except mysql.connector.Error as error:
        print("Error: Failed to connect to MySQL server:", error)

if __name__ == "__main__":
    # Configuration for web-01 MySQL server
    web_01_host = "web-01"
    web_01_user = "holberton_user"
    web_01_password = "projectcorrection280hbtn"

    # Configuration for web-02 MySQL server
    web_02_host = "web-02"
    web_02_user = "holberton_user"
    web_02_password = "projectcorrection280hbtn"

    print("Checking MySQL access for web-01...")
    check_mysql_access(web_01_host, web_01_user, web_01_password)

    print("\nChecking MySQL access for web-02...")
    check_mysql_access(web_02_host, web_02_user, web_02_password)
