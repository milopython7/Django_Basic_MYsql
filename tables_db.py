import mysql.connector

mi_db= mysql.connector.connect(
    host="localhost",
    user="milo",
    password="Milodevops7",
    database= "ecommerce")

mi_cursor = mi_db.cursor()

#Crear una tabla 
sql = """ CREATE TABLE cliente(
            nombre VARCHAR(255),
            apellido VARCHAR(255)) """

mi_cursor.execute(sql)

# Eliminar una tabla
# deleteTable = "DROP TABLE IF EXISTS cliente"
# mi_cursor.execute(deleteTable)

# Mostrar todas las tablas
mi_cursor.execute("SHOW TABLES")
for tablas in mi_cursor:
    print(tablas)

mi_db.close()