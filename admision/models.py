import string
from db import Base,engine
from sqlalchemy import Column,String,Integer,Time,Text,Date,ForeignKey,Boolean


class Cita(Base):
    __tablename__ = 'cita'
    id = Column(Integer, primary_key=True)

# class Cobertura(Base):
#     __tablename__ = 'cobertura'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     codigocobertura = Column(Integer)
#     descripcion = Column(String)
#     estado = Column(Boolean)


# class SubCobertura(Base):
#     __tablename__ = 'subcobertura'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     idcobertura = Column(Integer,ForeignKey("cobertura.id"))
#     descripcion = Column(String)
#     estado = Column(Boolean)

 
class Admision(Base):
    __tablename__ = 'admision'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idcita = Column(Integer,ForeignKey('cita.id'))
    # idacreditacion = Column(Integer, ForeignKey('idacreditacion.id'))
    # idcobertura = Column(Integer,ForeignKey('cobertura.id'))
    idacreditacion = Column(Integer)
    idcobertura = Column(Integer)
    idatencion = Column(Integer)
    idtipocuenta = Column(Integer)
    copagofijo = Column(Integer)
    copagovariable = Column(Integer)
    numeroautorizacion = Column(String)
    fincarencia = Column(String)
    observacion = Column(Text)
    estado = Column(Boolean)

      
# class Acreditacion(Base):
#     __tablename__ = 'acreditacion'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     idhistoria = Column(Integer,ForeignKey('historia.id'))
#     idproducto = Column(Integer, ForeignKey('producto.id'))
#     iafas = Column(Integer, ForeignKey('iafas.id'))
#     idparentesco = Column(Integer, ForeignKey('parentesco.id'))
#     codigoafiliado = Column(Integer)
#     documento = Column(String)
#     estado = Column(String)
    


# class CondicionesMedicas(Base):
#     __tablename__ = 'condicionesmedica'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     idacreditacion = Column(Integer,ForeignKey('acreditacion.id'))


def create_table():
    Base.metadata.create_all(bind=engine)