from flask import request
from flask_restx import abort
from app.services.contract_service import ContractService

class ContractController:
    def __init__(self):
        self.service = ContractService()

    def get_all_contracts(self):
        try:
            return self.service.get_all_contracts()
        except Exception as e:
            abort(500, message=str(e))

    def get_contract(self, contract_id):
        try:
            return self.service.get_contract(contract_id)
        except ValueError as e:
            abort(404, message=str(e))
        except Exception as e:
            abort(500, message=str(e))

    def create_contract(self):
        try:
            contract_data = request.get_json()
            return self.service.create_contract(contract_data), 201
        except Exception as e:
            abort(400, message=str(e))

    def update_contract(self, contract_id):
        try:
            contract_data = request.get_json()
            return self.service.update_contract(contract_id, contract_data)
        except ValueError as e:
            abort(404, message=str(e))
        except Exception as e:
            abort(400, message=str(e))

    def delete_contract(self, contract_id):
        try:
            self.service.delete_contract(contract_id)
            return '', 204
        except ValueError as e:
            abort(404, message=str(e))
        except Exception as e:
            abort(500, message=str(e)) 