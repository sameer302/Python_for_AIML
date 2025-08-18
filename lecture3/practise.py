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

'''
🔑 Summary: Variable Assignment & Object Mutability in Python

**Immutable Objects** (e.g., `int`, `float`, `str`, `tuple`)
- **Assignment**: Creates a new reference to the same object.
- **Modification**: Triggers creation of a **new object**.
- **Effect**: Original variable remains unchanged.

```python
x = 5
y = x
y += 1  # y now points to a new object (6), x is still 5
```

---

**Mutable Objects** (e.g., `list`, `dict`, `set`)
- **Assignment**: Creates a new reference to the **same object**.
- **Modification**: Changes the object **in place**.
- **Effect**: All references reflect the change.

```python
a = [1, 2]
b = a
b.append(3)  # a is now [1, 2, 3] too
```

---

Best Practices
- Use `.copy()` or `copy.deepcopy()` to avoid unintended shared references with mutable objects.
- Use `id()` to inspect whether two variables point to the same object.

'''

'''difference between shallow copy and deep copy is that, when we make a shallow copy using .copy() method, firstly only the copy of outer list/references
is made while the inner objects remain the same so if I try to make any change in the inner objects that change will be reflected in the original 
list as well.
Instead if I make a deep copy by importing copy module and using copy.deepcopy() then copies of outer as well as inner references are made and so any 
changes made to inner objects won't reflect in the original list.
So as a summary elements in the list are actually references to objects.
'''

# import copy
# original = [1, [2, 3]]
# shallow = copy.copy(original)
# shallow.append(4)
# print(original)  # [1, [2, 3, 4]] → nested list is shared
# print(shallow)
# shallow[1].append(4)
# print(original)
# print(shallow)

# original = [1, [2, 3]]
# shallow = copy.deepcopy(original)
# shallow.append(4)
# print(original)  # [1, [2, 3, 4]] → nested list is shared
# print(shallow)
# shallow[1].append(4)
# print(original)
# print(shallow)


# Q2) WAP to count the number of students with the "A" grade in the following tuple.
# ["C","D","A","B","B","A"]

# grades = ("C","D","A","A","B","B","A")
# print("number of students with A grade are: ", grades.count("A"))

# Q3) Store the above values in a list & sort them from "A" to "D".

# list = list(grades)
# list.sort()
# print(list)

# Since tuples are immutable so they don't have sort or reverse method
