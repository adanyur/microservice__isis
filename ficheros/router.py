from fastapi import Depends,APIRouter, HTTPException
from models import Medicos,Consultorios,Especialidad,Turnos
from schemas import MedicosBase,EspecialidadesBase,TurnosBase,ConsultoriosBase
from typing import List
from sqlalchemy.orm import Session
from db import get_db



router = APIRouter(prefix='/ficheros',tags=['Ficheros'])



@router.get('/especialidades',response_model =List[EspecialidadesBase])
def especialidades(db:Session = Depends(get_db)):
    return db.query(Especialidad).all()

@router.get('/medicos',response_model =List[MedicosBase])
def medicos(db:Session = Depends(get_db)):
    return db.query(Medicos).all()

@router.get('/medicos/{idespecialidad}',response_model =List[MedicosBase])
def get_medicos(idespecialidad:int,db:Session = Depends(get_db)):
    return db.query(Medicos).filter(Medicos.idespecialidad==idespecialidad).all()


@router.get('/turnos',response_model =List[TurnosBase])
def turnos(db:Session = Depends(get_db)):
    return db.query(Turnos).all()


@router.get('/consultorios',response_model =List[ConsultoriosBase])
def consultorios(db:Session = Depends(get_db)):
    return db.query(Consultorios).all()