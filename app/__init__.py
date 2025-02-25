from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://10.2.10.17:2002"], "supports_credentials": True}})
    
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

  
    from app.routes.api import api
    from app.routes import contract_routes, service_type_routes
    
    api.init_app(app)

    return app 