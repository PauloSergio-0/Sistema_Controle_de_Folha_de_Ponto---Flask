from flask import Flask
from .test_routes import test_routes
from .funcionario import routes_funcionario

def init_routes (app:Flask):
    
    routes_funcionario(app)
    test_routes(app)