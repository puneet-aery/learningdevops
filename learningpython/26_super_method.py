
# super method is used to call the constructor of the parent class. It is used to initialize the attributes of the parent class.


# class Employee:
#     def __init__(self):
#         print("this is Employee class constructor")

# class Programmer(Employee):
#     def __init__(self):
#         super().__init__() #super() is used to call the constructor of the parent class. It is used to initialize the attributes of the parent class.
#         print("this is Programmer class constructor")
        
        
        
# puneet = Programmer() #when we create an instance of the child class, the constructor of the parent class is called first, and 
                      # then the constructor of the child class is called.


# class method is confined to class only i.e instance attribute can not supercede the class attribute

class Employee:
    company = "Google"  
    @classmethod
    def getCompany(cls):
        print("the company is ",cls.company)

puneet = Employee()
puneet.company = "Microsoft" #instance attribute
puneet.getCompany()#instance attribute will supercede the class attribute
Employee.getCompany() #class method will access the class attribute, not the instance attribute.    
