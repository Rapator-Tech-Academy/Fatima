"""PYTHON OOP"""

class Employee:
    num_of_emp = 0
    raise_amount = 1.04 #raise 4%

    #regural methods 
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

    @classmethod
    def form_string(cls, emp_str):
        name, surname, pay = emp_str.split('-')
        return cls(name, surname, pay)
    
    #static methods
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
#Inheritance
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, name, surname, pay, prog_lang):
        super().__init__(name, surname, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, name, surname, pay, employees=None):
        super().__init__(name, surname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())



emp_1 = Employee('Fatima', 'Askerova', 50000)
emp_2 = Employee('test', 'test', 3000) 


print(Employee.num_of_emp)

#raise salary using @classmethod
Employee.set_raise_amount(1.05) #use classmethod to change raise up to 5%

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

#same output
#print ('{} {}'.format(emp_1.name, emp_1.surname))
#print(Employee.fullname(emp_1))
print(emp_1.fullname()) 

print(emp_1.email) 
print(emp_2.email)

#create new emp
emp_str_1 = 'John-Doe-7000'
emp_str_2 = 'Jane-Doe-4000'
emp_str_3 = 'Jon-Dop-7000'
#splits string with classmethod
new_emp_1 = Employee.form_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

#check if it is work date or not
import datetime
my_date = datetime.date(2020, 9, 24)

print(Employee.is_workday(my_date)) #returns True

#inheritance part
dev_1 = Developer('Fatima', 'Askerova', 5000, 'Python')
dev_2 = Developer('Bla', 'Bla', 3000, 'Java')

mgr_1 = Manager('lala', 'lala', 9000, [dev_1])
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)


print(mgr_1.email)
mgr_1.print_emps()
#print(help(Developer)) using help method you can see how inheritance works 
print(dev_1.email)
print(dev_1.prog_lang)
print(dev_2.email)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Developer))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))


