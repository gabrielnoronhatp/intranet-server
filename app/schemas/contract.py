from marshmallow import Schema, fields

class ContractSchema(Schema):
    id = fields.Int(dump_only=True)
    idtipo = fields.Str(required=True)
    idfilial = fields.Str(required=True)
    idfornecedor = fields.Str(required=True)
    dia_vencimento = fields.Str(required=True)
    valor_contrato = fields.Decimal(places=2)
    nome = fields.Str(required=True)
    telefone1 = fields.Str()
    telefone2 = fields.Str()
    endereco1 = fields.Str()
    endereco2 = fields.Str()
    email1 = fields.Str()
    email2 = fields.Str()
    data_venc_contrato = fields.Date()
    indice = fields.Str()
    forma_pag = fields.Str()
    agencia = fields.Str()
    conta = fields.Str()
    tipo_chave_pix = fields.Str()
    chave_pix = fields.Str()
    valor_multa = fields.Decimal(places=2)
    percentual_multa = fields.Decimal(places=4)
    obs1 = fields.Str()
    obs2 = fields.Str()
    datalanc = fields.Date()
    userlanc = fields.Str()
    cancelado = fields.Bool() 