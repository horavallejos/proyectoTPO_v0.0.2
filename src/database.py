import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='peques',
)

# FIN ARCHIVO CONEXION A BASE DE DATOS