def func_name(arg1, arg2=0, arg3=1): #default value
    """function body"""
    print(f'{arg1}, {arg1}, {arg1}')

func_name(arg1=1, arg2=2, arg3=3)

func_name(arg1=2) #true, cuz you gave value to arg1

#func_name() #false

#unpacking 
names = ['Ned', 'Cat', 'Rob']

def get_customers (a, b, c):
    customers = f"{a}, {b}, {c}"
    return customers

customers = get_customers(a=names[0], b=names[1], c=names[2]) 
print(customers)

#unpacking (extract)
names = ['Ned', 'Cat', 'Rob']

def get_customers (a, b, c):
    customers = f"{a}, {b}, {c}"
    return customers

customers = get_customers(*names) #extract method
print(customers)


def return_double_val(a, b):
    answ1 = a + b
    answ2 = a - b
    return answ1, answ2

rslt1, rslt2 = return_double_val(50, 15)

print(rslt1)
print(rslt2)


"""
names = ['Ned', 'Cat', 'Rob']

def get_stark(a, b, c):
    stark = f"{a}, {b}, {c}"
    return stark

stark = get_stark(*names)

print(stark)
"""

