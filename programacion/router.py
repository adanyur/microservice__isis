from fastapi import Depends,APIRouter
from models import Programacion
from schemas import ProgramacionSchema,ProgramacionBase
from sqlalchemy.orm import Session
from db import get_db


router = APIRouter(prefix='/programacion',tags=['Programacion'])


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