from db import Base,engine
from sqlalchemy import Column,String,Integer,Time,Boolean
from sqlalchemy.types import UserDefinedType

class TsVector(UserDefinedType):
    
    search = "TSVECTOR"
    cache_ok = True
    def get_col_spec(self):
        return self.search


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

class Servicio(Base):
    __tablename__ = "servicio"
    id = Column(Integer, primary_key=True,autoincrement=True)
    descripcion = Column(String)
    codigosunat = Column(Integer)



class Cobertura(Base):
    __tablename__ = "cobertura"
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String)
    subcobertura = Column(String)
    descripcion = Column(String)
    estado = Column(Boolean)
    

class ProductoIafas(Base):
    __tablename__ = "productoiafas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    iafas = Column(String)
    codigo = Column(String)
    descripcion = Column(String)
    iafasconcida = Column(String)
    estado = Column(Boolean)


class Cie10(Base):
    __tablename__ = "cie10"
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String)
    descripcion = Column(String)
    estado = Column(Boolean)
    search = Column(TsVector)


class GrupoCie10(Base):
    __tablename__ = "grupocie10"
    id = Column(Integer, primary_key=True,autoincrement=True)
    grupo = Column(String)
    descripcion = Column(String)
    estado = Column(Boolean)



class Pais(Base):
    __tablename__ = "pais"
    id = Column(Integer, primary_key=True, autoincrement=True)
    descr = Column(String(50))
    nacionalidad = Column(String(50))
    cod_sunat = Column(Integer)
    iso3166_n = Column(String(3))
    iso3166_ch2 = Column(String(2))
    iso3166_ch3 = Column(String(3))
    activo = Column(Boolean)



# class Departamento(Base):
#     __tablename__ = "departamento"
    


class Iafas(Base):
    __tablename__ = "iafas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(5))
    descripcion = Column(String(50))
    ruc = Column(String(11))
    siteds = Column(Boolean)


def create_table():
    Base.metadata.create_all(bind=engine)