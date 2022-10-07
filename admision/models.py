from db import Base,engine
from sqlalchemy import Column,String,Integer,Time,Text,Date,ForeignKey,Boolean,Numeric


class Cita(Base):
    __tablename__ = 'cita'
    id = Column(Integer, primary_key=True)

class Cobertura(Base):
    __tablename__ = 'cobertura'
    id = Column(Integer, primary_key=True)


class Admision(Base):
    __tablename__ = 'admision'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idcita = Column(Integer,ForeignKey('cita.id'))
    idiafas = Column(Integer, ForeignKey('iafas.id'))
    idcobertura = Column(Integer,ForeignKey('cobertura.id'))
    acreditacion = Column(Text)
    condicionmedica = Column(Text)
    copagofijo = Column(Integer)
    copagovariable = Column(Integer)
    numeroautorizacion = Column(String)
    fincarencia = Column(String)
    observacion = Column(Text,nullable=True)
    tipoadmision = Column(String(1))
    moneda = Column(Integer)
    tipocambio = Column(Numeric(10,2))
    estado = Column(String(1))


class Consumo(Base):
    __tablename__ = 'consumo'
    id = Column(Integer, primary_key=True,autoincrement=True)





def create_table():
    Base.metadata.create_all(bind=engine)