def sum(a,b):
    c =a+b   # local variables can only accessable only in fun
    return c
print(sum(5,6))

z=8 # global variable accessable to everyone



# global keyword

def sum(a,b):
    print ("hey i am summing")
    c= a+b
    global z
    z= 0
    return c