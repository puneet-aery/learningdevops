# f = open("file.txt", "r") # open the file in read mode
# data = f.read() # read the contents of the file
# print(data) # print the contents of the file
# f.close() # close the file  

# f = open("file.txt2", "w") # open the file in write mode
# data = f.write("Hello, this is a test file.") # creates a new file and writes data to the file
# f.close() # close the file


# f = open("file.txt", "a") # open the file in append mode
# data = f.write("hey puneet") # append data to the file
# f.close() # close the file



with open("file.txt", "r") as f: # open the file in read mode
    data = f.read() # read the contents of the file
    print(data) # print the contents of the file

 