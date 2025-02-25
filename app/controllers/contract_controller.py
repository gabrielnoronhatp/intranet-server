from flask import request, jsonify, send_file
from flask_restx import abort
from app.services.contract_service import ContractService
import os
from botocore.exceptions import ClientError
import logging

class ContractController:
    def __init__(self):
        self.service = ContractService()

    def get_all_contracts(self, filters):
        try:
            return self.service.get_all_contracts(filters)
        except Exception as e:
            abort(500, message=f"Error retrieving contracts: {str(e)}")

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
            
            # Preencher campos secundários com valores primários se não estiverem preenchidos
            contract_data['telefone2'] = contract_data.get('telefone2') or contract_data.get('telefone1')
            contract_data['email2'] = contract_data.get('email2') or contract_data.get('email1')
            contract_data['endereco2'] = contract_data.get('endereco2') or contract_data.get('endereco1')
            
            return self.service.create_contract(contract_data), 201
        except Exception as e:
            abort(400, message=str(e))

    def update_contract(self, contract_id):
        try:
            contract_data = request.get_json()
            
            # Preencher campos secundários com valores primários se não estiverem preenchidos
            contract_data['telefone2'] = contract_data.get('telefone2') or contract_data.get('telefone1')
            contract_data['email2'] = contract_data.get('email2') or contract_data.get('email1')
            contract_data['endereco2'] = contract_data.get('endereco2') or contract_data.get('endereco1')
            
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

    def list_contract_files(self, contract_id):
        try:
            files = self.service.list_contract_files(contract_id)
            logging.debug(f"Arquivos retornados: {files}")
            return jsonify(files)
        except ValueError as e:
            abort(404, message=str(e))
        except Exception as e:
            abort(500, message=str(e))

    def download_contract_file(self, contract_id, filename):
        try:
            # Obter o caminho do arquivo no S3
            file_key = f'contracts/{contract_id}/{filename}'
            
            # Baixar o arquivo do S3 para um local temporário
            temp_file_path = f'/tmp/{filename}'
            self.service.s3_client.download_file(self.service.bucket_name, file_key, temp_file_path)
            
            # Enviar o arquivo para o cliente
            return send_file(temp_file_path, as_attachment=True)
        
        except ClientError as e:
            abort(404, message=f"Erro ao baixar o arquivo: {str(e)}")
        except Exception as e:
            abort(500, message=str(e))

    def _allowed_file(self, filename, allowed_extensions):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in allowed_extensions