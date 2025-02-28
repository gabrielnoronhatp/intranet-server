from marshmallow import Schema, fields, validate

class ContractSchema(Schema):
    id = fields.Int(dump_only=True)
    idtipo = fields.Str(required=True)
    idfilial = fields.Str(required=True)
    idfornecedor = fields.Str(required=True)
    dia_vencimento = fields.Str(required=True)
    valor_contrato = fields.Decimal(places=2)
    nome = fields.Str(required=True)
    telefone1 = fields.Str()
    data_inicio_contrato = fields.Date(allow_none=True)
    banco = fields.Str(allow_none=True)
    telefone2 = fields.Str(allow_none=True)
    endereco1 = fields.Str()
    endereco2 = fields.Str(allow_none=True)
    email1 = fields.Str()
    email2 = fields.Str(allow_none=True)
    data_venc_contrato = fields.Date(allow_none=True)
    indice = fields.Str(allow_none=True)
    forma_pag = fields.Str()
    agencia = fields.Str(allow_none=True)
    conta = fields.Str(allow_none=True)
    tipo_chave_pix = fields.Str(allow_none=True)
    chave_pix = fields.Str(allow_none=True)
    valor_multa = fields.Decimal(places=2, allow_none=True)
    percentual_multa = fields.Decimal(places=4, allow_none=True)
    obs1 = fields.Str(allow_none=True)
    obs2 = fields.Str(allow_none=True)
    datalanc = fields.Date(allow_none=True)
    userlanc = fields.Str(allow_none=True)
    cancelado = fields.Bool() 