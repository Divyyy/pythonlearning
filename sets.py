s = {3, 23 , 2 ,11}
print(s, type(s))
#unorder,unique collections
# print(s[3])  you are not allowed to do something like this
s.add(32)
s.remove(3)
s.discard(345644) # remove only if present else dont through an error
# print(s)

#operatiions
a= {3,23,1}
b= {23,4,2,55,1}
c = a.union(b)
print(c)

d= a.intersection(b)
print(d)
e=a.difference(b)
print(e)
f=b.difference(a)
print(f)