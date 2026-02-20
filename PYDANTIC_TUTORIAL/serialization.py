# In Pydantic, serialization means converting a model instance into a format that can be stored or transmitted (usually dict or JSON).

from pydantic import BaseModel
class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address

address_dict={'city':'gurgaon','state':'haryana','pin':'122001'}
address1=Address(**address_dict)

patient_dict={'name':'nitish','gender':'male','age':35,'address':address1}
patient1=Patient(**patient_dict)

temp=patient1.model_dump() #str
temp2=patient1.model_dump_json() #json
temp3=patient1.model_dump(include=['name','gender']) #include and exclude
print(temp3)
print(type(temp3))