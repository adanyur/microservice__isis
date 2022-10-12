from db import Base,engine
from sqlalchemy import Column,String,Integer,Time,Text,Date,ForeignKey,Boolean,Numeric,DateTime


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
    # idiafas = Column(Integer, ForeignKey('iafas.id'))
    idcobertura = Column(Integer,ForeignKey('cobertura.id'))
    acreditacion = Column(Text)
    condicionmedica = Column(Text)
    copagofijo = Column(Integer)
    copagovariable = Column(Integer)
    numeroautorizacion = Column(String)
    fincarencia = Column(String)
    observacion = Column(Text,nullable=True)
    # tipoadmision = Column(String(1))
    # moneda = Column(Integer)
    # tipocambio = Column(Numeric(10,2))
    estado = Column(String(1))


class Consumo(Base):
    __tablename__ = 'consumo'  
    id = Column(Integer, primary_key=True,autoincrement=True)
    cuenta = Column(Integer,ForeignKey("admision.id"))
    idproducto = Column(Integer)
    idmedico = Column(Integer,ForeignKey("medico.id"))
    cantidad = Column(Numeric(10,2))
    precio = Column(Numeric(10,2))
    descuento  = Column(Numeric(10,2))
    subtotal = Column(Numeric(10,2))
    venta = Column(Numeric(10,2))
    igv = Column(Numeric(10,2))
    total = Column(Numeric(10,2))
    ventaseguro = Column(Numeric(10,2))
    igvseguro = Column(Numeric(10,2))
    totalseguro = Column(Numeric(10,2))
    fechaejecucion  = Column(DateTime)
    estado = Column(String(1))








def create_table():
    Base.metadata.create_all(bind=engine)