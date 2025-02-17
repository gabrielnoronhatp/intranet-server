from app.repositories.service_type_repository import ServiceTypeRepository
from app.schemas.service_type import ServiceTypeSchema

class ServiceTypeService:
    def __init__(self):
        self.repository = ServiceTypeRepository()
        self.schema = ServiceTypeSchema()

    def get_all(self):
        service_types = self.repository.get_all()
        return self.schema.dump(service_types, many=True)

    def get_by_id(self, service_type_id):
        service_type = self.repository.get_by_id(service_type_id)
        if not service_type:
            raise ValueError("Service type not found")
        return self.schema.dump(service_type)

    def create(self, service_type_data):
        validated_data = self.schema.load(service_type_data)
        service_type = self.repository.create(validated_data)
        return self.schema.dump(service_type)

    def update(self, service_type_id, service_type_data):
        service_type = self.repository.get_by_id(service_type_id)
        if not service_type:
            raise ValueError("Service type not found")
        validated_data = self.schema.load(service_type_data, partial=True)
        updated_service_type = self.repository.update(service_type, validated_data)
        return self.schema.dump(updated_service_type)

    def delete(self, service_type_id):
        service_type = self.repository.get_by_id(service_type_id)
        if not service_type:
            raise ValueError("Service type not found")
        self.repository.delete(service_type) 