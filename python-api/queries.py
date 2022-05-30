from models.medico import Medico

def insert(medico: Medico):
    return f"INSERT INTO Medico VALUES ('{medico.username}','{medico.job}','{medico.especialty}',{medico.cr})"

def findAll():
    return 'SELECT * FROM Medico'

def update(medico: Medico,id : int):
    return f"UPDATE Medico SET username ='{medico.username}', job = '{medico.job}',especialty = '{medico.especialty}', cr = {medico.cr} WHERE id={id}"

def delete(id: int):
    return f'DELETE FROM Medico WHERE id={id}'

def findOne(id:int):
    return f'SELECT * FROM Medico WHERE id={id}'