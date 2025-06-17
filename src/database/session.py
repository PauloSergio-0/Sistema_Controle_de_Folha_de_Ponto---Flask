import sqlite3 as con
from sqlalchemy import create_engine
from settings.database_config import folhaPonto
import os


class Database:
    def __init__(self):
        self.url = folhaPonto.URL_DATABASE
        self.connetionDB = str(self.url + folhaPonto.DATABASE)
    
    def create_db(self):
        
        if  not os.path.exists(self.url):
            os.makedirs(self.url, exist_ok=True)
            con.connect(self.connetionDB)
            
            
        else:
            con.connect(self.connetionDB)
        
    def exist_db(self):
        
        if not os.path.exists(self.connetionDB):
            return False
        
        return True