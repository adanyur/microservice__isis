from db import Base,engine
from sqlalchemy import Column,String,Integer,Time,Text,Date,ForeignKey,Boolean
from sqlalchemy.orm import relationship,backref




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
    historia = relationship('Historia',back_populates="persona", uselist=False)


class Historia(Base):
    __tablename__ = 'historia'
    historia = Column(Integer, primary_key=True,autoincrement=True)
    historiaReferencia = Column(Integer)
    idpersona = Column(Integer, ForeignKey("persona.id"))
    persona = relationship("Persona", back_populates="historia")



def create_table():
    Base.metadata.create_all(bind=engine)