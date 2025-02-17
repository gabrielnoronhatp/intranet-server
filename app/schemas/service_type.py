from marshmallow import Schema, fields
from flask_restx import fields as restx_fields
from flask_restx import Namespace

# Create namespace for service types
service_type_ns = Namespace('service-types', description='Service Types operations')

# Marshmallow schema for serialization/deserialization
class ServiceTypeSchema(Schema):
    id = fields.Int(dump_only=True)
    descricao = fields.Str(required=True)
    last_update = fields.DateTime(dump_only=True)

# Flask-RestX model for API documentation
service_type_model = service_type_ns.model('ServiceType', {
    'id': restx_fields.Integer(readonly=True),
    'descricao': restx_fields.String(required=True),
    'last_update': restx_fields.DateTime(readonly=True)
})

# Schema instances
service_type_schema = ServiceTypeSchema()
service_types_schema = ServiceTypeSchema(many=True) 