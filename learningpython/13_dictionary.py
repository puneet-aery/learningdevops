# dictionary is set of key value pairs. It is unordered, changeable and indexed. No duplicate keys.

marks = {"puneet" :100,"sharma":97,"list":[1,2,3],"0": 50}
# print(type(marks),marks)

# dictionary methods 

# print(marks.items())  # Output: dict_items([('puneet', 100), ('sharma', 97), ('list', [1, 2, 3]), ('0', 50)]) in tuple form

# print(marks.keys())  # Output: dict_keys(['puneet', 'sharma', 'list', '0'])

# print(marks.values())  # Output: dict_values([100, 97, [1, 2, 3], 50])

# print(marks.get("puneet2"))  # Output: None

# print(marks["puneet2"])  # Output: KeyError: 'puneet2' because it is not present in the dictionary

marks.update({"puneet":99,"mohit":98}) 
print(marks)  # Output: {'puneet': 99, 'sharma': 97, 'list': [1, 2, 3], '0': 50, 'mohit': 98}