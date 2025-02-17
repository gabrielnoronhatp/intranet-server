from datetime import datetime
from app import db
from sqlalchemy import text

class Contract(db.Model):
    __tablename__ = 'ctt_contratos'
    __table_args__ = {'schema': 'intra'}

    id = db.Column(db.Integer, primary_key=True)
    idtipo = db.Column(db.Integer)
    idfilial = db.Column(db.Integer)
    idfornecedor = db.Column(db.Integer)
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

    def __repr__(self):
        return f'<Contract {self.id}>' 