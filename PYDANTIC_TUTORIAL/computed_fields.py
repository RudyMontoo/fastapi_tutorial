from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field
from typing import List,Dict,Optional, Annotated

# Computed_field
# a computed field is a read-only field whose value is derived from other fields in the model.
# It is not stored in input, but calculated dynamically.
# eg BMI
class Patient(BaseModel):
    name: str
    email:EmailStr
    age: int
    weight:float
    height:float
    married: bool
    allergies: List[str] 
    contact_details: Dict[str,str]

    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.married)
    print('BMI',patient.calculate_bmi) # jo function ka naam hoga whi naam field ka bhi ho jayega

    print("inserted into database")



patient_info={'name':'nitish','age':'30','email':'abc@hdfc.com','weight':79.9,'height':1.5,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'235852890'}}
patient1=Patient(**patient_info) #type conversion validation happen in this step

insert_patient_data(patient1)