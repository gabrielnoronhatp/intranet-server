from flask_restx import Resource, Namespace, fields
from app.controllers.service_type_controller import ServiceTypeController
from app.routes.api import api

# Criar namespace
ns = Namespace('service-types', description='Operações com tipos de serviço')

# Registrar namespace na API principal
api.add_namespace(ns)

# Modelo usando o namespace
service_type_model = ns.model('ServiceType', {
    'id': fields.Integer(readonly=True, description='ID do tipo de serviço'),
    'descricao': fields.String(required=True, description='Descrição do tipo de serviço'),
    'last_update': fields.DateTime(readonly=True, description='Data da última atualização')
})

controller = ServiceTypeController()

@ns.route('/')
class ServiceTypeList(Resource):
    @ns.doc('list_service_types')
    @ns.marshal_list_with(service_type_model)
    def get(self):
        """Lista todos os tipos de serviço"""
        return controller.get_all()

    @ns.doc('create_service_type')
    @ns.expect(service_type_model)
    @ns.marshal_with(service_type_model, code=201)
    def post(self):
        """Cria um novo tipo de serviço"""
        return controller.create()

@ns.route('/<int:id>')
@ns.param('id', 'ID do tipo de serviço')
class ServiceTypeResource(Resource):
    @ns.doc('get_service_type')
    @ns.marshal_with(service_type_model)
    def get(self, id):
        """Obtém um tipo de serviço específico"""
        return controller.get_by_id(id)

    @ns.doc('update_service_type')
    @ns.expect(service_type_model)
    @ns.marshal_with(service_type_model)
    def put(self, id):
        """Atualiza um tipo de serviço"""
        return controller.update(id)

    @ns.doc('delete_service_type')
    @ns.response(204, 'Tipo de serviço removido')
    def delete(self, id):
        """Remove um tipo de serviço"""
        return controller.delete(id) 