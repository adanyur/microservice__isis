from fastapi import Depends,APIRouter, HTTPException
from models import Citas
from schemas import CitasBase
from sqlalchemy.orm import Session
from db import get_db,Base,engine



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

@router.post('/create')
def create_citas(CitasBase:CitasBase,db:Session = Depends(get_db)):
    row_item = Citas(**CitasBase.dict())
    db.add(row_item)
    db.commit()
    db.refresh(row_item)
    return row_item

@router.put('/update/{id}')
def update_citas(id:int,CitasBase:CitasBase,db:Session = Depends(get_db)):
    data = db.query(Citas).filter(Citas.id == id).first()
    if not data:
        raise HTTPException(status_code=404,detail="Citas no existe")
    return data;


@router.post('/')
def list_horarios():
    return;










