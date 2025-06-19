marks = [54, 23, 64, 93, 32]
#list are mutable
mixed = [43, "hello", False,4.2]
# print(marks[0])
# print(marks[2:4])
#marks.append(63) it will add one elment in the list
marks.extend(mixed)
marks.pop()
print(marks)

# create a list contaning the table of 5

# a= 5
# table = []

# for i in range (1,11):
#     table.append(5*i)

table = [5 * i for i in range(1,11)]
print(table)