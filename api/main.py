from fastapi import Depends, FastAPI,APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from datetime import date, time
from typing import Optional
#LIBRARY CONEXION sqlalchemy ORM
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session,relationship
#SQLALchemy TABLE
from sqlalchemy import Column,String,Integer,Time,Text,Date,ForeignKey


app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


''' CONEXION BD'''
DATABASE__URL = "postgresql://postgres:2009@localhost:5432/bd_isis"
engine = create_engine(DATABASE__URL)
sessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base  = declarative_base()

'''FUNCTION PARA GENERAR CONEXION'''
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

'''MAPEO DE TABLE'''
class Medicos(Base):
    __tablename__ = "medicos"
    id = Column(Integer, primary_key=True,autoincrement=True)

class Consultorios(Base):
    __tablename__ = "consultorios"
    id = Column(Integer, primary_key=True,autoincrement=True)

class Especialidades(Base):
    __tablename__ = "especialidades"
    id = Column(Integer, primary_key=True,autoincrement=True)
    descripcion = Column(String)

class Turnos(Base):
    __tablename__ = "turnos"
    id = Column(Integer, primary_key=True,autoincrement=True)


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

''''MODEL'''
class MedicosModel(BaseModel):
    id:int
    class Config:
        orm_mode = True

class ConsultoriosModel(BaseModel):
    id:int
    class Config:
        orm_mode = True

class EspecialidadesModel(BaseModel):
    id:int
    descripcion:str
    class Config:
        orm_mode = True

class TurnosModel(BaseModel):
    id:int
    class Config:
        orm_mode = True

class ProgramacionBase(BaseModel):
    id:Optional[int]
    idmedico:int
    idconsultorio:int
    idespecialidad:int
    idturno:int
    fecha:date
    estado:str
    cupos:int
    minutos:time
    observacion:str

''''    '''

class ProgramacionSchema(BaseModel):
    id:int
    fecha:date
    estado:str
    cupos:int
    minutos:time
    observacion:str
    especialidad:EspecialidadesModel = None 
    medico:MedicosModel = None 
    consultorio:ConsultoriosModel = None 
    turno:TurnosModel = None 

    class Config:
        orm_mode = True


'''FUNCTION PARA LA CREACION DE TABLE'''

def create_table():
    Base.metadata.create_all(bind=engine)
# create_table()


'''ROUTES'''
router = APIRouter(prefix='/programacion',tags=['programacion'])

@router.get('/listAll')
def list_programacion(db:Session = Depends(get_db)):
    return db.query(Programacion).all()

@router.get('/listById/{id}',response_model =ProgramacionSchema)
def get_programacion(id:int,db:Session = Depends(get_db)):

    data = db.query(Programacion).filter(Programacion.id==id).first()

    if data:
        return data
    return {"message":f'''No hay data con el id {id}'''}


@router.post('/create')
def create_programacion(programacion:ProgramacionBase,db:Session = Depends(get_db)):
    row_item = Programacion(**programacion.dict())
    db.add(row_item)
    db.commit()
    db.refresh(row_item)
    return row_item


@router.put('/update/{id}')
def update_programacion(id:int,programacionBase:ProgramacionBase,db:Session = Depends(get_db)):

    data = db.query(Programacion).filter(Programacion.id == id).first()

    if data :
        data.idmedico  = programacionBase.idmedico
        data.idconsultorio = programacionBase.idconsultorio
        data.idespecialidad = programacionBase.idespecialidad
        data.idturno = programacionBase.idturno
        data.fecha = programacionBase.fecha
        data.estado = programacionBase.estado
        data.cupos = programacionBase.cupos
        data.minutos = programacionBase.minutos
        data.observacion = programacionBase.observacion

        db.commit()
        db.refresh(data)
        return {"message":f''' Se actualizado'''}
    return {"message":f''' No hay data con el id {id}'''}


@router.delete('delete/{id}')
def delete_programacion(id:int,db:Session = Depends(get_db)):

    data = db.query(Programacion).filter(Programacion.id == id).first()
    if data:
        db.delete(data)
        db.commit()
        return {"message":f''' Se eleimino la programacion con el id {id} ''' }
    return {"message":f'''No exite programacion con el id {id}'''}

app.include_router(router)