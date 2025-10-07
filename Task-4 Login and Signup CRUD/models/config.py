import pymysql

def dbconnect():
    return pymysql.connect(
        host='localhost',
        user='dckap',
        password='Dckap2023Ecommerce',
        database='users'
    )


