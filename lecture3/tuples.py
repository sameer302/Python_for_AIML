# tuple holds immutable sequence of values while list holds mutable sequence of values
# tup = (1,2,3,6)
# print(type(tup))
# print(tup[0])
# print(tup[1])
# tup[0] = 5 # error : 'tuple' object does not support item assignment

# tup = ()
# print(type(tup))
# print(tup)

# tup = (1)
# print(tup)
# print(type(tup)) # here tup will be treated as an int variable

# tup = (1,)
# print(tup)
# print(type(tup)) # here tup will be treated as tuple

# hence for single element tuples we should always end it with ,
# for multiple elements adding , is optional
# this does not happen in case of lists as in case of tuples we are using () which is also generally used to enclose normal expressions in python. 
# But the [] are not generally used in python and we use them only when we want to make a list.

# slicing works same in tuple as in lists and string

# Methods in tuples

# tup = (1,4,2,6,8,2,3,2)
# print(tup.index(8))

# tup = (1,2,3,2,4,2,5,2)
# print(tup.count(2))
