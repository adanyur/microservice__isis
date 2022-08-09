from db import Base,engine
from sqlalchemy import Column,String,Integer,Time,Text,Date,ForeignKey,Boolean
from sqlalchemy.orm import relationship


class Persona(Base):
    __tablename__ = "persona"
    id = Column(Integer, primary_key=True,autoincrement=True)
    paterno = Column(String)
    materno = Column(String)
    nombres = Column(String)
    tipoDocumento = Column(Integer)
    documento =  Column(String)
    fechaNacimiento = Column(Date)
    genero = Column(Integer)
    estado = Column(Boolean)

class Historia(Base):
    __tablename__ = 'historia'
    historia = Column(Integer, primary_key=True)
    idpersona = Column(Integer,ForeignKey('persona.id'))
    persona = relationship("Persona", backref="persona")

class Programacion(Base):
    __tablename__ = 'programacion'
    id = Column(Integer, primary_key=True, autoincrement=True)

class Citas(Base):
    __tablename__ = 'citas'
    id = Column(Integer, primary_key=True,autoincrement=True)
    idprogramacion = Column(Integer,ForeignKey("programacion.id"))
    historia = Column(Integer,ForeignKey("historia.historia"))
    orden = Column(Integer)
    fecha = Column(Date)
    hora = Column(Time)
    observacion = Column(Text)
    estado = Column(String)
    paciente = relationship("Historia", backref="paciente")

