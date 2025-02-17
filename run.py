from app import create_app
from flask_cors import CORS
from decouple import config

# Cria a instância da aplicação
app = create_app()

# Configuração mais restritiva do CORS
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:3000", "https://seudominio.com"],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# Configurações de execução
if __name__ == '__main__':
    # Pega configurações do .env
    PORT = config('PORT', default=3002, cast=int)
    DEBUG = config('DEBUG', default=True, cast=bool)
    HOST = config('HOST', default='0.0.0.0')

    # Executa a aplicação
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG
    ) 