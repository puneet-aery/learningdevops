# recusion is a fucntion that calls itself. It is a powerful tool for solving problems that can be broken down into smaller, similar subproblems. 
# A recursive function typically has two main components: a base case that stops the recursion, and a recursive case that breaks the problem into smaller
# parts and calls itself.

def factoraial(n):
    if n == 0 or n ==1 : # base case
        return 1
    else: #   
        return n * factoraial(n - 1) # function calls itself with a smaller argument
    
    
    
    
    
n = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {n} is: {factoraial(n)}") # printing the result of the function call