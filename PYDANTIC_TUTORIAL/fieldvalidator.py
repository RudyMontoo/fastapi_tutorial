from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List,Dict,Optional, Annotated
# FIELD VALIDATOR
# A field validator is a function that validates (and optionally transforms) a specific field of a data model before or after it is processed.
# eg i want name should be in capital etc


class Patient(BaseModel):
    name: str
    email:EmailStr
    age: int
    weight:float
    married: bool
    allergies: List[str] 
    contact_details:Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains=['hdfc.com','icici.com']
        # abc@hdfc.com
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value

    @field_validator('name')
    @classmethod
    def name_validator(cls, value):
        return value.upper()

    @field_validator('age',mode='after')
    @classmethod
    def age_validator(cls, value):
        if 0<value<100:
            return value
        else:
            raise ValueError("age should be in between o and 100")



def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.married)
  

    print("inserted into database")



patient_info={'name':'nitish','age':'30','email':'abc@hdfc.com','weight':79.9,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'235852890'}}
patient1=Patient(**patient_info) #type conversion validation happen in this step

insert_patient_data(patient1)


# field validator work in two mode
# 1 before mode -> runs before type parsing
# 2 after mode(default) -> runs after type parsing