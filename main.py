from fastapi import FastAPI,Path,HTTPException ,Query
import json
app=FastAPI()


def loadData():
    with open("data/patients.json","r") as f:
        data=json.load(f)
        
    return data
    
    
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
