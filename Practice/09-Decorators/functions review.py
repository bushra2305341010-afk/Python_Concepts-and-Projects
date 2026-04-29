def func():
    return 1
print(func())
s = 'Global Variable'

def func_locals():
    print(locals())
print('Global variable keys:  ', globals().keys())
print('Value of global variable at key "s":  ', globals()['s'])
print(func_locals())

def hello(name='Nico'):
    print('Hello ' + name)
hello()
greet = hello
print(type(greet))
del hello
greet()

def new_hello(name='Nico'):
    print('The hello() function has been executed')

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return '\t This is inside the welcome() function'
    print(greet())
    print(welcome())
    print('Now we are back inside the hello() function')
new_hello()

def final_hello(name='Nico'):

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return '\t This is inside the welcome() function'
    if name == 'Nico':
        return greet
    else:
        return welcome
x = final_hello()
y = final_hello('Bacon')
print(x())
print(y())

def this_hello():
    return 'Hi Nico!'

def other(func):
    print('Other code would go here')
    print(func())
print(this_hello())
print(other(this_hello))
