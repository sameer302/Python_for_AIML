''' lists, tuples, dictionaries and sets are built in 
 data structures in python '''

# dictionary is collection of key value pairs

info = {
    "name" : "sameer",
    "subjects" : ["physiology","PHI","Communictions"],
    "topics" : ("dictionary","set"),
    "age" : 23,
    "is_adult" : True,
    10 : 96.6
}
# print(type(info))
# print(info)

# duplicate keys not allowed

# dictionary is unordered i.e. here we don't have indexing as in lists, string or tuple.

# dictionary is mutable

''' we can have any immutable data type or structure as key but not mutable ones like lists or dictionary. 
for value, any data type and structure is allowed '''

# print(info["name"])
# print(info["subjects"])
# print(info[10])
# print(info["surname"]) # error displayed

# info["name"] = "sam" # to modify existing key's value
# info["surname"] = "nilkhan" # to add a new key value pair
# print(info)

# null_dict = {}
# print(type(null_dict))
# null_dict["name"] = "james bond"
# print(null_dict)

# Nesting in dictionary
student = {
    "name" : "sameer",
    "subjects" : {
        "PHI" : 100,
        "Signals" : 100,
        "Communication" : 110
    },
    "genius" : True
}
# print(student)
# print(student["subjects"])
# print(student["subjects"]["PHI"])



# Methods in Dictionary

# print(student.keys()) # printed as dict_keys[]
# print(list(student.keys())) # printed as a list

# print(len(student))

# print(student.values()) # printed as dict_values[]
# print(list(student.values())) # printed as a list

# print(student.items())
# print(list(student.items()))
# pairs = list(student.items())
# print(pairs[0])

# print(student["name"])
# print(student.get("name"))

# print(student["name1"]) # throws error so gives unstable code
# print(student.get("name1")) # returns none so gives stable code

# student.update({"name" : "jack"})
# print(student)
# new_dict = {"name" : "monalisa"}
# student.update(new_dict)
# print(student)
