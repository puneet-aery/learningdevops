list =[1,"hello",3.14,True,"puneet"]
print(list)  # Output: [1, 'hello', 3.14, True, 'puneet']
print(list[0])  # Output: 1 
print(list[1:4])  # Output: ['hello', 3.14, True]


# list functtions are built-in functions in Python that allow you to manipulate and work with lists. Here are some examples

list.append("sharma")
print(list)  # Output: [1, 'hello', 3.14, True, 'puneet', 'sharma']

list.insert(1,2)
print(list)  # Output: [1, 2, 'hello', 3.14, True, 'puneet', 'sharma']
list.remove('sharma')
print(list)  # Output: [1, 2, 'hello', 3.14, True, 'puneet']
list.pop(4)
print(list)  # Output: [1, 2, 'hello', 3.14, 'puneet']
