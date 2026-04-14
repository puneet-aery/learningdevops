num =int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num*i}")
#     # or print(num, "x", i, "=", num*i)


# i = 1
# while i <= 10:
#     print(f"{num} x {i} = {num*i}")
#     i += 1

# sum = 0
# for i in range(1, num+1):
#     sum = sum + i
# print(sum)
    
    
# multiplication = 1
# for i in range(1, num+1):
#     multiplication = multiplication * i
# print(multiplication)





for i in range(1, num+1):
    print(" " * (num - i) + "*" * (2*i - 1))
   


