from fastapi import Depends,APIRouter, HTTPException
from models import Historia,Persona,create_table
from schemas import CreateHistoria,ViewHistoria,ViewPersona
from typing import List
from sqlalchemy.orm import Session
from db import get_db

router = APIRouter(prefix='/historia',tags=['Historia'])

@router.get('/createTable')
def creates_tables():
    create_table()    
    return;

@router.get('/listById/{id}',response_model=ViewHistoria)
def get_historia(id:int,db:Session = Depends(get_db)):
    return db.query(Historia).filter(Historia.idpersona == id).first()


@router.get('/autocomplete/{search}',response_model=list[ViewPersona])

def get_like_paciente(search:str,db:Session = Depends(get_db)):
    
    return db.query(Persona).filter(Persona.estado == True, 
            Persona.paterno.like(f'''{search}%''') | 
            Persona.materno.like(f'''{search}%''') |
            Persona.nombres.like(f'''{search}%''') |
            Persona.documento.like(f'''{search}%''')
            ).all();


@router.post('/create')
def create_historia(CreateHistoria:CreateHistoria,db:Session = Depends(get_db)):
    historia = CreateHistoria        
    persona_data = Persona(**historia.dict().pop('persona'))
    db.add(persona_data)
    db.commit()
    db.refresh(persona_data)
    if persona_data:
        historia_data =  historia.dict(exclude={'persona'})
        historia_data['idpersona'] = persona_data.id
        create_historia = Historia(**historia_data)
        db.add(create_historia)
        db.commit()
        db.refresh(create_historia)
        return {"message":"Paciente registrado"}



@router.put('/update')
def update_historia():

    return {}
