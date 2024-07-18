import mysql.connector

# The connection object database allows you to interact with the MySQL server, such as executing queries and fetching results.
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Successpeter29!'
)

# The cursor is used to execute SQL commands
cursor_object = database.cursor()
 
#  This method executes an SQL statement using the cursor object.
cursor_object.execute("CREATE DATABASE elderco")

print("All done")