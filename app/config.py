from decouple import config

class Config:
    # Database
    PG_USER = config('PG_USER')
    PG_PASSWORD = config('PG_PASSWORD')
    PG_HOST = config('PG_HOST')
    PG_PORT = config('PG_PORT')
    PG_DATABASE = config('PG_DATABASE')
    
    # Construir a URL de conexão do PostgreSQL
    SQLALCHEMY_DATABASE_URI = f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}'
    
    # Outras configurações
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SCHEMA_NAME = 'intra'
    SECRET_KEY = config('SECRET_KEY')

    # Configurações CORS
    CORS_HEADERS = 'Content-Type'
    
    # Em desenvolvimento, permitir todos os origens
    CORS_ORIGINS = "*"
    
    # Em produção, especificar as origens permitidas:
    # CORS_ORIGINS = [
    #     "http://localhost:3000",
    #     "http://127.0.0.1:3000",
    #     "http://seu-dominio.com"
    # ] 