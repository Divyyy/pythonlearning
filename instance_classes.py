class emp:
    company = "Asus"
    def __init__(self,salary,name,bond,company):
     self.salary = salary
     self.name = name
     self.bond = bond
     self.company = company
    
    def get_salary(self):
        return self.salary
    
    def get_info(self):
       print(f"the name of the emp is {self.name}.salary is {self.salary}.the bond is for {self.bond} years")
    

e1 = emp(3400,"john Doe",4)
print(e1.get_salary())
e1.get_info()

print(dir(e1))