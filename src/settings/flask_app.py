from flask import Flask
from routes import init_routes

def app_config():
    app = Flask(__name__)
    init_routes(app)
    return app