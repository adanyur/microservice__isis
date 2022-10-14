from datetime import date, time
from typing import Optional

from pydantic import BaseModel, Field


class LoginBase(BaseModel):
    username:str
    password:str