from db import Base,engine
from sqlalchemy import Column,String,Integer,Time,Text,Date,ForeignKey,Boolean
from sqlalchemy.orm import relationship


class Medicos(Base):
    __tablename__ = "medicos"
    id = Column(Integer, primary_key=True,autoincrement=True)
    idespecialidad = Column(Integer)
    nombres = Column(String)
    intervalo = Column(Time)
    estado = Column(Boolean,default=True)


class Consultorios(Base):
    __tablename__ = "consultorios"
    id = Column(Integer, primary_key=True,autoincrement=True)
    descripcion = Column(String)
    estado = Column(Boolean,default=True)


class Especialidades(Base):
    __tablename__ = "especialidades"
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



class Programacion(Base):
    __tablename__ = "programacion"
    id = Column(Integer, primary_key=True,autoincrement=True)
    fecha = Column(Date)
    estado = Column(String)
    cupos =  Column(Integer)
    minutos = Column(Time)
    observacion = Column(Text)
    idmedico = Column(Integer, ForeignKey("medicos.id"))
    idconsultorio =  Column(Integer, ForeignKey("consultorios.id"))
    idespecialidad =  Column(Integer, ForeignKey("especialidades.id"))
    idturno = Column(Integer, ForeignKey("turnos.id"))
    medico = relationship("Medicos", backref="medico")
    consultorio =  relationship("Consultorios", backref="consultorio")
    especialidad =  relationship("Especialidades", backref="especialidad")
    turno = relationship("Turnos", backref="turno")




def create_table():
    Base.metadata.create_all(bind=engine)