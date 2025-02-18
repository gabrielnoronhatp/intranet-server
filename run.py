from app import create_app
from decouple import config

app = create_app()


if __name__ == '__main__':
  
    PORT = config('PORT', default=3002, cast=int)
    DEBUG = config('DEBUG', default=True, cast=bool)
    HOST = config('HOST', default='0.0.0.0')
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG
    ) 