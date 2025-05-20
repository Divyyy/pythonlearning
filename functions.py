def average (a,b,c):
    d = (a+b+c)/3.0
    # print(d)
    return d
o1 =average(3,5,1)
o2 = average(4,5,6)

print(o1)
print(o2)

# function argument.py
def add(a,b, plus=0):
    x = a+ b+plus
    return x
c = add(3,5,2)
print(c)

# lambda function

square = lambda x:x*x
sum = lambda x,y,z: x+y+z

print(square(3))
print(sum(3,2,1))