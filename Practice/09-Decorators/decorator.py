def decorate_function(func):

    def wrap_func():
        print('This goes before the function')
        func()
        print('This goes after the function')
    return wrap_func

def basic_function():
    print('BASIC FUNCTION EXECUTED')
basic_function()
basic_function = decorate_function(basic_function)
basic_function()
