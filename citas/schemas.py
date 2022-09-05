from typing import List
from modelBase import * 


class PersonaIn(PersonaBase):
    class Config:
        orm_mode = True

class MedicoIn(MedicoBase):
    class Config:
        orm_mode = True

class EspecialidadIn(EspecialidadBase):
    class Config:
        orm_mode = True

class ConsultorioIn(ConsultorioBase):
    class Config:
        orm_mode = True

class TurnoIn(TurnoBase):
    class Config:
        orm_mode = True

class HistoriaIn(HistoriaBase):
    class Config:
        orm_mode = True

class Citas(CitasBase):
    class Config:
        orm_mode = True
    

class Actomedico(BaseModel):
    id:int
    idadminsion:int
    class Config:
        orm_mode = True

class Admision(AdmisionBase):
    actomedico:Actomedico = None
    class Config:
        orm_mode = True



#RELATIONS
class ProgramacionIn(ProgramacionBase):
    medico:MedicoIn = None
    consultorio:ConsultorioIn = None
    turno:TurnoIn = None
    especialidad:EspecialidadIn = None
    class Config:
        orm_mode = True

class CitaIn(CitasBase):
    programacion:ProgramacionIn = None
    class Config:
        orm_mode = True

class HistoriaPersonaIn(HistoriaBase):
    persona:PersonaIn = None
    class Config:
       orm_mode = True


class CitasIn(CitasBase):
    paciente:HistoriaPersonaIn = None
    admision:Admision =  None
    class Config:
        orm_mode= True


class AgendaMedicaIn(ProgramacionIn):
    citas:List[CitasIn] = None
    
    class Config:
        orm_mode = True

class PlantillaHorariosIn(BaseModel):
    idprogramacion:int
    orden:int
    hora:time
    fecha:date
    cita:CitasIn = None
    class Config:
        orm_mode = True

class AdmisionCitasIn(HistoriaBase):
    persona:PersonaIn = None
    cita:CitaIn = None
    class Config:
        orm_mode = True