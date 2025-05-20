# single - quotes string
a = 'hello,Python'
#double-quoted string
b = "hello world"
#triple quoted string useful for multi line
c = '''this is
      a multi line string '''

#slicing
name = "harry0123456789"
# print (name [0:2])
# print (name [2:-3])
# print (name [0:10:n]) skip n-1 charc
print (name [0:10:2])
 


# d =len(a)
# print(d)
# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.title())


# text = "python is fun"
# print(text.find("is"))
# print(text.replace("n", "k"))

text = "Apples,Bananas,Pineapples"
print(text.split(","))
print(",".join(['Apples','Bananas', 'Pineapples']))



# fstrings
a = "john"
a1 = 10000
b = "jack"
b1 = 100
print(f"{a} you are awesome and take this {a1}$ bag")