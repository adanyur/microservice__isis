from typing import List

from db import get_db
from fastapi import APIRouter, Depends
from models import (Cie10, Consultorio, Especialidad, Iafas, Medico, Pais,
                    Servicio, TipoDocumento, Turno, create_table)
from schemas import (ConsultoriosBase, EspecialidadesBase, MedicosBase,
                     TurnosBase)
from sqlalchemy.orm import Session

router = APIRouter(prefix='/ficheros',tags=['Ficheros'])


@router.get('/createTable')
def creates_tables():
    create_table()
    return {"message":"CREATE TABLE"}


@router.get('/especialidades',response_model = List[EspecialidadesBase])
def especialidades(db:Session = Depends(get_db))->List[EspecialidadesBase]:
    return db.query(Especialidad).order_by(Especialidad.descripcion).all()


@router.get('/especialidades/{id}')
async def listById_especialidad(id:int,db:Session = Depends(get_db))->EspecialidadesBase:
    return db.query(Especialidad).filter(Especialidad.id == id).first()







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
    


async def lista_paises(db:Session):
 return db.query(Pais).order_by(Pais.descr).all()


@router.get('/paises')
async def listado_paises(db:Session = Depends(get_db)):
    return await lista_paises(db)


@router.get('/iafas')
async def listado_iafas(db:Session = Depends(get_db)):
    return db.query(Iafas).all()    



@router.get('/medicos',response_model = List[MedicosBase])
def medicos(db:Session = Depends(get_db))->List[MedicosBase]:
    return db.query(Medico).order_by(Medico.nombres).all()


@router.get('/medicos/{idespecialidad}',response_model =List[MedicosBase])
def get_medicos(idespecialidad:int,db:Session = Depends(get_db)):
    return db.query(Medico).filter(Medico.idespecialidad==idespecialidad).order_by(Medico.nombres).all()

