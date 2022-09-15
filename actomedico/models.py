from db import Base,engine
from sqlalchemy import Column,String,Integer,Time,Text,Date,ForeignKey,Boolean,Numeric
from sqlalchemy.orm import relationship



class Servicio(Base):
    __tablename__ = 'servicio'
    id = Column(Integer, primary_key=True)

class Admision(Base):
    __tablename__ = 'admision'
    id = Column(Integer, primary_key=True)


class Cie10(Base):
    __tablename__ = 'cie10'
    id = Column(Integer, primary_key=True)
    codigo = Column(String)
    descripcion = Column(String)
    estado = Column(Boolean)


class Antencedente(Base):
    __tablename__ = 'atencedente'
    id = Column(Integer, primary_key=True,autoincrement=True)
    idactomedico = Column(Integer, ForeignKey("actomedico.id"))
    idantecedente = Column(Integer)
    descripcion = Column(String)


class Diagnostico(Base):
    __tablename__='diagnostico'
    id = Column(Integer, primary_key=True,autoincrement=True)
    idactomedico = Column(Integer, ForeignKey("actomedico.id"))
    idcie10 = Column(Integer, ForeignKey("cie10.id"))
    tipodiagnostico = Column(Integer)
    cie10 = relationship("Cie10",backref="cie10")

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
    idadmision = Column(Integer, ForeignKey("admision.id"))
    motivoconsulta = Column(Text)
    enferproblemaactual = Column(Text)
    examenfisico = Column(Text)
    presionarterial = Column(Numeric(10,2))
    cardiaca = Column(Numeric(10,2))
    respiratoria = Column(Numeric(10,2))
    tempbucal = Column(Numeric(10,2))
    tempaxilar = Column(Numeric(10,2))
    peso = Column(Numeric(10,2))
    talla = Column(Numeric(10,2))
    masacorporal = Column(Numeric(10,2))
    perimcefalico = Column(Numeric(10,2))
    atencion = Column(Integer)
    antecedentes = relationship("Antencedente",backref="antecedentes")
    diagnosticos = relationship("Diagnostico",backref="diagnosticos")
    recetas = relationship("Receta",backref="recetas")
    

class Cita(Base):
    __tablename__ = 'cita'
    id = Column(Integer, primary_key=True)
    estado = Column(String)



def create_table():
    Base.metadata.create_all(bind=engine)