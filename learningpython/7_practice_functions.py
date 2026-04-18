#  degree celsius to fahrenheit formula c/5 = (f-32)/9

def f_to_c(f):
    return (f - 32) * 5/9




f = int(input("enter temp in fagrenheit: "))
c = f_to_c(f)
print(f"{round(c, 2)}°C")
print("temp is celsius is", round(c, 2),"°C")
