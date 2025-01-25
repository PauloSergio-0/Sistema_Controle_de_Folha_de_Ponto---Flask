import sqlite3 as con
from database.session import Database



class Funcionario:
    
    def funcionario_table():
        
        with open("src/sql/funcionario_sql/table_funcionario.sql", "r") as file:
            table_sql = file.read()
        
        connection = con.connect(Database().connetionDB)
        cursor = connection.cursor()
        cursor.execute(table_sql)
        connection.commit()
        connection.close()