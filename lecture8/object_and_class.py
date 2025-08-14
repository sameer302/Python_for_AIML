# we moved from procedural to functional and then to object oriented programming
# this was done to relate coding with real world scenarios

# class Student:
#     name = "sameer"

# s1 = Student()
# print(s1.name) # same name for every student

# class College:
#     name = "IIT"
#     location = "Powai"
#     rank = 1

# college = College()
# print(college.name, college.rank) # printed as two separate values, not as a tuple

# class Laptop:
#     # default constructor
#     def __init__(self, price):
#         print("default constructor")

#     # parameterized constructor
#     def __init__(self, fullname, model): # here self is alias for the object initiating the class, self or any other name but one parameter is must for creating init function
#         self.name = fullname # here it will create a name attribute and assign it the given value
#         self.model = model # here it will create model attribute and assign it the passed value
#         print("adding new laptop in database...")

# if we don't create the init function then also python creates it for us automatically and in such case the
# function definition just contains pass

# this concept of default and parameterized init functions wont work in python coz
# python does not support method overloading directly so we need to handle that separately

# class Laptop:

#     def __init__(self, name = None, model = None): 
#         if((name == None) and (model == None)):
#             print("initialized with no argument")
#         elif(model == None):
#             print("initialized with one argument")
#             self.name = name
#         else:
#             print("initialized with two arguments")
#             self.name = name # here it will create a name attribute and assign it the given value
#             self.model = model # here it will create model attribute and assign it the passed value

# l1 = Laptop("Dell", "G3 15")
# print(l1.name)
# print(l1.model)

# l2 = Laptop("Asus")
# print(l2.name) 

# l3 = Laptop()
# print(l3)

# ANOTHER WAY OF HANDLINE THE ABOVE SCENARIO

class Laptop:

    def __init__(self, *args): 
        if(len(args) == 0):
            print("initialized with no argument")
        elif(len(args) == 1):
            print("initialized with one argument")
            self.name = args[0]
        else:
            print("initialized with two arguments")
            self.name = args[0] # here it will create a name attribute and assign it the given value
            self.model = args[1] # here it will create model attribute and assign it the passed value

l1 = Laptop("Dell", "G3 15")
print(l1.name)
print(l1.model)

l2 = Laptop("Asus")
print(l2.name) 

l3 = Laptop()
print(l3)

''' 
*args lets you pass any number of positional arguments to a function or method.
It collects them into a tuple.
Useful when the number of inputs isn't fixed

def greet(*args):
    for name in args:
        print(f"Hello, {name}!")

We can use list or tuple in place of *args but then we need to pass the arguments as a list or tuple and for no arguments we need to pass
empty list or tuple but in case of *args, we can directly pass the arguments as normal arguments.

The `print(f"Hello, {name}!")` statement uses Python's **f-string** formatting, a concise and readable way to embed expressions directly within 
string literals. Introduced in Python 3.6, f-strings allow variables and even inline expressions to be placed inside `{}` brackets, 
making string construction both intuitive and powerful. Compared to older methods like `.format()` and `%` formatting, f-strings are cleaner, 
easier to debug, and support dynamic content seamlessly. For example, `f"Twice of {x} is {2 * x}"` evaluates expressions on the fly, 
making f-strings ideal for modern Python development.


**kwargs allows a function or method to accept any number of keyword arguments.
It stores them as a dictionary where keys are argument names and values are their corresponding values.
Useful for handling optional or dynamic named parameters.

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

'''

# class Student:
#     college = "IITB" # class attribute, stored only once in memory

#     def __init__(self, name, marks=None):
#         self.name = name # object attribute, stored separately in memory for each object
#         self.marks = marks # object attribute
#         print("added new student to database")

# s1 = Student("sameer","99")
# print(s1.name)
# print(s1.marks)
# print(s1.college)

# print(Student.college)

# a class contains two main components, data(attributes) and methods(functions)

# class Food:
#     taste = "It is good"

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def cook(self):
#         print("time to cook",self.name)

# f1 = Food("vadapav",16)
# f1.cook()
# print(f1.taste)



# Static Methods  

# class Student:
#     @staticmethod # Enables a function to run at class level
#     def hello():
#         print("hello")

# s1 = Student()
# s1.hello()



# Abstraction
# Hide unnecessary details



# Encapsulation
# Wrapping data and function together

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car started")

# car1 = Car()
# car1.start()