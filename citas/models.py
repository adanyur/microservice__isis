from email.policy import default
from db import Base,engine
from sqlalchemy import Column,String,Integer,Time,Text,Date,ForeignKey, column
from sqlalchemy.orm import relationship

class Programacion(Base):
    __tablename__ = 'programacion'
    id = Column(Integer, primary_key=True)


class Citas(Base):
    __tablename__ = 'citas'
    id = Column(Integer, primary_key=True,autoincrement=True)
    idprogramacion = Column(Integer,ForeignKey("programacion.id"))
    historia = Column(Integer)
    orden = Column(Integer)
    fecha = Column(Date)
    hora = Column(Time)
    observacion = Column(Text)
    estado = Column(String)

