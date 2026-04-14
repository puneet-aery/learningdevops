# break statement is used to exit a loop prematurely. When the break statement is executed, the loop is terminated and the program continues 
# with the next statement after the loop. 
# continue statement is used to skip the current iteration of a loop and move on to the next iteration. When the continue statement is executed, 
# the rest of the code inside the loop is skipped for the current iteration, and the loop continues with the next iteration. 

# pass statement is used as a placeholder for code that is not yet implemented. It allows you to write code that is syntactically correct, b
# ut does not do anything.





for i in range(1,50):
    if i == 10:
        break
    print(i)
    
    
for i in range(1,50):
    if i == 10:
        continue
    print(i)    
    
    l = ["hello", "world", "python", "programming"]
for i in l:
    if i == "python":
        break
    print(i)    
    
l = ["hello", "world", "python", "programming"]
for i in l:
    if i == "python":
        continue
    print(i)    