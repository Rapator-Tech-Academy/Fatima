def say_hello():
    return "Hello Python"
print(say_hello().upper())

def say_my_name (name="your name", surname="your surname"):
    return '{} {}'.format(name, surname)
print(say_my_name(name="Fatima", surname="Askerova"))

def get_country(*country):
    print("I am from " + country[0])
get_country("Azerbaijan", "China", "Germany")


 