# What is OOP in Python?
# Interview-ready answer:

# Object-Oriented Programming (OOP) is a programming approach that organizes code using classes and objects.
# It helps make applications reusable, modular, maintainable, and easier to manage.

# Python supports four major OOP principles:
# 1. Encapsulation
# 2. Inheritance
# 3. Polymorphism
# 4. Abstraction
# What is a class?
# A class is a blueprint or template used to create objects. It defines attributes and methods.
class Employee:
    def display(self):
        print("Welcome to OOPS progaming in python")

emp = Employee()
emp.display()
# What is an object?
# An object is an instance of a class. It has its own data and can use the methods defined by its class.
class Employee:
    name = "Ganesh"
    role = "Python Developer"


emp1 = Employee()

print(emp1.name)
print(emp1.role)
# Constructor, self, and variables
# What is __init__()?
# __init__() is a special method that Python automatically calls after creating an object.
# It is commonly used to initialize object attributes.
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp1 = Employee("John", 50000)

print(emp1.name)
print(emp1.salary)


# What is self?
# self refers to the current instance of a class.
# It allows us to access that object's attributes and methods.
# Instance variables vs class variables
# Instance variables: Each object can have its own value.
# 
# Class variables: Shared through the class and its instances unless an instance shadows the attribute.
class Employee:

    company = "ABC Technologies"  # Class variable

    def __init__(self, name, salary):
        self.name = name           # Instance variable
        self.salary = salary       # Instance variable


emp1 = Employee("John", 50000)
emp2 = Employee("David", 60000)

print(emp1.name)
print(emp2.name)
print(emp1.company)
print(emp2.company)
# What happens if you change a class variable?
class Employee:
    company = "ABC"

emp1 = Employee()
emp2 = Employee()

Employee.company = "XYZ" # it will update

print(emp1.company)
print(emp2.company)
# Types of methods
# Python classes commonly use three types of methods.
# 1. Instance method
# Works with an individual object's data. Its first parameter is conventionally self.
class Employee:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


emp = Employee("John")
emp.display()
# Class method
# Works with the class itself. It uses the @classmethod decorator and conventionally receives cls.
class Employee:

    company = "ABC"

    @classmethod
    def change_company(cls, name):
        cls.company = name


Employee.change_company("XYZ")

print(Employee.company)
# Static method
# A utility method associated with a class. It does not automatically receive self or cls.
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))
# Encapsulation
# encapsulation is nothing but grouping or bundling ot related things inside a class
#  1/ if we gourp in side a class like means code will clean and organized.
#  2, prevents the data from accidental removal or deletion.
# Public variables
# Can be accessed directly.
class Employee:
    def __init__(self):
        self.name = "John"

emp = Employee()
print(emp.name)
# Protected convention: _variable
# A single leading underscore indicates that an attribute is intended for internal or subclass use.
# It is a convention, not enforced access control.
class Employee:

    def __init__(self):
        self._salary = 50000

    def get_salary(self):
        return self._salary


emp = Employee()

print(emp.get_salary())

# Private name convention: __variable: Triggers name mangling.
# Python automatically changes the name of the attribute inside the class to _ClassName__attributeName,
# making it difficult to access directly from outside.
class Employee:

    def __init__(self):
        self.__salary = 50000

    def get_salary(self):
        return self.__salary


emp = Employee()

print(emp.get_salary())

class Employee:

    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):

        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")


emp = Employee(50000)

print(emp.get_salary())

emp.set_salary(60000)

print(emp.get_salary())

# Inheritance
# What is inheritance?
# Inheritance allows a child class to reuse attributes and methods from a parent class.
# It helps reduce code duplication and supports code reuse.
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()


# Single inheritance
# One child inherits from one parent.


class Parent:
    def display(self):
        print("Parent")


class Child(Parent):
    pass


# Multilevel inheritance
# A class inherits from another child class.
class Grandparent:
    def show1(self):
        print("Grandparent")


class Parent(Grandparent):
    def show2(self):
        print("Parent")


class Child(Parent):
    def show3(self):
        print("Child")


obj = Child()
obj.show1()
obj.show2()
obj.show3()

# Multiple inheritance
# One child inherits from multiple parents.
class Camera:
    def take_photo(self):
        print("Taking photo")


class Phone:
    def make_call(self):
        print("Making call")


class Smartphone(Camera, Phone):
    pass


mobile = Smartphone()

mobile.take_photo()
mobile.make_call()

# Hierarchical inheritance
# Multiple child classes inherit from one parent.
class Employee:
    def work(self):
        print("Employee working")


class Developer(Employee):
    pass


class Tester(Employee):
    pass

# Hybrid inheritance
# A combination of two or more inheritance types.

# What is super()?
# super() provides access to methods from the next class in the method resolution order (MRO).
# ]It is commonly used to call parent-class initialization or behavior.
class Employee:

    def __init__(self, name):
        self.name = name


class Developer(Employee):

    def __init__(self, name, language):
        super().__init__(name)
        self.language = language


dev = Developer("John", "Python")

print(dev.name)
print(dev.language)

# Method overriding and polymorphism
# What is method overriding?
# Method overriding happens when a child class provides its own implementation of an inherited method.
class Animal:

    def sound(self):
        print("Animal sound")


class Dog(Animal):

    def sound(self):
        print("Bark")


dog = Dog()
dog.sound()


# What is polymorphism?
# Polymorphism means one interface or method name can work with different object types, each providing its own behavior.

class EmailAlert:

    def send(self):
        print("Sending email alert")


class SMSAlert:

    def send(self):
        print("Sending SMS alert")


class TeamsAlert:

    def send(self):
        print("Sending Teams alert")


def send_notification(notification):
    notification.send()


send_notification(EmailAlert())
send_notification(SMSAlert())
send_notification(TeamsAlert())
# What is abstraction?
# Abstraction means exposing essential functionality while hiding implementation details.

# Python supports abstraction through the abc module and abstract base classes.

from abc import ABC, abstractmethod


class Report(ABC):

    @abstractmethod
    def generate(self):
        pass


class PDFReport(Report):

    def generate(self):
        print("Generating PDF report")


class ExcelReport(Report):

    def generate(self):
        print("Generating Excel report")


pdf = PDFReport()
pdf.generate()

excel = ExcelReport()
excel.generate()



