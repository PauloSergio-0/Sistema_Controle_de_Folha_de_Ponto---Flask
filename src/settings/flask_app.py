from flask import Flask
from routes import init_routes
from database.session import Database
def app_config():
    
    app = Flask(__name__)
    init_routes(app)
    
    Database().create_db()
    
    return app