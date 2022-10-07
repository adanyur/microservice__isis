
from db import Base,engine
from sqlalchemy import Column,String,Integer,Time,Text,Date,ForeignKey,Boolean,Numeric
from sqlalchemy.orm import relationship





class Consumo(Base):
    __tablename__ = 'consumo'  
    id = Column(Integer, primary_key=True,autoincrement=True)
    cuenta = Column(Integer,ForeignKey("admision.id"))
    precio = Column(Numeric(10,2))
    
    idmedico = Column(Integer,ForeignKey("medico.id"))
    estado = Column(String(1))

    