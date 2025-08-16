# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("sam")
# print(s1)

# del s1
# print(s1)

# s2 = Student("jack")
# print(s2)
# print(s2.name)

# del s2.name
# print(s2)
# # print(s2.name)

# s3 = Student("cash")
# print(s3)
# print(s3.name)




# class Account:
#     def __init__(self, acc_no, acc_pwd):
#         self.acc_no = acc_no
#         self.acc_pwd = acc_pwd # here pwd is public attribute

# acc1 = Account(12345, "abc12")
# print(acc1.acc_no)
# print(acc1.acc_pwd)


# class Account:
#     def __init__(self, acc_no, acc_pwd):
#         self.acc_no = acc_no
#         self.__acc_pwd = acc_pwd # here pwd is private attribute

# acc1 = Account(12345, "abc12")
# print(acc1.acc_no)
# print(acc1.__acc_pwd)


# class Account:
#     def __init__(self, acc_no, acc_pwd):
#         self.acc_no = acc_no
#         self.__acc_pwd = acc_pwd

#     def show_pwd(self): # private attributes can be accessed only inside of the class
#         print(self.__acc_pwd)

# acc1 = Account(12345, "abc12")
# print(acc1.acc_no)
# acc1.show_pwd()


# class Person:
#     __name = "anonymous"

#     def __hello(self): # even methods can be made private
#         print(self.__name)

# p1 = Person
# print(p1.__name) # error: no attribute __name


# class Person:
#     __name = "anonymous"

#     def __hello(self): # even methods can be made private
#         print(self.__name)

# p1 = Person
# p1.__hello() # error: no attribute __hello


# class Person:
#     __name = "anonymous"

#     def __hello(self): # even methods can be made private
#         print(self.__name)

#     def welcome(self):
#         self.__hello()

# p2 = Person()
# p2.welcome()





## Inheritance ##

# Single Inheritance

# class Car: # Base class
#     wheels = 4

#     @staticmethod # we can only access static method from an derived class object
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(Car): # Derived class
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# print(car1.name)
# car1.start()
# car1.stop()
# print(car1.wheels)




# Multi-level Inheritance

# class Car: # Base class
#     wheels = 4

#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(Car): # Derived class
#     brand = "toyota"
#     def __init__(self, name):
#         self.name = name

# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("electrical")
# print(car1.type)
# print(car1.brand) 
# car1.start()
# car1.stop()
# print(car1.wheels)




# Multiple Inheritance

# class A:
#     varA = "Welcome to class A"

# class B:
#     varB = "Welcome to class B"

# class C(A,B):
#     varC = "Welcome to class C"

# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)



# Super method

# class Car: # Base class
#     wheels = 4

#     def __init__(self, type):
#         self.type = type

#     def start(self):
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(Car): # Derived class
#     def __init__(self, name,type):
#         self.name = name
#         super().__init__(type)
#         super().start()

# car1 = ToyotaCar("fortuner","electrical")
# print(car1.name)
# print(car1.type)




# class Person:
#     name = "anonymous"

#     def changeName(self,name):
#         self.name = name

# p1 = Person()
# p1.changeName("sam")
# print(p1.name)
# print(Person.name)


# class Person:
#     name = "anonymous"

#     def changeName(self,name):
#         Person.name = name

# p1 = Person()
# p1.changeName("sam")
# print(p1.name)
# print(Person.name)


# class Person:
#     name = "anonymous"

#     def changeName(self,name):
#         self.__class__.name = name

# p1 = Person()
# p1.changeName("sam")
# print(p1.name)
# print(Person.name)


# Three types of methods:
# 1) static methods: used when neither class nor object attribute is being changed
# 2) class methods: used when class attributes need to be changed
# 3) instance methods: used when object/instance attributes need to be changed

# class Person:
#     name = "anonymous"

#     @classmethod
#     def changeName(cls,name):
#         cls.name = name

# p1 = Person()
# p1.changeName("jack") # here classmethod is being called
# print(p1.name) # although p1 does not have special name attribute but here we are accessing the class attribute
# print(Person.name) # class attribute is being printed





# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.average = str((self.phy + self.chem + self.math)/3) + "%"

# s1 = Student(98,89,95)
# print(s1.phy)
# print(s1.average)
# s1.phy = 91
# print(s1.phy)
# print(s1.average)


# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     def calcAverage(self):
#         self.average = str((self.phy + self.chem + self.math)/3) + "%"

# s1 = Student(98,89,95)
# print(s1.phy)
# # print(s1.average) # error: student object has no attribute 'average'
# s1.calcAverage() # after calling this method average attribute will be made for the object
# print(s1.average)
# s1.phy = 91
# print(s1.phy)
# s1.calcAverage()
# print(s1.average)


# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     @property # these are called as decorators
#     def average(self): # here average will be a new attribute whose value will be updated everytime
#         return str((self.phy + self.chem + self.math)/3) + "%"
    
# s1 = Student(98,89,95)
# print(s1.phy)
# print(s1.average)
# s1.phy = 90
# print(s1.phy)
# print(s1.average)

# s2 = Student(76,87,98)
# print(s2.average)





# Polymorphism
# Operator overloading

# print(1 + 2)
# print(type(1))
# # here 1 and 2 are objects of class int and in the int class, '+' operator is defined for its objects which adds the numerical value of the objects

# print("sam" + "king")
# print(type("sam"))
# # here "sam" and "king" are objects of class str and in the str class, '+' operator is defined for its objects which concatenates the two strings

# print([1,2,3] + [4,5,6])
# print(type([1,2,3]))
# here [1,2,3] and [4,5,6] are objects of class list and in the list class, '+' is defined for its objects which merges the two lists

# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(f"{self.real}i + {self.img}j")
    
# num1 = Complex(2,3)
# num1.showNumber()
# num2 = Complex(1,5)
# num2.showNumber()
# print(num1 + num2) # unsupported operand for complex


# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(f"{self.real}i + {self.img}j")

#     def add(self,num2):
#         newreal = self.real + num2.real
#         newimg = self.img + num2.img
#         return Complex(newreal, newimg)
    
# num1 = Complex(2,3)
# num1.showNumber()
# num2 = Complex(1,5)
# num2.showNumber()
# num3 = num1.add(num2)
# num3.showNumber()


# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     # def showNumber(self):
#     #     print(f"{self.real}i + {self.img}j")

#     def __str__(self):
#         return (f"{self.real}i + {self.img}j")

#     def __add__(self,num2): # __fun__ are called dunder functions
#         newreal = self.real + num2.real
#         newimg = self.img + num2.img
#         return Complex(newreal, newimg)
    
#     def __sub__(self,num2):
#         newreal = self.real - num2.real
#         newimg = self.img - num2.img
#         return Complex(newreal, newimg)
    
# num1 = Complex(2,3)
# print(num1)
# num2 = Complex(1,5)
# print(num2)
# print(num1 + num2)
# print(num1 - num2)