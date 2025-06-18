from sqlalchemy import Integer, String, Date, Time, ForeignKey, Column
from sqlalchemy.orm import relationship
from database.database import Base

class RegistroPonto(Base):
    
    __tablename__= 'registro_ponto'
    
    id = Column(Integer, primary_key=True)
    id_funcionario = Column(Integer, ForeignKey('funcioanrio.id'))
    nome = Column(String, nullable = False)
    cpf = Column(String, nullable = False)
    data = Column(Date, nullable=False)
    hora_entrada = Column(Time, nullable=False)
    hora_saida = Column(Time, nullable=False)
    
    funcionario = relationship('funcionarios', back_populates='registro_ponto')