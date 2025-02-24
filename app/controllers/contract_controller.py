from flask import request, jsonify
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

    def upload_contract_file(self, contract_id):
        try:
            if 'file' not in request.files:
                abort(400, message="Nenhum arquivo fornecido")
            
            file = request.files['file']
            if file.filename == '':
                abort(400, message="Nenhum arquivo selecionado")

            # Verifica extensões permitidas
            allowed_extensions = {'pdf', 'doc', 'docx', 'xls', 'xlsx'}
            if not self._allowed_file(file.filename, allowed_extensions):
                abort(400, message="Tipo de arquivo não permitido")

            result = self.service.upload_contract_file(contract_id, file)
            return jsonify(result)
        except ValueError as e:
            abort(404, message=str(e))
        except Exception as e:
            abort(500, message=str(e))

    def get_contract_files(self, contract_id):
        try:
            files = self.service.list_contract_files(contract_id)
            return jsonify(files)
        except ValueError as e:
            abort(404, message=str(e))
        except Exception as e:
            abort(500, message=str(e))

    def _allowed_file(self, filename, allowed_extensions):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in allowed_extensions