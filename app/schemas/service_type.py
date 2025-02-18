from marshmallow import Schema, fields
from flask_restx import fields as restx_fields
from flask_restx import Namespace

service_type_ns = Namespace('service-types', description='Service Types operations')


class ServiceTypeSchema(Schema):
    id = fields.Int(dump_only=True)
    descricao = fields.Method('get_formatted_description', dump_only=True)
    last_update = fields.DateTime(dump_only=True)

    def get_formatted_description(self, obj):
        return f"{obj.id}-{obj.descricao.strip().lower()}"


service_type_model = service_type_ns.model('ServiceType', {
    'id': restx_fields.Integer(readonly=True),
    'descricao': restx_fields.String(readonly=True),
    'last_update': restx_fields.DateTime(readonly=True)
})

# Schema instances
service_type_schema = ServiceTypeSchema()
service_types_schema = ServiceTypeSchema(many=True) 