import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Database
    PG_USER = os.getenv('PG_USER')
    PG_PASSWORD = os.getenv('PG_PASSWORD')
    PG_HOST = os.getenv('PG_HOST')
    PG_PORT = os.getenv('PG_PORT')
    PG_DATABASE = os.getenv('PG_DATABASE')
    SQLALCHEMY_DATABASE_URI = f'postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SCHEMA_NAME = 'intra'
    SECRET_KEY = os.getenv('SECRET_KEY')
    CORS_HEADERS = 'Content-Type'
    CORS_ORIGINS = "*" 