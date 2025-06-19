
#decorator is a function that makes a function, it creates a new function insdie its body(wrapper).  then it returns that new function


def decorator(func):
    def wrapper():
        print("I am to excute a function>>>>>")
        func()
        print("I Have executed this function>>>>")
    return wrapper










@decorator
def say_hello():
    print("hello!")


#say_hello()
f = decorator(say_hello)
f()


'''
it will look like this

def f():
print("i am about to execute a function......")
print("hello!")
print("i have excuted this function....")
'''