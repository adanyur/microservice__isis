from fastapi import Depends,APIRouter
from models import Medico,Consultorio,Especialidad,Turno,create_table,TipoDocumento,Servicio,Cie10
from schemas import MedicosBase,EspecialidadesBase,TurnosBase,ConsultoriosBase
from typing import List
from sqlalchemy.orm import Session
from db import get_db


router = APIRouter(prefix='/ficheros',tags=['Ficheros'])


@router.get('/createTable')
def creates_tables():
    create_table()
    return {"message":"CREATE TABLE"}


@router.get('/especialidades',response_model = List[EspecialidadesBase])
def especialidades(db:Session = Depends(get_db))->List[EspecialidadesBase]:
    return db.query(Especialidad).order_by(Especialidad.descripcion).all()



@router.get('/medicos',response_model = List[MedicosBase])
def medicos(db:Session = Depends(get_db))->List[MedicosBase]:
    return db.query(Medico).order_by(Medico.nombres).all()


@router.get('/medicos/{idespecialidad}',response_model =List[MedicosBase])
def get_medicos(idespecialidad:int,db:Session = Depends(get_db)):
    return db.query(Medico).filter(Medico.idespecialidad==idespecialidad).order_by(Medico.nombres).all()


@router.get('/turnos',response_model = List[TurnosBase])
def turnos(db:Session = Depends(get_db))->List[TurnosBase]:
    return db.query(Turno).all()


@router.get('/consultorios',response_model = List[ConsultoriosBase])
def consultorios(db:Session = Depends(get_db))->List[ConsultoriosBase]:
    return db.query(Consultorio).all()


@router.get('/tipodocumentos')
def tipoDocumento(db:Session = Depends(get_db)):
    return db.query(TipoDocumento).all()


@router.get('/servicio')
def servicio(db:Session = Depends(get_db)):
    return db.query(Servicio).all()

@router.get('/cie10')
def cie10(search:str,db:Session = Depends(get_db)):
    return db.query(Cie10).filter(Cie10.estado == True, Cie10.codigo.like(f'''{search}%''') | Cie10.descripcion.like(f'''{search}%''')).order_by(Cie10.descripcion).all();
    


