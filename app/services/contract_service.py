from app.repositories.contract_repository import ContractRepository
from app.schemas.contract import ContractSchema
import boto3
from botocore.exceptions import ClientError
from werkzeug.utils import secure_filename
import os
from datetime import datetime

class ContractService:
    def __init__(self):
        self.repository = ContractRepository()
        self.schema = ContractSchema()
        self.s3_client = boto3.client('s3')
        self.bucket_name = os.getenv('S3_BUCKET_NAME')

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

    def upload_contract_file(self, contract_id, file):
        try:
            # Verifica se o contrato existe
            contract = self.get_contract(contract_id)
            
            # Gera um nome seguro para o arquivo com timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            original_filename = secure_filename(file.filename)
            filename = f"{timestamp}_{original_filename}"
            
            # Define o caminho no S3: contracts/ID_DO_CONTRATO/ARQUIVO
            file_key = f'contracts/{contract_id}/{filename}'
            
            # Realiza o upload para o S3
            self.s3_client.upload_fileobj(
                file,
                self.bucket_name,
                file_key,
                ExtraArgs={
                    'ContentType': file.content_type
                }
            )
            
            # Gera a URL do arquivo
            file_url = f"https://{self.bucket_name}.s3.amazonaws.com/{file_key}"
            
            # Aqui você pode salvar a referência do arquivo no banco de dados
            # self.save_contract_file_reference(contract_id, file_url, filename)
            
            return {
                'message': 'Arquivo enviado com sucesso',
                'file_url': file_url,
                'filename': filename,
                'contract_id': contract_id
            }
            
        except ClientError as e:
            raise Exception(f"Erro ao fazer upload do arquivo para S3: {str(e)}") 