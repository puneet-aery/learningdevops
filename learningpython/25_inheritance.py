class Employee:
    company = "Google"
    
# class Programmer(Employee):
#     language = "Python"
class Programmer:
    language = "Python"
    
# puneet = Programmer()
# print(puneet.company,puneet.language) #Single inderitance inherits attributes from the parent class. 


class coder(Employee,Programmer):
    name = "Puneet"
    
a = coder()
print(a.name,a.company,a.language) #Multiple inheritance inherits attributes from multiple parent classes.


# multilevel inheritance is when a child class inherits from a parent class, and then another child class inherits from the first child class.

class A:
    a = 1
class B(A):
    b = 2   
class C(B):
    c = 3
print(A.a) #Single inheritance
print(B.a,B.b) #Multilevel inheritance inherits attributes from the parent class.
print(C.a,C.b,C.c) #Multilevel inheritance inherits attributes from the parent class and the child class.