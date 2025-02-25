from flask_restx import Resource, Namespace, fields
from flask_cors import cross_origin
from app.controllers.contract_controller import ContractController
from app.routes.api import api
from flask import request


ns = Namespace('contracts', description='Operações de contratos')
api.add_namespace(ns)


contract_model = ns.model('Contract', {
    'id': fields.Integer(readonly=True, description='ID do contrato'),
    'idtipo': fields.String(required=True, description='ID do tipo de serviço'),
    'idfilial': fields.String(required=True, description='ID da filial'),
    'idfornecedor': fields.String(required=True, description='ID do fornecedor'),
    'nome': fields.String(required=True, description='Nome'),
    'telefone1': fields.String(description='Telefone principal'),
    'telefone2': fields.String(description='Telefone secundário', allow_null=True),
    'endereco1': fields.String(description='Endereço principal'),
    'endereco2': fields.String(description='Endereço secundário', allow_null=True),
    'email1': fields.String(description='Email principal'),
    'email2': fields.String(description='Email secundário', allow_null=True),
    'data_venc_contrato': fields.Date(description='Data de vencimento'),
    'banco': fields.String(description='Banco'),
    'indice': fields.String(description='Índice'),
    'forma_pag': fields.String(description='Forma de pagamento'),
    'agencia': fields.String(description='Agência'),
    'conta': fields.String(description='Conta'),
    'tipo_chave_pix': fields.String(description='Tipo de chave PIX', allow_null=True),
    'chave_pix': fields.String(description='Chave PIX', allow_null=True),
    'valor_multa': fields.Float(description='Valor da multa'),
    'percentual_multa': fields.Float(description='Percentual da multa', allow_null=True),
    'obs1': fields.String(description='Observação 1'),
    'obs2': fields.String(description='Observação 2', allow_null=True),
    'datalanc': fields.Date(description='Data de lançamento'),
    'userlanc': fields.String(description='Usuário de lançamento', allow_null=True),
    'cancelado': fields.Boolean(description='Status de cancelamento')
})

controller = ContractController()

# Definindo o modelo para a resposta de arquivo
@ns.route('/')
class ContractList(Resource):
    @cross_origin()
    @ns.doc('list_contracts')
    @ns.param('idtipo', 'ID do tipo de serviço', _in='query')
    @ns.param('nome', 'Nome do contrato', _in='query')
    @ns.param('idfilial', 'ID da filial', _in='query')
    @ns.param('data_venc_contrato', 'Data de vencimento', _in='query')
    @ns.param('datalanc', 'Data de lançamento', _in='query')
    @ns.param('descricao_tipo', 'Descrição do tipo de serviço', _in='query')
    @ns.marshal_list_with(contract_model)
    def get(self):
        args = request.args
        return controller.get_all_contracts(args)

    @cross_origin()
    @ns.doc('create_contract')
    @ns.expect(contract_model)
    @ns.marshal_with(contract_model, code=201)
    def post(self):
        return controller.create_contract()

@ns.route('/<int:contract_id>')
@ns.param('contract_id', 'ID do contrato')
class Contract(Resource):
    @ns.doc('get_contract')
    @ns.marshal_with(contract_model)
    def get(self, contract_id):
        return controller.get_contract(contract_id)

    @ns.doc('update_contract')
    @ns.expect(contract_model)
    @ns.marshal_with(contract_model)
    def put(self, contract_id):
        return controller.update_contract(contract_id)

    @ns.doc('delete_contract')
    @ns.response(204, 'Contrato removido')
    def delete(self, contract_id):
        return controller.delete_contract(contract_id)

@ns.route('/<int:contract_id>/files')
@ns.param('contract_id', 'ID do contrato')
class ContractFiles(Resource):
    @ns.doc('get_contract_files')
    def get(self, contract_id):
        """Lista todos os arquivos de um contrato específico"""
        return controller.list_contract_files(contract_id)

    @ns.doc('upload_contract_file')
    @ns.expect(ns.parser().add_argument('file', 
        location='files', 
        type='FileStorage', 
        required=True,
        help='Arquivo do contrato'))
    @ns.response(200, 'Arquivo enviado com sucesso')
    def post(self, contract_id):
        """Faz upload de um arquivo para um contrato específico"""
        return controller.upload_contract_file(contract_id) 
    
@ns.route('/<int:contract_id>/files/<string:filename>')
@ns.param('contract_id', 'ID do contrato')
@ns.param('filename', 'Nome do arquivo')
class ContractFileDownload(Resource):
    @ns.doc('download_contract_file')
    def get(self, contract_id, filename):
        return controller.download_contract_file(contract_id, filename)
    