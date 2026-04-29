class Sample(object):
    pass
x = Sample()
print(type(x))

class Dog(object):
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
sam = Dog(breed='Lab', name='Sam')
print(sam.breed)
print(sam.name)

class Circle(object):
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius
c = Circle()
c.setRadius(2)
print('Radius is: ', c.getRadius())
print('Area is: ', c.area())

class Animal(object):

    def __init__(self):
        print('Animal created')

    def whoAmI(self):
        print('Animal')

    def eat(self):
        print('Eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def whoAmI(self):
        print('Dog')

    def bark(self):
        print('Woof!')
dog = Dog()
dog.whoAmI()
dog.bark()
dog.eat()

class Book(object):

    def __init__(self, title, author, pages):
        print('A book is created')
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return 'Title:%s , author:%s, pages:%s ' % (self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book is destroyed')
book = Book('Python Rocks!', 'Jose Portilla', 159)
print(book)
print(len(book))
del book
