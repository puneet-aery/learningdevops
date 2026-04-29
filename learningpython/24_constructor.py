class Employee:
    salary = 50000
    language = "Python" 
    
    def __init__(self, name, language): #constructor method or dunder method called automatically, it is called when an instance of the class is created. 
                                #  It is used to initialize the  attributes of the class.
        self.name = name
        self.language = language
        
        
        
        
        
puneet = Employee("Puneet", "Java") #when we create an instance of the class, we need to pass the arguments to the constructor method. The constructor method will initialize the attributes of the class with the values passed as arguments.
print(puneet.name, puneet.salary, puneet.language,puneet.salary)