# MODEL VALIDATOR
# a model validator validates the entire model, not just one field.
# It’s used when validation depends on multiple fields together.
# eg if age is gt 60 then it is compulsory to add emergency number


from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List,Dict,Optional, Annotated


class Patient(BaseModel):
    name: str
    email:EmailStr
    age: int
    weight:float
    married: bool
    allergies: List[str] 
    contact_details: Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if  model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older tham 60 mush have an emergency contact')
        return model
def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.married)
  

    print("inserted into database")



patient_info={'name':'nitish','age':'65','email':'abc@hdfc.com','weight':79.9,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'235852890','emergency':'2345679'}}
patient1=Patient(**patient_info) #type conversion validation happen in this step

insert_patient_data(patient1)
