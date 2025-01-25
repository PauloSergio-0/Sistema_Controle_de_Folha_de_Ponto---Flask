from flask import Flask
from routes import init_routes
from database.session import Database
from model.funcionario_model.funcionario_model import Funcionario
from model.ponto_registro_model.folha_de_ponto_model import FolhaPonto

def app_config():
    
    app = Flask(__name__)
    init_routes(app)
    
    Database().create_db()
    
    if Database().exist_db():
        Funcionario.funcionario_table()
        FolhaPonto.folhaPonto_table()
        
    return app