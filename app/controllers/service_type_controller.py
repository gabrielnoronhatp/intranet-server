from flask import request
from flask_restx import abort
from app.services.service_type_service import ServiceTypeService

class ServiceTypeController:
    def __init__(self):
        self.service = ServiceTypeService()

    def get_all(self):
        try:
            return self.service.get_all()
        except Exception as e:
            abort(500, message=str(e))

    def get_by_id(self, id):
        try:
            return self.service.get_by_id(id)
        except ValueError as e:
            abort(404, message=str(e))
        except Exception as e:
            abort(500, message=str(e))

    def create(self):
        try:
            data = request.get_json()
            # Remove o ID se estiver na descrição (formato: "id - descricao")
            if 'descricao' in data and ' - ' in data['descricao']:
                data['descricao'] = data['descricao'].split(' - ', 1)[1]
            return self.service.create(data), 201
        except Exception as e:
            abort(400, message=str(e))

    def update(self, id):
        try:
            data = request.get_json()
            return self.service.update(id, data)
        except ValueError as e:
            abort(404, message=str(e))
        except Exception as e:
            abort(400, message=str(e))

    def delete(self, id):
        try:
            self.service.delete(id)
            return '', 204
        except ValueError as e:
            abort(404, message=str(e))
        except Exception as e:
            abort(500, message=str(e)) 