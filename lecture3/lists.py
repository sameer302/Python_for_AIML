# marks = [94.4, 90.8, 87.5, 95.6]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[2])
# print(len(marks))

# list = []
# print(type(list))
# print(list)

# numbers = [1]
# print(numbers)
# print(type(numbers))



# list can store elements of different types like integers, float, string. etc.
# student = ["sameer", 99.9, 23, "Akola"]
# print(student)
# print("student name is:",student[0])



# list and string are similar but major difference is, strings are immutable but lists are mutable
# student = ["sameer", 99.9, 23, "Akola"]
# print(student)
# student[0] = "sam"
# print(student)
# print("student name is:",student[0])
# print(student[4]) # gives error list index out of range
# str = "sameer"
# print(str[6]) # gives error string index out of range



# list slicing similar to string slicing along with the concept of negative slicing

# difference between functions and methods is, functions are general purpose with respect to data type but methods are special functions 
# which can be applied only to a specific data type for example list methods or string methods, etc.




# List Methods

# modifying or updating list is also called as mutating list
# list = [1,2,3]
# print(list)
# print(list.append(4)) # here append method does not return anything or we can say it returns None value
# print(list) # original list is modified

# list = [4,2,5,7]
# list.sort() # here also sort method returns None value
# print(list) # original list is modified

# when we use string.capitalize(), the original string is not modified and instead a new string literal is created or we can say the capitalize() 
# method returns a new string literal and it is printed, but when we use list.sort() then the original list is sorted and the previous order of values 
# is lost and this method does not return anything

# by default sorting is ascending but for descending sorting,
# list = [8,3,5,9,1]
# list.sort(reverse=True)
# print(list)

# sorting is also applicable on list of strings or characters.
# list = ["z","f","y","q"]
# list.sort() # sorting in ascending order of unicode values
# print(list)

# sorting is not applicable when list contains strings and numbers both
# list = ["a","b",1,2]
# list.sort() # error : '<' not supported between instances of 'int' and 'str'
# print(list) 

# list = [1,2,3,4,5]
# list.reverse()
# print(list)

# list = [1,2,3]
# list.insert(1,5) # inserts 5 at index 1 and shifts other elements to right
# print(list)

# list = [1,2,3,1,2,1]
# list.remove(1) # removes first occurence of the entered element
# print(list)

# list = [1,2,3,4,5]
# list.pop(2) # removes element at the given index
# print(list)

# when we apply a method on any data type variable then either the method modifies the variable and returns None or it will create a new variable of the
# the same data type with the modifications and return this new variable without affecting the original variable. for e.g., string.capitalize() 
# or string.replace() will return a new string but list.append() will modify the original list

# we can go to official python documentation to look for more methods related to lists, strings or tuples
