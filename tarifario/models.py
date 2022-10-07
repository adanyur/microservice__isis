
from db import Base,engine
from sqlalchemy import Column,String,Integer,Time,Text,Date,ForeignKey,Boolean
from sqlalchemy.orm import relationship


class Tarifario(Base):
    __tablename__ = 'tarifario'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(3))
    subtitulo = Column(String(3))
    codigo = Column(String(6))
    descripcion = Column(String(500))
    descripcion = Column(String(250))
    grupocontable = Column(Integer)
    cpms = Column(String(10))
    estado = Column(Boolean)


class Tarifariodetalle(Base):
    __tablename__ = 'ta'
  