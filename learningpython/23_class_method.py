class Employee:
    salary = 50000
    language = "Python"  
    
    def getinfo(self):
        print(f"the langusage is {self.language} and the salary is {self.salary}")
        
        
    @staticmethod  #it does not need self parameter as it is not bound to any instance of the class. 
    def greet():
        print("Hello, Good Morning.")
        
        
        
        
        
        
puneet = Employee()
puneet.name = "Puneet"
puneet.language = "Java" #instance attribute, it will override the class attribute as the instance attribute has higher precedence than the class attribute.  
puneet.greet()
print(puneet.name, puneet.salary, puneet.language)
puneet.getinfo() # or
# Employee.getinfo(puneet) 
# we can also call the method using the class name and passing the instance as an argument. 
# This is because the method is bound to the instance, and it needs to be passed as an argument when called using the class name.