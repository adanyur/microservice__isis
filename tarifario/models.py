
from db import Base, engine
from sqlalchemy import (Boolean, Column, Date, ForeignKey, Integer, Numeric,
                        String, Text, Time)
from sqlalchemy.orm import relationship


class TarifarioGrupo(Base):
    __tablename__ = 'tarifariogrupo'
    codigo = Column(Integer,primary_key=True)
    descripcion = Column(String,nullable=False)



class TarifarioTitulo(Base):
    __tablename__ = 'tarifariotitulo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(3))
    descripcion = Column(String(255))
    grupocontable = Column(Integer)
    estado = Column(Boolean)


class TarifarioSubtitulo(Base):
    __tablename__ = 'tarifariosubtitulo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(4))
    descripcion = Column(String(255))
    idtarifariotitulo = Column(Integer, ForeignKey("tarifariotitulo.id"))
    estado = Column(Boolean)

    
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

    
class TarifarioDetalle(Base):
    __tablename__ = 'tarifariodetalle'
    id = Column(Integer, primary_key=True,autoincrement=True)
    idtarifario = Column(Integer, ForeignKey("tarifario.id"))
    idiafas = Column(Integer)
    precio = Column(Numeric(10,2))


def create_table():
    Base.metadata.create_all(bind=engine)