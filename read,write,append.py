f = open("div.txt", "r")

content = f.read()
print(content)
f.close()

#write file in python
f = open("john doe.txt", "w")

string = '''
john doe is a nice guy'''

f.write(string)
f.close()




#append

f = open("john doe.txt", "a")

string = '''
john doe lives in bihar chapra'''

f.write(string)
f.close()