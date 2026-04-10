# sets are collections of unique elements. They are unordered and mutable, meaning you can add or remove elements from a set, 
# but the elements themselves must be immutable (like numbers, strings, or tuples). Sets are defined using curly braces {} 
# or the set() constructor.

dict = {}      # this is for empty dictionary
set = set()     # this is for empty set

a = {1,2,4,56,56,45,45,60,61}
print(a)  # Output: {1, 2, 4, 45, 56, 60, 61} because sets do not allow duplicate values and are unordered

# set methods
(a.add(70))  # Output: None because the add() method does not return any value, it modifies the set in place
print(a)

(a.remove(61))
print(a)
