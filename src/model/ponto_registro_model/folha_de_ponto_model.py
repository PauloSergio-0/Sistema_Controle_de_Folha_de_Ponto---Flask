import sqlite3 as con
from database.session import Database



class FolhaPonto:
    
    def folhaPonto_table():
        
        with open("src/sql/folha_de_ponto_sql/table_folha_de_ponto.sql", 'r') as file:
            table_sql = file.read()
        
        connection = con.connect(Database().connetionDB)
        cursor = connection.cursor()
        cursor.execute(table_sql)
        connection.commit()
        connection.close()