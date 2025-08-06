# block of statements that perform a specific task.
# repeating or redundant block of code can be made into a function

# def calcSum(a,b): # a,b are parameters
#     sum = a+b
#     print(sum)
# the above block of code is called function definition
# calcSum(7,8) # 7,8 are arguments and this is function calling

# even if we don't write return statement or just write return, in both cases it will return none

# def calcMul(c,d):
#     mul = c*d
#     return mul

# result = calcMul(4,9)
# print(result)

# def print_hello(): # function may or may not have any parameters
#     print("hello") # function may or may not return any value

# print_hello()
# output = print_hello()
# print(output) # function that does not return anything, returns None

# Q1) Make a function to find average of three numbers

# def avg_three(a,b,c):
#     avg = (a+b+c)/3
#     return avg

# print(avg_three(2,3,4))

# types of functions:
# 1) Built-in functions - print(), type(), len(), range()
# 2) User defined functions

# print("sameer","nilkhan", sep="$", end=" ")
# print("king")

# default parameters
# def calcMul(a,b):
#     print(a*b)
    
# calcMul() # error missing arguments

# def calcMul(a=1,b=2):
#     print(a*b)

# calcMul(4,7)
# calcMul()

# def calcMul(a,b=2):
#     print(a*b)

# calcMul(4,7)
# # calcMul() # error missing arguments
# calcMul(5)

# def calcMul(a=1,b): # here it will throw error since non-default first default later
#     print(a*b)
