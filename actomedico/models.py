from db import Base,engine
from sqlalchemy import Column,String,Integer,Time,Text,Date,ForeignKey,Boolean
from sqlalchemy.orm import relationship



class Servicio(Base):
    __tablename__ = 'servicio'
    id = Column(Integer, primary_key=True)

class Admision(Base):
    __tablename__ = 'admision'
    id = Column(Integer, primary_key=True)


class Antencedente(Base):
    __tablename__ = 'atencedente'
    id = Column(Integer, primary_key=True,autoincrement=True)
    idactomedico = Column(Integer, ForeignKey("actomedico.id"))
    idantecedente = Column(String)
    descripcion = Column(String)


class Diagnostico(Base):
    __tablename__='diagnostico'
    id = Column(Integer, primary_key=True,autoincrement=True)
    idactomedico = Column(Integer, ForeignKey("actomedico.id"))
    idciex = Column(String)
    tipodiagnostico = Column(Integer)


class Receta(Base):
    __tablename__ = 'receta'
    id = Column(Integer, primary_key=True,autoincrement=True)
    idactomedico = Column(Integer, ForeignKey("actomedico.id"))
    idservicio = Column(Integer, ForeignKey("servicio.id"))
    idproducto = Column(Integer)
    cantidad = Column(Integer)
    indicacion = Column(String)
    estado = Column(String)


class Actomedico(Base):
    __tablename__ = 'actomedico'
    id = Column(Integer, primary_key=True,autoincrement=True)
    idadminsion = Column(Integer, ForeignKey("admision.id"))
    motivoconsulta = Column(Text)
    enferproblemaactual = Column(Text)
    examenfisico = Column(Text)
    presionarterial = Column(Integer)
    cardiaca = Column(Integer)
    respiratoria = Column(Integer)
    tempbucal = Column(Integer)
    tempaxilar = Column(Integer)
    peso = Column(Integer)
    talla = Column(Integer)
    masacorporal = Column(Integer)
    perimcefalico = Column(Integer)
    atencion = Column(Integer)
    antecedentes = relationship("Antencedente",backref="antecedentes")
    diagnosticos = relationship("Diagnostico",backref="diagnosticos")
    recetas = relationship("Receta",backref="recetas")
    


def create_table():
    Base.metadata.create_all(bind=engine)