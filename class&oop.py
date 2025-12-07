# Python Recap: Classes and Object-Oriented Programming (OOP)

# ===== BASIC CLASS CONCEPTS =====
print("--- BASIC CLASS CONCEPTS ---\n")

# 1. Simple class definition
class Dog:
    pass

print("1. Empty class:")
my_dog = Dog()
print(f"Created object: {my_dog}")
print(f"Type: {type(my_dog)}")
print()

# 2. Class with __init__ (constructor)
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

print("2. Class with constructor:")
my_cat = Cat("Whiskers", 3)
print(f"Cat name: {my_cat.name}, Age: {my_cat.age}")
print()

# 3. Class with methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old"
    
    def birthday(self):
        self.age += 1
        return f"Happy birthday! Now {self.age} years old"

print("3. Class with methods:")
person = Person("Alice", 25)
print(person.introduce())
print(person.birthday())
print()

# 4. Class attributes vs instance attributes
class Car:
    # Class attribute (shared by all instances)
    wheels = 4
    
    def __init__(self, brand, model):
        # Instance attributes (unique to each instance)
        self.brand = brand
        self.model = model

print("4. Class vs Instance attributes:")
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
print(f"car1: {car1.brand} {car1.model}, wheels: {car1.wheels}")
print(f"car2: {car2.brand} {car2.model}, wheels: {car2.wheels}")
print(f"Class attribute: Car.wheels = {Car.wheels}")
print()

# ===== ENCAPSULATION =====

# 5. Public, protected, and private attributes
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner              # Public
        self._account_number = "12345"  # Protected (convention)
        self.__pin = "1234"             # Private (name mangling)
    
    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        self.__pin = new_pin

print("5. Public, Protected, Private:")
account = BankAccount("Bob", 1000)
print(f"Public: {account.owner}")
print(f"Protected: {account._account_number}")
print(f"Private (via method): {account.get_pin()}")
# print(account.__pin)  # This would raise AttributeError
print(f"Name mangled access: {account._BankAccount__pin}")
print()

# 6. Property decorator (getters and setters)
# @property lets you use a method like an attribute.
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

print("6. Property decorator:")
temp = Temperature(25)
print(f"Celsius: {temp.celsius}")
print(f"Fahrenheit: {temp.fahrenheit}")
temp.celsius = 30
print(f"New Celsius: {temp.celsius}")
print()

# ===== INHERITANCE =====
print("--- INHERITANCE ---\n")

# 7. Single inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog2(Animal):
    def speak(self):
        return "Woof!"

class Cat2(Animal):
    def speak(self):
        return "Meow!"

print("7. Single inheritance:")
dog = Dog2("Buddy")
cat = Cat2("Mittens")
print(f"{dog.name} says: {dog.speak()}")
print(f"{cat.name} says: {cat.speak()}")
print()

# 8. super() to call parent methods
class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly
    
    def speak(self):
        return "Chirp!"
    
    def info(self):
        parent_speak = super().speak()
        return f"{self.name} - Can fly: {self.can_fly}, Parent says: {parent_speak}"

print("8. super() function:")
bird = Bird("Tweety", True)
print(bird.info())
print()

# 9. Multiple inheritance
class Flyable:
    def fly(self):
        return "Flying high!"

class Swimmable:
    def swim(self):
        return "Swimming fast!"

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return "Quack!"

print("9. Multiple inheritance:")
duck = Duck("Donald")
print(f"{duck.name} says: {duck.speak()}")
print(duck.fly())
print(duck.swim())
print()

# 10. Method Resolution Order (MRO)
print("10. Method Resolution Order:")
print(f"Duck MRO: {Duck.__mro__}")
print()

# ===== POLYMORPHISM =====
print("--- POLYMORPHISM ---\n")

# 11. Method overriding
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

print("11. Method overriding:")
shapes = [Rectangle(5, 3), Circle(4)]
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area()}")
print()

# 12. Duck typing (polymorphism without inheritance)
class Plane:
    def fly(self):
        return "Plane flying!"

class Superhero:
    def fly(self):
        return "Superhero flying!"

def make_it_fly(thing):
    return thing.fly()

print("12. Duck typing:")
print(make_it_fly(Plane()))
print(make_it_fly(Superhero()))
print()

# ===== SPECIAL/MAGIC METHODS =====
# 13. __str__ and __repr__
# __str__ is meant to be human readable
# __repr__ is meant to help the developer understand the class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

print("13. __str__ and __repr__:")
book = Book("1984", "George Orwell")
print(f"str(): {str(book)}")
print(f"repr(): {repr(book)}")
print()

