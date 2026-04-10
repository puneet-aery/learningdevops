s1 ={1,2,3,5,8,10}

s2 = {1,4,6,7,8,9}

# union of sets
print(s1.union(s2))  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} because the union of two sets contains all the unique elements from both sets

# intersection of sets

print(s2.intersection(s1))  # Output: {1, 8} because the intersection of two sets contains only the elements that are present in both sets


# subsets

s3 = {5,2,3}

print(s3.issubset(s1))  # Output: True because s3 is a subset of s1, meaning all elements of s3 are also present in s1

print(s3.issubset(s2))  # Output: False because s3 is not a subset of s2, meaning not all elements of s3 are present in s2

