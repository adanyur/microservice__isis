
from db import Base,engine
from sqlalchemy import Column,String,Integer,Time,Text,Date,ForeignKey,Boolean,Numeric
from sqlalchemy.orm import relationship


class Tarifario(Base):
    __tablename__ = 'tarifario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(3))
    subtitulo = Column(String(3))
    codigo = Column(String(6))
    descripcion = Column(String(500))
    unidad = Column(Numeric(10,2))
    grupocontable = Column(Integer)
    codigosunat = Column(String(8))
    cpms = Column(String(10))
    estado = Column(Boolean)


class Tarifariodetalle(Base):
    __tablename__ = 'ta'
  