# tuple is an immutable sequence of values in Python. Once a tuple is created, its elements cannot be modified. T
# uples are defined using parentheses () and can contain elements of different data types. 
# Here are some examples of tuples:

a = (1,2,3,4,5,6,"hello",3.14,True)
print(a)  # Output: (1, 2, 3, 4, 5, 6, 'hello', 3.14, True)

print(type(a))  # Output: <class 'tuple'>

# functions of tuple

a.count(3)  # Output: 1
print(a.count(3))  # Output: 1
a.index("hello")  # Output: 6   
print(a.index("hello"))  # Output: 6
print(len(a))  # Output: 9

