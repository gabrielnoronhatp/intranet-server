from flask_restx import Api

api = Api(
    title='Intranet-API',
    version='1.0',
    description='API para gerenciamento de serviços da INTRANET',
    doc='/',
    prefix='/api'
) 