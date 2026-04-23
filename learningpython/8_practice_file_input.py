# f = open("poem.txt", "r") # open the file in read mode
# d = f.read() # read the contents of the file
# if "twinkle" in d:
#     print("found")  
#     print(d) # read the contents of the file
# else:
#     print("not found")
# f.close() # close the file  


# write a table utpo 20 and store in a file called table.txt

def tablefun(n,m):    
        table = ""
        for i in range(1, 11):
            table += f"{n} X {i} = {n*i}\n"
        with open(f"tables/table_{n}.txt", "w") as f: # open the file in write mode
            f.write(table) # write the table to the file
            # or without using with statement
        # f = open(f"tables/table_{n}.txt", "w") # open the file in write mode
        # f.write(table) # write the table to the file
        # f.close() # close the file

# for i in range(1, 21):
#     tablefun(i,10)

    
    
    
    