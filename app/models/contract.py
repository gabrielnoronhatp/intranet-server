from datetime import datetime
from app import db
from sqlalchemy import text

class Contract(db.Model):
    __tablename__ = 'ctt_contratos'
    __table_args__ = {'schema': 'intra'}

    id = db.Column(db.Integer, primary_key=True)
    idtipo = db.Column(db.String(10), db.ForeignKey('intra.ctt_tipo_contrato.id'))
    idfilial = db.Column(db.String(100))
    dia_vencimento = db.Column(db.String(2))
    idfornecedor = db.Column(db.String(10))
    valor_contrato = db.Column(db.Numeric(14, 2))
    nome = db.Column(db.String(200))
    telefone1 = db.Column(db.String(20))
    telefone2 = db.Column(db.String(20))
    endereco1 = db.Column(db.String(200))
    endereco2 = db.Column(db.String(300))
    email1 = db.Column(db.String(100))
    email2 = db.Column(db.String(100))
    data_venc_contrato = db.Column(db.Date)
    indice = db.Column(db.String(10))
    forma_pag = db.Column(db.String(20))
    agencia = db.Column(db.String(40))
    conta = db.Column(db.String(40))
    tipo_chave_pix = db.Column(db.String(40))
    chave_pix = db.Column(db.String(100))
    valor_multa = db.Column(db.Numeric(14, 2))
    percentual_multa = db.Column(db.Numeric(14, 4))
    obs1 = db.Column(db.Text)
    obs2 = db.Column(db.Text)
    datalanc = db.Column(db.Date, default=datetime.utcnow)
    userlanc = db.Column(db.String(100))
    cancelado = db.Column(db.Boolean, default=False)

    def to_dict(self):
        service_type = self.service_type
        service_type_desc = service_type.descricao_formatada if service_type else None
        
        return {
            'id': self.id,
            'idtipo': self.idtipo,
            'dia_vencimento': self.dia_vencimento,
            'tipo_servico': service_type_desc,
            'idfilial': self.idfilial,
            'idfornecedor': self.idfornecedor,
            'valor_contrato': float(self.valor_contrato) if self.valor_contrato else None,
            'nome': self.nome,
            'telefone1': self.telefone1,
            'telefone2': self.telefone2,
            'endereco1': self.endereco1,
            'endereco2': self.endereco2,
            'email1': self.email1,
            'email2': self.email2,
            'data_venc_contrato': self.data_venc_contrato,
            'indice': self.indice,
            'forma_pag': self.forma_pag,
            'agencia': self.agencia,
            'conta': self.conta,
            'tipo_chave_pix': self.tipo_chave_pix,
            'chave_pix': self.chave_pix,
            'valor_multa': float(self.valor_multa) if self.valor_multa else None,
            'percentual_multa': float(self.percentual_multa) if self.percentual_multa else None,
            'obs1': self.obs1,
            'obs2': self.obs2,
            'datalanc': self.datalanc,
            'userlanc': self.userlanc,
            'cancelado': self.cancelado
        }

    def __repr__(self):
        return f'<Contract {self.id}>' 