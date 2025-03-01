from app.models.contract import Contract
from app import db
from sqlalchemy import text
from app.models.service_type import ServiceType

class ContractRepository:
    @staticmethod
    def get_all():
        return Contract.query.filter_by(cancelado=False).all()
    
    @staticmethod
    def get_by_id(contract_id):
        return Contract.query.get(contract_id)
    
    @staticmethod
    def get_next_id():
        result = db.session.execute(text('SELECT COALESCE(MAX(id), 0) + 1 FROM intra.ctt_contratos'))
        return result.scalar()

    def create(self, contract_data):
    
        contract_data['id'] = self.get_next_id()
        
        contract = Contract(**contract_data)
        db.session.add(contract)
        db.session.commit()
        return contract
    
    @staticmethod
    def update(contract, contract_data):
        for key, value in contract_data.items():
            setattr(contract, key, value)
        db.session.commit()
        return contract
    
    @staticmethod
    def delete(contract):
        contract.cancelado = True
        db.session.commit()

    @staticmethod
    def get_service_type_by_description(description):
        return ServiceType.query.filter_by(descricao=description).first()

    @staticmethod
    def get_service_types_by_partial_description(partial_description):
        return ServiceType.query.filter(ServiceType.descricao.ilike(f"%{partial_description}%")).all() 