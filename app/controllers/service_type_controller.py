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
            service_type_data = request.get_json()
            return self.service.create(service_type_data), 201
        except Exception as e:
            abort(400, message=str(e))

    def update(self, id):
        try:
            service_type_data = request.get_json()
            return self.service.update(id, service_type_data)
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