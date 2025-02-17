from decouple import config

class Config:
    # Database
    PG_USER = config('PG_USER')
    PG_PASSWORD = config('PG_PASSWORD')
    PG_HOST = config('PG_HOST')
    PG_PORT = config('PG_PORT')
    PG_DATABASE = config('PG_DATABASE')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SCHEMA_NAME = 'intra'
    SECRET_KEY = config('SECRET_KEY')
    CORS_HEADERS = 'Content-Type'
    CORS_ORIGINS = "*"
    
    