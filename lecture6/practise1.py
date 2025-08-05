# Q1) WAF to print the length of a list(list is the paramenter).

# def print_length(list):
#     print(len(list))

# marks = [99,98,95]
# print_length(marks)

############################################################################

# int = 5
# print(int)

# list, int, float, etc are not keywords in python but they are classes.
# they can be used as identifiers
# keywords like if, def, while, can't be used as identifiers

# import keyword
# print(keyword.kwlist)

############################################################################

# Q2) WAF to print the elements of a list in a single line.(list is the parameter)

# def print_elements(list):
#     for el in list:
#         print(el,end=" ")

# name = ["sam","jack","cash","vash"]
# print_elements(name)

################################################################################

# Q3) WAF to find the factorial of n(n is the parameter)

# def calc_factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     print(fact)

# n = int(input("enter the number: "))
# calc_factorial(n)

############################################################################

# Q4) WAF to convert USD to INR

# def convert_to_INR(usd_value):
#     inr_value = usd_value*83
#     print(usd_value,"USD =",inr_value,"INR")

# convert_to_INR(70)

###########################################################################

# Q5) WAF to print odd or even

def odd_or_even(num):
    if(num%2==0):
        print("EVEN")
    else:
        print("ODD")

odd_or_even(26)