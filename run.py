from app import create_app
from decouple import config
from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, doc='/swagger')  # Define a rota para o Swagger

# Exemplo de um namespace e rota
ns = api.namespace('example', description='Example operations')

@ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    PORT = config('PORT', default=5000, cast=int)
    DEBUG = config('DEBUG', default=True, cast=bool)
    HOST = config('HOST', default='0.0.0.0')
    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG
    ) 