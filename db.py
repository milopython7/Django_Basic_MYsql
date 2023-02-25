import mysql.connector

mi_db= mysql.connector.connect(
    host="localhost",
    user="milo",
    password="Milodevops7" )

mi_cursor = mi_db.cursor()


# Creacion de bd desde python
sql = "CREATE DATABASE ecommerce"
mi_cursor.execute(sql)

# deleteDatabase = "DROP DATABASE ecommerce"
# mi_cursor.execute(deleteDatabase)

# mostrar todas las bases de datos desde python
showDatabases = "SHOW DATABASES"
mi_cursor.execute(showDatabases)

for items in mi_cursor:
    print(items)

mi_db.close()