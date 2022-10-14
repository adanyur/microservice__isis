
import json

from fastapi import APIRouter, HTTPException
from schemas import LoginBase

router = APIRouter(prefix='/login',tags=['Login'])

@router.post('')
async def login(loginBase:LoginBase):
    with open('data.json', 'r') as f:
        data = json.load(f)

    if data['User']['username'] != loginBase.username:
        raise   HTTPException(status_code=400, detail=f'''Usuario ingresado incorrecto''')

    if loginBase.password != '123':
        raise   HTTPException(status_code=400, detail=f''' Password ingresado incorrecto''')

    return data;

