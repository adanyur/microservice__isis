from db import Base,engine
from sqlalchemy import Column,String,Integer,Time,Text,Date,ForeignKey,Boolean
from sqlalchemy.orm import relationship


class Medico(Base):
    __tablename__ = "medico"
    id = Column(Integer, primary_key=True,autoincrement=True)
    idespecialidad = Column(Integer)
    nombres = Column(String)
    intervalo = Column(Time)
    estado = Column(Boolean,default=True)


class Consultorio(Base):
    __tablename__ = "consultorio"
    id = Column(Integer, primary_key=True,autoincrement=True)
    descripcion = Column(String)
    estado = Column(Boolean,default=True)


class Especialidad(Base):
    __tablename__ = "especialidad"
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



class Programacion(Base):
    __tablename__ = "programacion"
    id = Column(Integer, primary_key=True,autoincrement=True)
    fecha = Column(Date)
    estado = Column(String)
    cupos =  Column(Integer)
    minutos = Column(Time)
    observacion = Column(Text)
    idmedico = Column(Integer, ForeignKey("medico.id"))
    idconsultorio =  Column(Integer, ForeignKey("consultorio.id"))
    idespecialidad =  Column(Integer, ForeignKey("especialidad.id"))
    idturno = Column(Integer, ForeignKey("turno.id"))
    medico = relationship("Medico", backref="medico")
    consultorio =  relationship("Consultorio", backref="consultorio")
    especialidad =  relationship("Especialidad", backref="especialidad")
    turno = relationship("Turno", backref="turno")



def create_table():
    Base.metadata.create_all(bind=engine)