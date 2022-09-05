from db import Base,engine
from sqlalchemy import Column,String,Integer,Time,Boolean


class Especialidad(Base):
    __tablename__ = "especialidad"
    id = Column(Integer, primary_key=True,autoincrement=True)
    descripcion = Column(String)
    estado = Column(Boolean,default=True)


class Consultorio(Base):
    __tablename__ = "consultorio"
    id = Column(Integer, primary_key=True,autoincrement=True)
    descripcion = Column(String)
    estado = Column(Boolean,default=True)


class Turno(Base):
    __tablename__ = "turno"
    id = Column(Integer, primary_key=True,autoincrement=True)
    descripcion = Column(String)
    horainicio = Column(Time)
    horafin = Column(Time)
    horas = Column(Time)
    estado = Column(Boolean,default=True)


class Medico(Base):
    __tablename__ = "medico"
    id = Column(Integer, primary_key=True,autoincrement=True)
    idespecialidad = Column(Integer)
    nombres = Column(String)
    intervalo = Column(Time)
    estado = Column(Boolean,default=True)


class TipoDocumento(Base):
    __tablename__ = "tipodocumento"
    id = Column(Integer, primary_key=True,autoincrement=True)
    descripcion = Column(String)
    abreviado = Column(String)
    sunat = Column(Integer)

class Iafas(Base):
    __tablename__ = "iafas"
    id = Column(Integer, primary_key=True,autoincrement=True)
    descripcion = Column(String)
    codigoiafas = Column(Integer)
    estado = Column(Boolean,default=True)


class Servicio(Base):
    __tablename__ = "servicio"
    id = Column(Integer, primary_key=True,autoincrement=True)
    descripcion = Column(String)
    codigosunat = Column(Integer)


def create_table():
    Base.metadata.create_all(bind=engine)