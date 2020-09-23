#Generators, Itertators, Decorators

#Itertators
#my_list = [4, 7, 0, 3]
#
#my_iter = iter(my_list)
#
#print(next(my_iter)) #use next() func to manually iterate trough all the items in my_list
#print(next(my_iter))
#print(next(my_iter))
#print(next(my_iter))
#
#next(my_iter) #StopIteration

class ThreePower:
    """Comment this part so others would understand your code"""
    
    def __init__(self, maxnum = 0):
        self.max = maxnum

    def __iter__(self):
        self.n = 0 
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 3 ** self.n
            self.n =+ 1
        else:
            raise StopIteration
    
a = ThreePower(9)

my_iter = iter(a)

for i in a:
    print(i)
        
#Generators no return, instead yield 
def get_three_power(maximum):
    my_list = list(range(0,maximum+1))
    for i in my_list:
        yield 3 ** i
    
    b = get_three_power(9)

    for i in b:
        print(i)

#Decorator
def my_dec(func):
    def inner():
        print("Decorator addeed")
        func()
    return inner

def say_hi ():
    return f"Hello world"

    print(say_hi())
    a = my_dec(say_hi())
    print(a)



