from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List,Dict,Optional, Annotated
class Patient(BaseModel):
    # name: str

    # Email str
    email:EmailStr
    # Urll datatype
    linkedin_url:AnyUrl

    # we can add requirement?condition  using Field
    
    age: int=Field(gt=0, lt=120)

    # add strictness
    weight:Annotated[float, Field(gt=0, strict=True)]

    # also field function is ued to insert metadata "Annotated use in this"
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give max len of name as 50 char', examples=['Nitish','Amit'])]
    # also we can default value using field
    # married:bool
    married: Annotated[bool, Field(default=None, description='is the patient married or not')]



    allergies: List[str] #here list will not work
    # if take only list then list can take any data type since we take List[str]



    # we can also make optional features rememeber when u make something optional u have to give default value
    contact_details:Optional[Dict[str,str]]=None

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.married)
  

    print("inserted into database")



patient_info={'name':'nitish','age':30,'email':'abc@gmail.com','linkedin_url':'https://www.linkedin.com/mynetwork/grow/','weight':79.9,'married':True,'allergies':['pollen','dust'],'contact_details':{'phone':'235852890'}}
patient1=Patient(**patient_info)

insert_patient_data(patient1)