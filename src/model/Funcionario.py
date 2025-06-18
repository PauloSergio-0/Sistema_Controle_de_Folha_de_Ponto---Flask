from sqlalchemy import Column, Integer, String
from database.database import Base


class Funcionario(Base):
    __tablename__ = "funcionarios"
    
    id = Column(Integer, primary_key = True)
    nome = Column(String, nullable = False)
    cpf = Column(String, nullable = False)
    departamento = Column(String, nullable = False)
    status = Column(String, nullable = False)