from db import Base, engine
from sqlalchemy import (Boolean, Column, Date, ForeignKey, Integer, String,
                        Text, Time)
from sqlalchemy.orm import backref, relationship
from sqlalchemy.types import UserDefinedType


class TsVector(UserDefinedType):
    search = "TSVECTOR"
    cache_ok = True
    def get_col_spec(self):
        return self.search


class Persona(Base):
    __tablename__ = "persona"
    id = Column(Integer, primary_key=True,autoincrement=True)
    paterno = Column(String)
    materno = Column(String)
    nombres = Column(String)
    tipodocumento = Column(Integer)
    documento =  Column(String)
    fechanacimiento = Column(Date)
    genero = Column(Integer)
    estado = Column(Boolean)
    search = Column(TsVector)
    historia = relationship('Historia',back_populates="persona", uselist=False)


class Historia(Base):
    __tablename__ = 'historia'
    historia = Column(Integer, primary_key=True,autoincrement=True)
    historiaReferencia = Column(Integer)
    idpersona = Column(Integer, ForeignKey("persona.id"))
    persona = relationship("Persona", back_populates="historia")



def create_table():
    Base.metadata.create_all(bind=engine)