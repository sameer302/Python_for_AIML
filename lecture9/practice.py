'''
Q1) Define a Circle clas...
'''
# import math

# class Circle:
#     def __init__(self, rad):
#         self.rad = rad

#     def Area(self):
#         area = math.pi * (self.rad**2)
#         return area
    
#     def Perimeter(self):
#         perimeter = 2 * math.pi * self.rad
#         return perimeter
    
# cir1 = Circle(5)
# print(cir1.Area())
# print(cir1.Perimeter())

#########################################################################

'''
Q2) Define a Employee class with attributes role....
'''

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print(f"role:{self.role}\ndept:{self.dept}\nsalary:{self.salary}")

emp1 = Employee("intern","research","12lpa")
emp1.showDetails()

class Engineer(Employee):
    def __init__(self,name,age):
        # super().__init__("Engineer","IT","30lpa")
        self.name = name
        self.age = age

engg1 = Engineer("sam",23)
engg1.showDetails() # engg1 is an object of both classes, Employee and Engineer

#####################################################################

'''
Q3) Create a class called order...
'''

# class Order:
#     def __init__(self,item,price):
#         self.item = item
#         self.price = price

#     def __gt__(self, order2):
#         return self.price > order2.price
        
# ord1 = Order("vadapav",25)
# ord2 = Order("pavbhaji",75)
# print(ord1 > ord2)