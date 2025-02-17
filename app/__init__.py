from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configurar CORS
    CORS(app, resources={
        r"/*": {
            "origins": "*",  # Em produção, especifique os domínios permitidos
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
            "supports_credentials": True
        }
    })

    # Configurar headers de segurança
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response

    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        # Removemos a criação do schema e apenas criamos as tabelas
        # Assumindo que o schema 'intra' já existe
        db.create_all()

    from app.routes.contract_routes import api
    api.init_app(app)

    return app 