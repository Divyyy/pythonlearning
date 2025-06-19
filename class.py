# class is a blueprint or a template eg form for an exam that contains name, age,electives, father's name etc
#object specfic instances created from the template(class) eg form which contains the data for john doe
class employe:
    company ="HP"
    def get_salary(self):
        return 34000
e = employe() # an obj of an employee is created
print(e.get_salary())