from fastapi import FastAPI,Path,HTTPException ,Query
import json
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal
from fastapi.responses import JSONResponse

app=FastAPI()

class Patient(BaseModel):
    id:Annotated[str,Field(...,description="Id of the patient",examples=["P001"])]
    name:Annotated[str,Field(...,description="Name of the patient")]
    city:Annotated[str,Field(...,description="City where patient is living")]
    age:Annotated[int,Field(...,gt=0,lt=120,description="Age of the patient")]
    gender:Annotated[Literal['male','female','others'],Field(...,description="Gender of the patient")]
    height:Annotated[float,Field(...,gt=0,description="height of the patient in meters")]
    weight:Annotated[float,Field(...,gt=0,description="Weight of the patient in kgs")]
    
    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Normal"
        else:
            return "Obese" 
    

def loadData():
    with open("data/patients.json","r") as f:
        data=json.load(f)
        
    return data

def saveData(data):
    with open("data/patients.json","w")as f:
        json.dump(data,f)
    
    
@app.get("/")
def hello():
    return {'message':"Patient Management System API"}

@app.get('/about')
def about():
    return {'messages':"A fully functional API to manage patient records"}


@app.get("/view")
def viewPatient():
    print("Inside vii")
    data=loadData()
    return data

@app.get("/view/{patient_id}")
def viewPatientById(patient_id:str=Path(...,description="Id of the patient in the database",example="P001")):
    data = loadData()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException (
            status_code=404,
            detail="Patient not found"
        )
        

@app.get("/sort")
def sortPatientById(sort_by:str=Query(...,description="Sort on basic of height weight and bmi"),order:str=Query('asc',description="Sort by ascending and descending order")):
    valid_fields=["height","weight","bmi"]
    valid_order=["asc","dsc"]
    print("in the sort order")
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f"""Invalid sort option.Please select from the below options {valid_fields}""")
    
    if order not in valid_order:
        raise HTTPException(status_code=400,detail=f"""Invalid Order option is selected. Please select from below options {valid_order}""")
    
    order_value= True if order =="asc" else False
    data=loadData()
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=order_value)
    
    return sorted_data


@app.post("/create")
def createPatient(patient:Patient):
    data=loadData()
    
    if patient.id in data:
        raise HTTPException(status_code=400,detail="Patient Already Exists !!")
    
    data[patient.id]=patient.model_dump(exclude=['id']) # Change model to dictionary and add it 
    
    saveData(data)
    
    return JSONResponse(status_code=201,content={"message":"Patient created successfully !!"})
    
    
    
     
    
    