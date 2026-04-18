# functions are reusable blocks of code that perform a specific task. 
# They help to break down complex problems into smaller, manageable pieces, and they promote code reusability and modularity.


# def avg(): # fuction defination
#     a = int(input("enter first number: "))
#     b = int(input("enter second number: "))
#     average = (a + b) / 2
#     print(average) 
    

# avg() #  function call


# FUNCTION WITH ARGUMENTS
# def greeting(name,ending): # function definition with parameters
#     print("Hello " + name + "! Welcome to learning Python.")
#     print(f"Hello {name}! Welcome to learning Python.") # using f-string for formatting
#     print(ending)
#     return "Greeting sent!" # function returns a value  
    
    
# greeting("Puneet", "Nice to meet you!") # function call with argument   
# print(greeting("Puneet", "Nice to meet you!")) # printing the return value of the function




# FUNCTION WITH DEFAULT ARGUMENTS


def greet(name="sharma", greeting="Hello"): # function definition with default argument  
    print(f"{greeting} {name}!") # using f-string for formatting   
    return "Greeting sent!" # function returns a value 
    
greet("Puneet") # function call with default argument
greet("Puneet", "Hi") # function call with custom argument
greet() # function call with all default arguments  
print(greet()) # printing the return value of the function with default arguments   