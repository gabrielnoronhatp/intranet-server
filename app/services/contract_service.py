from app.repositories.contract_repository import ContractRepository
from app.schemas.contract import ContractSchema
import boto3
from botocore.exceptions import ClientError
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from app.models.contract import Contract
import logging

class ContractService:
    def __init__(self):
        self.repository = ContractRepository()
        self.schema = ContractSchema()
        self.s3_client = boto3.client('s3')
        self.bucket_name = os.getenv('S3_BUCKET_NAME')

    def get_service_type_id_by_description(self, description):
        # Implementar lógica para buscar o ID do tipo de serviço pela descrição
        service_type = self.repository.get_service_type_by_description(description)
        if not service_type:
            raise ValueError("Service type not found")
        return service_type.id

    def get_service_type_ids_by_partial_description(self, partial_description):
        # Busca todos os tipos de serviço que contêm a descrição parcial
        service_types = self.repository.get_service_types_by_partial_description(partial_description)
        return [service_type.id for service_type in service_types]

    def get_all_contracts(self, filters=None):
        query = Contract.query
        if filters:
            if 'idtipo' in filters and filters['idtipo']:
                query = query.filter(Contract.idtipo.ilike(f"%{filters['idtipo']}%"))
            if 'nome' in filters and filters['nome']:
                query = query.filter(Contract.nome.ilike(f"%{filters['nome']}%"))
            if 'idfilial' in filters and filters['idfilial']:
                query = query.filter(Contract.idfilial.ilike(f"%{filters['idfilial']}%"))
            if 'data_venc_contrato' in filters and filters['data_venc_contrato']:
                query = query.filter_by(data_venc_contrato=filters['data_venc_contrato'])
            if 'datalanc' in filters and filters['datalanc']:
                query = query.filter_by(datalanc=filters['datalanc'])
            if 'descricao_tipo' in filters and filters['descricao_tipo']:
                service_type_ids = self.get_service_type_ids_by_partial_description(filters['descricao_tipo'])
                if not service_type_ids:
                    raise ValueError("No service types found with the given description")
                query = query.filter(Contract.idtipo.in_(service_type_ids))

        contracts = query.all()
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
            contract = self.get_contract(contract_id)
            if not contract:
                raise ValueError("Contract not found")
            
            filename = secure_filename(file.filename)
            key = f'contracts/{contract_id}/{filename}'
            
            self.s3_client.upload_fileobj(
                Fileobj=file,
                Bucket=self.bucket_name,
                Key=key
            )
            
            return {
                'filename': filename,
                'file_url': f"https://{self.bucket_name}.s3.amazonaws.com/{key}",
                'size': file.size,
            }   
        
        except ClientError as e:
            logging.error(f"Erro ao fazer upload do arquivo do contrato no S3: {str(e)}")
            raise Exception(f"Erro ao fazer upload do arquivo do contrato no S3: {str(e)}")

    def list_contract_files(self, contract_id):
        try:
            prefix = f'contracts/{contract_id}/'
            logging.debug(f"Prefixo usado para listar arquivos: {prefix}")

            files = []
            continuation_token = None

            while True:
                list_params = {
                    'Bucket': self.bucket_name,
                    'Prefix': prefix
                }

                if continuation_token:
                    list_params['ContinuationToken'] = continuation_token

                response = self.s3_client.list_objects_v2(**list_params)

                logging.debug(f"S3 Response: {response}")
                print(response)
                if 'Contents' in response:
                   
                    for obj in response['Contents']:
                        file_url = f"https://{self.bucket_name}.s3.amazonaws.com/{obj['Key']}"
                        filename = obj['Key'].split('/')[-1]

                        files.append({
                            'filename': filename,
                            'file_url': file_url,
                            'size': obj['Size'],
                            'last_modified': obj['LastModified'].isoformat(),
                            'contract_id': contract_id
                        })

                if not response.get('IsTruncated'):  # Verifica se há mais arquivos
                    break

                continuation_token = response.get('NextContinuationToken')

            if not files:
                logging.warning(f"Nenhum arquivo encontrado para o contrato {contract_id}.")
                return {
                    'status_code': 404,
                    'message': f'Nenhum arquivo encontrado para o contrato {contract_id}.',
                    'contract_id': contract_id,
                    'files': []
                }

            return {
                'status_code': 200,
                'contract_id': contract_id,
                'files': files
            }

        except ClientError as e:
            error_message = e.response['Error'].get('Message', str(e))
            logging.error(f"Erro ao listar arquivos do contrato no S3: {error_message}")
            return {
                'status_code': 500,
                'message': 'Erro ao buscar arquivos.',
                'error': error_message
            }
        
        
       



     