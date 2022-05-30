import  configDatabase as _DB
import pyodbc as _pyodbc
import queries as _query
from models.medico import Medico

class Repository:
    __connection = None

    def __init__(self) -> None:
        self.__connection = self.getConnection()
    
    def getConnection(self):
        self.__connection = _pyodbc.connect(_DB.CONNECTION_STRING,autocommit=False)
        return self.__connection.cursor()

    def closeConnection(self):
        self.__connection.close()

    def commit(self):
        self.__connection.commit()

    def insert(self,medico: Medico):
            msg=""
            try:
                self.__connection.execute(_query.insert(medico))
                self.commit()
                msg = "Success to insert user"
            except:
                msg = "Failed to insert user"
                return 500,msg
            
            return 200,msg

    def findAll(self):
        data = []
        msg = ""
        try:
            records = self.__connection.execute(_query.findAll()).fetchall()
            column_names = [column[0] for column in self.__connection.description]
            for rec in records:
                data.append(dict(zip(column_names, rec)))
            msg = "Execution succeeded"
        except:
            msg = "Execution Failed"
            return data,500,msg
        return data,200,msg

    def delete(self,id : int):
        msg=""
        try:
            self.__connection.execute(_query.delete(id))
            msg = "User deleted with success"
        except:
            msg= "Failed to delete user"
            return 500,msg
            
        self.commit()
        return 200,msg
        

    def update(self,medico:Medico,id:int):
        msg = ""
        try:
            self.__connection.execute(_query.update(medico,id))
            self.commit()
            msg = "User updated with success"
        except:
            msg = "Failed to update user"
            return 500,msg
        
        return 200,msg    
    
    def findOne(self,id:int):
        data = []
        msg = ""
        try:
            records = self.__connection.execute(_query.findOne(id)).fetchall()
            column_names = [column[0] for column in self.__connection.description]
            for rec in records:
                data.append(dict(zip(column_names, rec)))
            msg = "User found with success"
        except:
            msg = "Execution Failed"
            return data,500,msg
        return data,200,msg


        

    

    

