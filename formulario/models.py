from db import Base,engine
from sqlalchemy import Column,String,Integer,Time,Text,Date,ForeignKey,Boolean
from sqlalchemy.orm import relationship,backref
from sqlalchemy.types import UserDefinedType


class Formulario(Base):
    __tablename__ = 'formulario'
    id = Column(Integer, primary_key=True,autoincrement=True)
    descripcion = Column(String(250), nullable=False)
    estado = Column(Boolean, default=True)
    campos = relationship('Campos',back_populates="formulario")


class Campos(Base):
    __tablename__ = 'campos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idformulario =  Column(Integer, ForeignKey('formulario.id'))
    label = Column(String(255), nullable=False)
    controltype = Column(String(250), nullable=False)
    type = Column(String(250), nullable=False)
    order = Column(Integer, nullable=False)
    value = Column(String(250), nullable=True)
    formulario = relationship('Formulario',back_populates="campos")
    




def create_table():
    Base.metadata.create_all(bind=engine)