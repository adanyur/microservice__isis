from fastapi import Depends,APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import distinct
from models import Programacion,create_table
from schemas import ProgramacionSchema,ProgramacionBase,ProgramacionEspecialidadesEsquema,ProgramacionParameters,UpdateProgramacion
from base import *
from typing import List
from sqlalchemy.orm import Session
from utils import calcularCupo
from db import get_db


router = APIRouter(prefix='/programacion',tags=['Programacion'])


@router.get('/createTables')
def creates_tables():
    create_table()
    return {"message": "create tables"}

@router.get('/listAll',response_model =List[ProgramacionSchema])
def list_programacion(db:Session = Depends(get_db)):
    return db.query(Programacion).all()


@router.get('/listById/{id}',response_model =ProgramacionSchema)
def get_programacion(id:int,db:Session = Depends(get_db)):
    data = db.query(Programacion).filter(Programacion.id==id).first()
    if not data:
        raise HTTPException(status_code=404, detail='No hay data')
    return data


@router.get('/listByFecha/{fecha}',response_model =List[ProgramacionSchema])
def get_fecha_programacion(fecha:str,db:Session = Depends(get_db)):
    programacion_data =  db.query(Programacion).filter(Programacion.fecha==fecha).all()    
    # if not programacion_data:
    #     raise   HTTPException(status_code=404, detail=f'''No se encontro programaciones con fecha {fecha}''')
    return programacion_data


@router.get('/listEspecialidades/{fecha}',response_model=List[ProgramacionEspecialidadesEsquema])
def get_fecha_especialidad_programacion(fecha:str,db:Session = Depends(get_db)):

    especialidad_data = db.query(Programacion).distinct(Programacion.idespecialidad).filter(Programacion.fecha==fecha).all()

    # if not especialidad_data:
    #     raise   HTTPException(status_code=404, detail=f'''No hay programacion para hoy {fecha}''')
    return especialidad_data


@router.post('/listMedicos',response_model=List[ProgramacionSchema])
def get_fecha_medico_programacion(ProgramacionParameters:ProgramacionParameters,db:Session = Depends(get_db)):
    return  db.query(Programacion).filter(Programacion.fecha==ProgramacionParameters.fecha , Programacion.idespecialidad==ProgramacionParameters.especialidad).all()


@router.post('/create')
def create_programacion(programacion:ProgramacionIn, db:Session = Depends(get_db)):

    programacionData = programacion.dict(exclude={'medico','turno'})
    programacionData['idmedico'] = programacion.medico.id
    programacionData['idturno'] = programacion.turno.id
    programacionData['minutos'] = programacion.medico.intervalo
    programacionData['cupos'] = calcularCupo(programacion)

    row_item = Programacion(**programacionData)
    db.add(row_item)
    db.commit()
    db.refresh(row_item)
    
    return {"message":f''' Se genero la programacion'''}


@router.put('/update/{id}')
def update_programacion(id:int,programacionBase:ProgramacionBase,db:Session = Depends(get_db)):
    data = db.query(Programacion).filter(Programacion.id == id).first()
    if not data:
        raise HTTPException(status_code=404, detail='Programacion no existe')

    for key,value in programacionBase.dict(exclude_unset=True).items():
        setattr(data,key,value)
        
    db.add(data)
    db.commit()
    db.refresh(data)
    return {"message":f''' Se actualizado'''}

@router.post('/cambioestado')
def cambioestado_programacion(UpdateProgramacion:UpdateProgramacion,db:Session = Depends(get_db)):
    db.query(Programacion).filter(Programacion.id == UpdateProgramacion.idprogramacion).update(dict({"estado":UpdateProgramacion.estado}))
    db.commit()
    return {"message":f''' Se cambio de estado'''}



@router.delete('delete/{id}')
def delete_programacion(id:int,db:Session = Depends(get_db)):
    data = db.query(Programacion).filter(Programacion.id == id).first()
    if not data:
        raise HTTPException(status_code=404, detail='No existe programacion')
    db.delete(data)
    db.commit()
    return {"message":f''' Se eleimino la programacion con el id {id} ''' }