# 14. __len__ and __getitem__
class Playlist:
    def __init__(self, songs):
        self.songs = songs
    
    def __len__(self):
        return len(self.songs)
    
    def __getitem__(self, index):
        return self.songs[index]

print("14. __len__ and __getitem__:")
playlist = Playlist(["Song1", "Song2", "Song3"])
print(f"Length: {len(playlist)}")
print(f"First song: {playlist[0]}")
print()

# 15. Arithmetic operators
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

print("15. Arithmetic operators:")
v1 = Vector(2, 3)
v2 = Vector(1, 4)
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print()

# 16. Comparison operators
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __eq__(self, other):
        return self.grade == other.grade
    
    def __lt__(self, other):
        return self.grade < other.grade
    
    def __gt__(self, other):
        return self.grade > other.grade

print("16. Comparison operators:")
student1 = Student("Alice", 85)
student2 = Student("Bob", 90)
print(f"student1 == student2: {student1 == student2}")
print(f"student1 < student2: {student1 < student2}")
print(f"student2 > student1: {student2 > student1}")
print()

# ===== CLASS METHODS AND STATIC METHODS =====
print("--- CLASS METHODS AND STATIC METHODS ---\n")

# Feature	                    staticmethod	classmethod
# Can call without object?	    ✅ Yes	      ✅ Yes
# First parameter	                none	         cls
# Knows class?	                ❌ No	        ✅ Yes
# Used for	                utility functions	factories, modifying class state

# 17. Class methods
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomatoes", "basil"])
    
    @classmethod
    def pepperoni(cls):
        return cls(["mozzarella", "tomatoes", "pepperoni"])

print("17. Class methods (factory):")
pizza1 = Pizza.margherita()
print(f"Margherita: {pizza1.ingredients}")
pizza2 = Pizza.pepperoni()
print(f"Pepperoni: {pizza2.ingredients}")
print()

# 18. Static methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

print("18. Static methods:")
print(f"MathUtils.add(5, 3) = {MathUtils.add(5, 3)}")
print(f"MathUtils.multiply(4, 7) = {MathUtils.multiply(4, 7)}")
print()

# ===== ABSTRACT CLASSES =====

# 19. Abstract base class
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    def honk(self):
        return "Beep beep!"

class Car2(Vehicle):
    def start_engine(self):
        return "Car engine started"
    
    def stop_engine(self):
        return "Car engine stopped"

print("19. Abstract base class:")
car = Car2()
print(car.start_engine())
print(car.honk())
# vehicle = Vehicle()  # This would raise TypeError
print()

# ===== COMPOSITION =====

# 20. Composition (has-a relationship)
class Engine:
    def start(self):
        return "Engine started"

class Wheels:
    def __init__(self, count):
        self.count = count

class Car3:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()
        self.wheels = Wheels(4)
    
    def info(self):
        return f"{self.brand} has {self.wheels.count} wheels"

print("20. Composition:")
car = Car3("Tesla")
print(car.info())
print(car.engine.start())
print()

# ===== DATA CLASSES (Python 3.7+) =====

# 21. Dataclass
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    
    def distance_from_origin(self):
        return (self.x**2 + self.y**2)**0.5

print("21. Dataclass:")
point = Point(3, 4)
print(f"Point: {point}")
print(f"Distance: {point.distance_from_origin()}")
print()

# ===== ADVANCED CONCEPTS =====

# 22. __call__ (making objects callable)
class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

print("22. __call__ (callable objects):")
times_three = Multiplier(3)
print(f"times_three(5) = {times_three(5)}")
print()

# 23. __enter__ and __exit__ (context manager)
class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        print(f"Opening {self.filename}")
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            print(f"Closing {self.filename}")
            self.file.close()

print("23. Context manager:")
# This would actually create a file
# with FileManager('test.txt') as f:
#     f.write('Hello')
print("(Example shown - requires file system)")
print()

# 24. Metaclasses (advanced)
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "Connected"

print("24. Metaclass (Singleton pattern):")
db1 = Database()
db2 = Database()
print(f"db1 is db2: {db1 is db2}")
print()

# 25. __slots__ (memory optimization)
class OptimizedPoint:
    __slots__ = ['x', 'y']
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

print("25. __slots__ (memory optimization):")
opt_point = OptimizedPoint(10, 20)
print(f"Point: ({opt_point.x}, {opt_point.y})")
# opt_point.z = 30  # This would raise AttributeError
print("__slots__ prevents adding new attributes dynamically")
print()

print("="*60)
print("END OF OOP CONCEPTS")
print("="*60)