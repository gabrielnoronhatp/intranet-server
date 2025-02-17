from app import create_app
from flask_cors import CORS
from decouple import config

app = create_app()


CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:3000", "https://seudominio.com"],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})


if __name__ == '__main__':
  
    PORT = config('PORT', default=3002, cast=int)
    DEBUG = config('DEBUG', default=True, cast=bool)
    HOST = config('HOST', default='0.0.0.0')

    # Executa a aplicação
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG
    ) 