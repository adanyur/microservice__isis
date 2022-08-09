from fastapi import Depends,APIRouter, HTTPException
from models import Historia,Persona,create_table
from schemas import HistoriaSquema,HistoriaBase,ShowPersona
from typing import List
from sqlalchemy.orm import Session
from db import get_db

router = APIRouter(prefix='/historia',tags=['Historia'])

@router.get('/createTable')
def creates_tables():
    create_table()    
    return;

@router.get('/listById/{id}',response_model=HistoriaSquema)
def get_historia(id:int,db:Session = Depends(get_db)):
    return db.query(Historia).filter(Historia.idpersona == id).first()


@router.get('/autocomplete/{search}',response_model=list[ShowPersona])
def get_like_paciente(search:str,db:Session = Depends(get_db)):

    return db.query(Persona).filter(
        Persona.paterno.like(f'''%{search}%''')|
        Persona.materno.like(f'''%{search}%''')|
        Persona.documento.like(f'''%{search}%''')
        ).all()


@router.post('/create')
def create_historia(HistoriaBase:HistoriaBase,db:Session = Depends(get_db)):

    # persona_data = HistoriaBase.dict()
    # obj = {}
    # for key,value in persona_data.items():
    #     print(obj[key]=value)
            # setattr(HistoriaBase,key,value)
            # return HistoriaBase
    # persona_data = Persona(**HistoriaBase.dict().pop('persona'))
    # db.add(persona_data)
    # db.commit()
    # db.refresh(persona_data)
    # if persona_data.id:
    #     HistoriaBase.idpersona = persona_data.id

    #     historia_data = Historia(**HistoriaBase.dict(exclude='persona'))
    #     db.add(historia_data)
    #     db.commit()
    #     db.refresh(historia_data)
    return HistoriaBase
    