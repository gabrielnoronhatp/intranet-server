from app.models.service_type import ServiceType
from app import db
from sqlalchemy import text

class ServiceTypeRepository:
    @staticmethod
    def get_all():
        return ServiceType.query.all()
    
    @staticmethod
    def get_by_id(service_type_id):
        return ServiceType.query.get(service_type_id)
    
    @staticmethod
    def get_next_id():
        result = db.session.execute(text('SELECT COALESCE(MAX(id), 0) + 1 FROM intra.ctt_tipo_contrato'))
        return result.scalar()

    def create(self, service_type_data):
        service_type_data['id'] = self.get_next_id()
        service_type = ServiceType(**service_type_data)
        db.session.add(service_type)
        db.session.commit()
        return service_type
    
    @staticmethod
    def update(service_type, service_type_data):
        for key, value in service_type_data.items():
            setattr(service_type, key, value)
        db.session.commit()
        return service_type
    
    @staticmethod
    def delete(service_type):
        db.session.delete(service_type)
        db.session.commit() 