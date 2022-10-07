from db import Base
from sqlalchemy import Column,String,Integer,Time,Text,Date,ForeignKey,Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.orm import relationship
from datetime import date



class Medico(Base):
    __tablename__ = "medico"
    id = Column(Integer, primary_key=True)
    nombres = Column(String)

class Especialidad(Base):
    __tablename__ = "especialidad"
    id = Column(Integer, primary_key=True)
    descripcion = Column(String)

class Consultorio(Base):
    __tablename__ = "consultorio"
    id = Column(Integer, primary_key=True)
    descripcion = Column(String)

class Turno(Base):
    __tablename__ = "turno"
    id = Column(Integer, primary_key=True)
    descripcion = Column(String)  


class Cobertura(Base):
    __tablename__ = "cobertura"
    id = Column(Integer, primary_key=True)
    codigo = Column(String)
    subcobertura = Column(String)
    descripcion = Column(String)


class Persona(Base):
    __tablename__ = "persona"
    id = Column(Integer, primary_key=True)
    paterno = Column(String)
    materno = Column(String)
    nombres = Column(String)
    tipodocumento = Column(Integer)
    documento =  Column(String)
    fechanacimiento = Column(Date)
    genero = Column(Integer)
    estado = Column(Boolean)


class Programacion(Base):
    __tablename__ = 'programacion'
    id = Column(Integer, primary_key=True)
    fecha = Column(Date)
    cupos = Column(Integer)
    minutos = Column(Time)
    observacion = Column(Text)
    estado = Column(String)
    idmedico = Column(Integer,ForeignKey('medico.id'))
    idconsultorio = Column(Integer,ForeignKey('consultorio.id'))
    idespecialidad = Column(Integer,ForeignKey('especialidad.id'))
    idturno = Column(Integer,ForeignKey('turno.id'))
    medico = relationship("Medico", backref="medico")
    consultorio = relationship("Consultorio", backref="consultorio")
    especialidad = relationship("Especialidad", backref="especialidad")
    turno = relationship("Turno", backref="turno")
    citas = relationship("Citas", backref="citas")


class Actomedico(Base):
    __tablename__="actomedico"
    id = Column(Integer,primary_key=True)
    idadmision = Column(Integer, ForeignKey('admision.id'))


class Admision(Base):
    __tablename__='admision'
    id = Column(Integer,primary_key=True)
    acreditacion = Column(Text)
    idcobertura = Column(Integer,ForeignKey('cobertura.id'))
    idcita = Column(Integer, ForeignKey('cita.id'))
    copagofijo = Column(String)
    copagovariable = Column(String)
    numeroautorizacion = Column(String)
    fincarencia = Column(String)
    actomedico = relationship('Actomedico', backref='actomedico',uselist=False)
    cobertura = relationship('Cobertura', backref='cobertura',uselist=False)


class Citas(Base):
    __tablename__ = 'cita'
    id = Column(Integer, primary_key=True, autoincrement=True)
    idprogramacion = Column(Integer,ForeignKey("programacion.id"))
    historia = Column(Integer,ForeignKey("historia.historia"))
    orden = Column(Integer)
    fecha = Column(Date)
    hora = Column(Time)
    observacion = Column(Text)
    estado = Column(String)
    paciente = relationship("Historia", backref="paciente")
    programacion = relationship("Programacion", backref="programacion")
    admision = relationship("Admision", backref="admision",uselist=False)


class Historia(Base):
    __tablename__ = 'historia'
    historia = Column(Integer, primary_key=True)
    idpersona = Column(Integer,ForeignKey('persona.id'))
    persona = relationship("Persona", backref="persona")
    cita = relationship("Citas",primaryjoin=f'''and_(Historia.historia==Citas.historia,Citas.estado=='R',Citas.fecha=='{date.today()}')''',uselist=False)
    
    
       





    