
from db import Base,engine
from sqlalchemy import Column,String,Integer,Time,Text,Date,ForeignKey,Boolean,Numeric,DateTime
from sqlalchemy.orm import relationship


class Consumo(Base):
    __tablename__ = 'consumo'  
    id = Column(Integer, primary_key=True,autoincrement=True)
    cuenta = Column(Integer)
    idproducto = Column(Integer)
    idmedico = Column(Integer)
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