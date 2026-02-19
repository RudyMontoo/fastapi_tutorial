# def insert_patient_data(name,age):
#     print(name)
#     print(age)
#     print("inserted into database")

# insert_patient_data('Rudra','Twenty One')




# METHOD 1
# def insert_patient_data(name:str,age:int):
#     print(name)
#     print(age)
#     print("inserted into database")

# insert_patient_data("Rudra",21)
# insert_patient_data("Rudra","21") #but this also work




# Method 2
def insert_patient_data(name:str,age:int):
    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print("inserted into database")
    else:
        raise TypeError("Incorrect datatype")
insert_patient_data("Rudra","21")  #error

# but this is not stable method because if we have 1000 of function so we will need to write in every function this things

# PROBLEM 1:this problem is solve by pydantic , there is no type validation

# PROBLEM 2: there is not data validation
def insert_patient_data(name:str,age:int):
    if type(name)==str and type(age)==int:
        if(age<0):
            raise ValueError("Age cant be neg")
        else:
            print(name)
            print(age)
            print("inserted into database")
    else:
        raise TypeError("Incorrect datatype")
insert_patient_data("Rudra","21")



# PYDANTIC #

DEFINE PYDANTIC MODEL

INITIATE THE MODEL WITH RAW INPUT data

PASS THE VALIDATION