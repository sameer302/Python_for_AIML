# Q1) WAP to ask the user to enter names of their 3 favourite movies and store them in a list.

# print("enter names of your three favourite movies: ")
# movie1 = input("enter name of first movie: ")
# movie2 = input("enter name of second movie: ")
# movie3 = input("enter name of third movie: ")
# list = [movie1,movie2,movie3]
# print(list)

# Alternative to above code

# movies = []
# print("enter names of your three favourite movies: ")
# movie1 = input("enter name of first movie: ")
# movie2 = input("enter name of second movie: ")
# movie3 = input("enter name of third movie: ")
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)

# Alternative to above code

# movies = []
# movies.append(input("enter the name of first movie: "))
# movies.append(input("enter the name of second movie: "))
# movies.append(input("enter the name of third movie: "))
# print(movies)

# Q2) WAP to check if a list contains a palindrome of elements.

# list = [1, "sam", "sam", 3]
# list2 = list.copy()
# list2.reverse()
# if(list2 == list):
#     print("it's a palindrome!")
# else:
#     print("not a palindrome!")

# here the reason we use copy method instead of directly assigning one list to other is that when we assign one list to another then two references are 
# created for the same list and so if we do some changes using any reference then the original list is also changed. To avoid this we can use .copy method 
# to make a soft copy (or shallow copy) of our list. This way we can modify the soft copy without affecting the original list. 

'''difference between shallow copy and deep copy is that, when we make a shallow copy using .copy() method, firstly only the copy of outer list/references
is made while the inner objects remain the same so if I try to make any change in the inner objects that change will be reflected in the original 
list as well.
Instead if I make a deep copy by importing copy module and using copy.deepcopy() then copies of outer as well as inner references are made and so any 
changes made to inner objects won't reflect in the original list.
So as a summary elements in the list are actually references to objects.'''




# Q2) WAP to count the number of students with the "A" grade in the following tuple.
# ["C","D","A","B","B","A"]

# grades = ("C","D","A","A","B","B","A")
# print("number of students with A grade are: ", grades.count("A"))

# Q3) Store the above values in a list & sort them from "A" to "D".

# list = ["C","D","A","A","B","B","A"]
# list.sort()
# print(list)