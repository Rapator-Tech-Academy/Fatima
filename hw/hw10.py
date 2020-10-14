#decorators

def outer_func():
    message = 'Hello'

    def inner_func():
        print(message)
    return inner_func()

my_func = outer_func()
my_func()
my_func()
my_func()


