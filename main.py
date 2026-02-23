from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json

app = FastAPI()


# -------------------------
# Utility Functions
# -------------------------

def load_data():
    try:
        with open('patients.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f, indent=4)


# -------------------------
# Root Endpoints
# -------------------------

@app.get("/")
def hello():
    return {"message": "Patient Management System API"}


@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient records"}


@app.get("/view")
def view():
    return load_data()


# -------------------------
# Path Parameter
# -------------------------

@app.get("/patient/{patient_id}")
def view_patient(
    patient_id: str = Path(..., description="ID of the patient", example="P001")
):
    data = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code=404, detail="Patient not found")


# -------------------------
# Query Parameter
# -------------------------

@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="height, weight or bmi"),
    order: str = Query("asc", description="asc or desc")
):
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field. Choose from {valid_fields}")

    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order. Use asc or desc")

    data = load_data()
    reverse = True if order == "desc" else False

    return sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=reverse)


# -------------------------
# Pydantic Model
# -------------------------

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Patient ID", examples=["P001"])]
    name: Annotated[str, Field(...)]
    city: Annotated[str, Field(...)]
    age: Annotated[int, Field(..., gt=0, lt=120)]
    gender: Annotated[Literal["male", "female", "others"], Field(...)]
    height: Annotated[float, Field(..., gt=0)]
    weight: Annotated[float, Field(..., gt=0)]

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        return "Obese"


# -------------------------
# Create Patient
# -------------------------

@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")

    data[patient.id] = patient.model_dump()
    save_data(data)

    return JSONResponse(status_code=201, content={"message": "Patient created successfully"})