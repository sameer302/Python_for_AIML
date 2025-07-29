# tuple holds immutable sequence of values while list holds mutable sequence of values
# tup = (1,2,3,6)
# print(type(tup))
# print(tup[0])
# print(tup[1])
# tup[0] = 5 # error : 'tuple' object does not support item assignment

# tup = ()
# print(type(tup)) # output will be <class 'tuple'>
# print(tup) # output will be ()

# tup = (1)
# print(tup) #output will be 1
# print(type(tup)) # output will be <class 'int'>

# tup = (1,)
# print(tup) # output will be (1,)
# print(type(tup)) # output will be <class 'tuple'>

# hence for single element tuples we should always end it with ,
# for multiple elements adding , is optional
# this does not happen in case of lists as in case of tuples we are using () which is also generally used to enclose normal expressions in python. 
# But the [] are not generally used in python and we use them only when we want to make a list.

# slicing works same in tuple as in lists and string

# Methods in tuples

# tup = (1,4,2,6,8,2,3,2,8)
# print(tup.index(8)) # returns index of the first occurence of the element

# tup = (1,2,3,2,4,2,5,2)
# print(tup.count(2))
