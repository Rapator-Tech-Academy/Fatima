#PYTHON OOP
class Employee:
    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay
        self.email = name + '.' + surname + '@company.com'

        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.name, self.surname)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        #self.pay = int(self.pay * self.raise_amount)

    @classmethod #decorator, turn regular method into class method 
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    

    
emp_1 = Employee('Fatima', 'Askerova', 50000)
emp_2 = Employee('test', 'test', 3000) 

print(Employee.num_of_emp)

Employee.set_raise_amount(1.05)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

#same output
#print ('{} {}'.format(emp_1.name, emp_1.surname))
#print(Employee.fullname(emp_1))
print(emp_1.fullname()) 
 

print(emp_1.email) 
print(emp_2.email)

