from pydantic import BaseModel

class Medico(BaseModel):
    username: str 
    job:str 
    especialty:str 
    cr: int
    
