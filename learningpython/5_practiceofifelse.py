
sub1 = int(input("Enter marks for subject 1: "))
sub2 = int(input("Enter marks for subject 2: "))    
sub3 = int(input("Enter marks for subject 3: "))

percentage = ((sub1+sub2+sub3)/300)*100
if (percentage>=40 and sub1>=(33/100)*100 and sub2>=(33/100)*100 and sub3>=(33/100)*100):
    print("Congratulations! You have passed the exam.")
else:
    print("Sorry! You have failed the exam.")   
    