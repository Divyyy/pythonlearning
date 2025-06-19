class Animal:
    location = "India"
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self):
     print("genric animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("woof!")


# a = Animal("Dog")
# a.speak()

d = Dog("bruno","18")
d.speak()
print(d.location)