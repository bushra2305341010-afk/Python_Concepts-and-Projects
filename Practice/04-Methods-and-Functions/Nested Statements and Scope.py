f = lambda x: x ** 2
name = 'this is a global name'

def greet():
    name = 'sammy'

    def hello():
        print('Hello ' + name)
    hello()
greet()
print(name)
print(type(len))
x = 20

def changeX(x):
    print('x is ', x)
    x = 50
    print('changed x to ', x)
changeX(x)
print('x is still ', x)
x = 50

def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)
print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)
