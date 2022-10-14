from datetime import date, datetime, timedelta
from typing import List

from db import Base, engine, get_db
from fastapi import APIRouter, Depends, HTTPException
from modelBase import CreateCita, PlantillaHorariosBase
from models import Citas, Historia, Programacion
from schemas import (AdmisionCitasIn, AgendaMedicaIn, PlantillaHorariosIn,
                     updateCita)
from sqlalchemy.orm import Session

router = APIRouter(prefix='/citas',tags=['Citas'])


def create_table():
    Base.metadata.create_all(bind=engine)


@router.get('/createTable')
def creates_tables():
    create_table()
    return {"messages":"Se creo tablas"};

@router.get('/listAll')
def list_citas(db:Session = Depends(get_db)):
    return db.query(Citas).all();


@router.get('/liById/{id}')
def get_citas(id:int,db:Session = Depends(get_db)):
    citas_data = db.query(Citas).filter(Citas.id == id).first()
    if not citas_data:
        raise HTTPException(status_code=404,detail="Citas no existe")
    return citas_data

@router.post('/create')
def create_citas(CreateCita:CreateCita,db:Session = Depends(get_db)):
    row_item = Citas(**CreateCita.dict())
    db.add(row_item)
    db.commit()
    db.refresh(row_item)
    return row_item


@router.post('/cambioestado')
def update_citas(updateCita:updateCita,db:Session = Depends(get_db)):

    estadoCita = {
            "S":"SUSPENDIDO",
            "R":"RESERVADO"
    }

    db.query(Citas).filter(Citas.id == updateCita.idcita).update(dict({"estado":updateCita.estado}))
    db.commit()
    return {"message":f'''Se cambio estado de la cita a {estadoCita[updateCita.estado]}'''}



def citaFind(data,idprogramacion:int,orden:int):
    return next((item for item in data if item.idprogramacion == idprogramacion and item.orden == orden),None)


@router.post('/plantillaHorarios',response_model=List[PlantillaHorariosIn])
def list_plantillas_horarios(PlantillaHorariosBase:PlantillaHorariosBase,db:Session = Depends(get_db)):

    data = db.query(Citas).filter(Citas.idprogramacion == PlantillaHorariosBase.idprogramacion,Citas.estado != 'S').all()
    plantilla = []
    hora = datetime.strptime(str(PlantillaHorariosBase.horaInicio),'%H:%M:%S')
    for orden in range(PlantillaHorariosBase.cupos):
        hora+=timedelta(minutes=int(PlantillaHorariosBase.minutos.minute))      
        plantilla.append({
            "idprogramacion":PlantillaHorariosBase.idprogramacion,
            "orden":orden + 1,
            "fecha":PlantillaHorariosBase.fecha,
            "hora":hora.strftime('%H:%M:%S'),
            "cita": citaFind(data,PlantillaHorariosBase.idprogramacion,orden + 1)
        })
    return plantilla


@router.get('/agendamedica/{fecha}',response_model=List[AgendaMedicaIn])
def list_agendamedica(fecha:str = date.today() ,db:Session = Depends(get_db)) -> AgendaMedicaIn:
    return db.query(Programacion).filter(Programacion.fecha == fecha).all()



@router.get('/admisioncita/{id}',response_model=AdmisionCitasIn)
def first_paciente(id:int,db:Session = Depends(get_db)):
     return  db.query(Historia).filter(Historia.idpersona==id).first()

