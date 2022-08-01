from db import Base,engine
from sqlalchemy import Column,String,Integer,Time,Text,Date,ForeignKey,Boolean


class Especialidad(Base):
    __tablename__ = "especialidades"
    id = Column(Integer, primary_key=True,autoincrement=True)
    descripcion = Column(String)
    estado = Column(Boolean,default=True)


class Consultorios(Base):
    __tablename__ = "consultorios"
    id = Column(Integer, primary_key=True,autoincrement=True)
    descripcion = Column(String)
    estado = Column(Boolean,default=True)


class Turnos(Base):
    __tablename__ = "turnos"
    id = Column(Integer, primary_key=True,autoincrement=True)
    descripcion = Column(String)
    horainicio = Column(Time)
    horafin = Column(Time)
    horas = Column(Time)
    estado = Column(Boolean,default=True)


class Medicos(Base):
    __tablename__ = "medicos"
    id = Column(Integer, primary_key=True,autoincrement=True)
    idespecialidad = Column(Integer)
    nombres = Column(String)
    intervalo = Column(Time)
    estado = Column(Boolean,default=True)