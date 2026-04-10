
# if else statements are used to execute a block of code based on a condition. 
# if elif else (ladder) statements are used to execute a block of code based on multiple conditions.


marks = int(input("Enter your marks: "))

if(marks >= 90):
    print("grade = A")
elif(marks >= 80):
    print("grade = B")
elif(marks >= 70):
    print("grade = C")
elif(marks >= 60):
    print("grade = D")
else:
    print("grade = F")
