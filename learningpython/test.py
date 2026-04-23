def tablefun(m):    
        table = ""
        n = 1
        for i in range(1, 11):
            table += f"{n} X {i} = {n*i}\n"
        with open(f"tables/table_{n}.txt", "w") as f: # open the file in write mode
            f.write(table) 
        n+=1
        if n>m:
            return