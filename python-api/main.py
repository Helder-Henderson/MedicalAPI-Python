from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Request
from repository import Repository
from models.medico import Medico
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def list_All_User(request: Request):
    """
    Show all registered doctors 
    """

    dba = Repository()
    data,status_code,msg = dba.findAll()
    if(status_code==500):
        raise HTTPException(status_code=status_code, detail=msg)
    dba.closeConnection()
    return templates.TemplateResponse("index.html", {"request":request,"data":data},status_code=status_code)
        
@app.get("/register")
def root(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
async def create_User(medico : Medico) -> None:
    """
    Add a doctor to database
    """

    dba = Repository()
    status_code,msg = dba.insert(medico)
    if(status_code == 500):
        return HTTPException(status_code=status_code, detail=msg)
    dba.closeConnection()
    return msg


@app.delete("/delete/{id}")
def delete_User(id:int):
    """
    Delete a doctor from database
    """

    dba = Repository()
    status_code,msg = dba.delete(id)
    dba.closeConnection()

    if(status_code==500):
        raise HTTPException(status_code,detail=msg)

    return msg
    

@app.get("/update/{user_id:int}")
def root(request: Request,user_id:int):

    dba = Repository()
    data,status_code,msg = dba.findOne(user_id)

    if(status_code==500):
        raise HTTPException(status_code=status_code,detail=msg)

    dba.closeConnection()
    return templates.TemplateResponse("update.html", {"request": request,"data":data})


@app.put("/update/{id:int}")
def update_User(medico:Medico,id : int):
    """
    Update doctor from database
    """
    

    dba = Repository()
    status_code,msg = dba.update(medico,id)

    if(status_code==500):
        raise HTTPException(status_code,detail=msg)

    dba.closeConnection()
    return msg
    
    



    

    
    

