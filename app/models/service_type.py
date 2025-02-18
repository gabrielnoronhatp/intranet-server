from app import db
from datetime import datetime

class ServiceType(db.Model):
    __tablename__ = 'ctt_tipo_contrato'
    __table_args__ = {'schema': 'intra', 'extend_existing': True}

    id = db.Column('id', db.Integer, primary_key=True)
    descricao = db.Column('descricao', db.String(255), nullable=False)
    last_update = db.Column('last_update', db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relacionamento com Contract
    contracts = db.relationship('Contract', backref='service_type', lazy=True)

    @property
    def descricao_formatada(self):
        return f"{self.id}-{self.descricao.strip().lower()}"

    @property
    def descricao_simples(self):
        return self.descricao.strip().lower()

    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao_formatada,
            'last_update': self.last_update
        }

    def to_dict_with_id(self):
        return {
            'id': self.id,
            'descricao': self.descricao_formatada,
            'last_update': self.last_update
        }

    def __repr__(self):
        return f'<ServiceType {self.descricao_formatada}>' 