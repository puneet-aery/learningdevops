# class is defined as a blueprint for creating objects. It allows you to encapsulate data and functions that operate on that data into a single unit.
# In Python, you can define a class using the `class` keyword followed by the class name and a colon.

class Employee:
    salary = 50000
    language = "Python"    
    
    
    
    
puneet = Employee()
puneet.name = "Puneet"
puneet.language = "Java" #instance attribute, it will override the class attribute as the instance attribute has higher precedence than the class attribute.  
print(puneet.name, puneet.salary, puneet.language)
  
    
    # # here Employee is the class, and puneet is an instance of that class and called an object. We can access the attributes of the class using the instance.
    # salary and language are class attributes whereas name is an instance attribute. Class attributes are shared by all instances of the class, while 
    # instance attributes are unique to each instance.