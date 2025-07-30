'''
Q1) Store following word meanings in a python dictionary
table : "a piece of furniture","list of facts and figures"
cat : "a small animal"
'''
# dict = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture","list of facts and figures"]
# }
# print(dict)

'''
Q2) You are given a list of subjects for students. Assume one 
classroom is required for 1 subject. How many classrooms are 
needed by all students.
"python", "java", "C++", "python", "javascript", "java", "python", 
"java", "C++", "C"
'''
# set = {"python", "java", "C++", "python", "javascript", "java", "python", 
# "java", "C++", "C"}
# print(len(set))

'''
Q3) WAP to enter marks of 3 subjects from the user and store them 
in a dictionary. Start with an empty dictionary and add one by one.
Use subject name as key and marks as value.
'''
# dict = {}
# dict["phy"] = int(input("enter marks of physics: "))
# dict["chem"] = int(input("enter marks of chemistry: "))
# dict["maths"] = int(input("enter marks of mathematics: "))
# print(dict)

# alternative to above

# marks = {}
# marks.update({"phy" : input("enter marks of physics: ")})
# marks.update({"chem" : input("enter marks of chemistry: ")})
# marks.update({"maths" : input("enter marks of mathematics: ")})
# print(marks)

'''
Q4) Figure out a way to store 9 and 9.0 as separate values in the set
(you can take help of built-in data types)
'''
# set = {9,9.0}
# print(set) # only 9 is printed

# 9 and 9.0 get same hash value in python

# solution 1)
# set = {9, "9.0"}
# print(set)

# solution 2)
set = {
    ("float",9.0),
    ("int",9)
}
print(set)