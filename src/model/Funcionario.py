from sqlalchemy import Column, Integer, String
from database.database import Base


class Funcionario(Base):
    __tablename__ = "funcionarios"
    
    id = Column(Integer, primary_key = True)
    nome = Column(String, nullable = False)
    