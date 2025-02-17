from app.repositories.contract_repository import ContractRepository
from app.schemas.contract import ContractSchema

class ContractService:
    def __init__(self):
        self.repository = ContractRepository()
        self.schema = ContractSchema()

    def get_all_contracts(self):
        contracts = self.repository.get_all()
        return self.schema.dump(contracts, many=True)

    def get_contract(self, contract_id):
        contract = self.repository.get_by_id(contract_id)
        if not contract:
            raise ValueError("Contract not found")
        return self.schema.dump(contract)

    def create_contract(self, contract_data):
        validated_data = self.schema.load(contract_data)
        contract = self.repository.create(validated_data)
        return self.schema.dump(contract)

    def update_contract(self, contract_id, contract_data):
        contract = self.repository.get_by_id(contract_id)
        if not contract:
            raise ValueError("Contract not found")
        validated_data = self.schema.load(contract_data, partial=True)
        updated_contract = self.repository.update(contract, validated_data)
        return self.schema.dump(updated_contract)

    def delete_contract(self, contract_id):
        contract = self.repository.get_by_id(contract_id)
        if not contract:
            raise ValueError("Contract not found")
        self.repository.delete(contract) 