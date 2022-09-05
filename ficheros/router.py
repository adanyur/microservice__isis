from fastapi import Depends,APIRouter
from models import Medico,Consultorio,Especialidad,Turno,create_table,TipoDocumento,Servicio
from schemas import MedicosBase,EspecialidadesBase,TurnosBase,ConsultoriosBase
from typing import List
from sqlalchemy.orm import Session
from db import get_db


router = APIRouter(prefix='/ficheros',tags=['Ficheros'])


@router.get('/createTable')
def creates_tables():
    create_table()
    return {"message":"CREATE TABLE"}


@router.get('/especialidades',response_model =List[EspecialidadesBase])
def especialidades(db:Session = Depends(get_db)):
    return db.query(Especialidad).all()



@router.get('/medicos',response_model =List[MedicosBase])
def medicos(db:Session = Depends(get_db)):
    return db.query(Medico).all()


@router.get('/medicos/{idespecialidad}',response_model =List[MedicosBase])
def get_medicos(idespecialidad:int,db:Session = Depends(get_db)):
    return db.query(Medico).filter(Medico.idespecialidad==idespecialidad).all()


@router.get('/turnos',response_model =List[TurnosBase])
def turnos(db:Session = Depends(get_db)):
    return db.query(Turno).all()


@router.get('/consultorios',response_model =List[ConsultoriosBase])
def consultorios(db:Session = Depends(get_db)):
    return db.query(Consultorio).all()


@router.get('/tipodocumentos')
def tipoDocumento(db:Session = Depends(get_db)):
    return db.query(TipoDocumento).all()


@router.get('/servicio')
def servicio(db:Session = Depends(get_db)):
    return db.query(Servicio).all()