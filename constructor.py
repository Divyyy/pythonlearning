class Emp:
    company = "Asus"  # Class variable shared by all instances

    def __init__(self, salary, name, bond):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = Emp.company  # Correct way to reference class variable

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"The name of the emp is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years.")

# Creating an instance
e1 = Emp(3400, "John Doe", 4)

# Using instance methods
print(e1.get_salary())  # Output: 3400
e1.get_info()           # Output: The name of the emp is John Doe. Salary is 3400. The bond is for 4 years.

# Show all attributes and methods of the object
print(dir(e1))
