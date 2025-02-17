from flask_restx import Api, Resource, Namespace, fields
from flask_cors import cross_origin
from app.controllers.contract_controller import ContractController


api = Api(
    title='Intranet-API',
    version='1.0',
    description='API para gerenciamento de serviços da INTRANET',
    doc='/',
    prefix='/api' 
)
ns = Namespace('contracts', description='Operações de contratos')
api.add_namespace(ns)


contract_model = api.model('Contract', {
    'id': fields.Integer(readonly=True, description='ID do contrato'),
    'idtipo': fields.Integer(required=True, description='Tipo do contrato'),
    'idfilial': fields.Integer(required=True, description='ID da filial'),
    'idfornecedor': fields.Integer(required=True, description='ID do fornecedor'),
    'nome': fields.String(required=True, description='Nome'),
    'telefone1': fields.String(description='Telefone principal'),
    'telefone2': fields.String(description='Telefone secundário'),
    'endereco1': fields.String(description='Endereço principal'),
    'endereco2': fields.String(description='Endereço secundário'),
    'email1': fields.String(description='Email principal'),
    'email2': fields.String(description='Email secundário'),
    'data_venc_contrato': fields.Date(description='Data de vencimento'),
    'indice': fields.String(description='Índice'),
    'forma_pag': fields.String(description='Forma de pagamento'),
    'agencia': fields.String(description='Agência'),
    'conta': fields.String(description='Conta'),
    'tipo_chave_pix': fields.String(description='Tipo de chave PIX'),
    'chave_pix': fields.String(description='Chave PIX'),
    'valor_multa': fields.Float(description='Valor da multa'),
    'percentual_multa': fields.Float(description='Percentual da multa'),
    'obs1': fields.String(description='Observação 1'),
    'obs2': fields.String(description='Observação 2'),
    'datalanc': fields.Date(description='Data de lançamento'),
    'userlanc': fields.String(description='Usuário de lançamento'),
    'cancelado': fields.Boolean(description='Status de cancelamento')
})

controller = ContractController()

@ns.route('/')
class ContractList(Resource):
    @cross_origin()
    @ns.doc('list_contracts')
    @ns.marshal_list_with(contract_model)
    def get(self):
        """Lista todos os contratos"""
        return controller.get_all_contracts()

    @cross_origin()
    @ns.doc('create_contract')
    @ns.expect(contract_model)
    @ns.marshal_with(contract_model, code=201)
    def post(self):
        """Cria um novo contrato"""
        return controller.create_contract()

@ns.route('/<int:contract_id>')
@ns.param('contract_id', 'ID do contrato')
class Contract(Resource):
    @ns.doc('get_contract')
    @ns.marshal_with(contract_model)
    def get(self, contract_id):
        """Obtém um contrato específico"""
        return controller.get_contract(contract_id)

    @ns.doc('update_contract')
    @ns.expect(contract_model)
    @ns.marshal_with(contract_model)
    def put(self, contract_id):
        """Atualiza um contrato"""
        return controller.update_contract(contract_id)

    @ns.doc('delete_contract')
    @ns.response(204, 'Contrato removido')
    def delete(self, contract_id):
        """Remove um contrato"""
        return controller.delete_contract(contract_id) 