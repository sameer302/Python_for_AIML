''' lists, tuples, dictionaries and sets are built in 
 classes in python '''

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
# print(info.items())
# both of the above methods print the same key value pairs but in different styles

# duplicate keys not allowed

# dictionary is unordered i.e. here we don't have indexing as in lists, string or tuple.
# So it means that we need to know the key value to access any element in dictionary.

# dictionary is mutable

''' we can have any immutable object as key but not mutable ones like lists or dictionary. 
for value, any object is allowed '''

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
# student = {
#     "name" : "sameer",
#     "subjects" : {
#         "PHI" : 100,
#         "Signals" : 100,
#         "Communication" : 110
#     },
#     "genius" : True
# }
# print(student)
# print(student["subjects"])
# print(student["subjects"]["PHI"])



# Methods in Dictionary

# print(student.keys()) # printed as dict_keys[]
# print(list(student.keys())) # printed as a list

# print(len(student))

# print(info.values()) # printed as dict_values[]
# print(list(info.values())) # printed as a list

# print(info.items()) # printed as dict_items and each element is a tuple of key and value separated by comma
# print(list(info.items())) # printed as list and again each element will be a tuple
# pairs = list(info.items())
# print(pairs[0]) # prints first key, value pair as a tuple

# print(info["name"])
# print(info.get("name"))

# print(student["name1"]) # throws error so gives unstable code
# print(student.get("name1")) # returns none so gives stable code


info.update({"name" : "jack"})
print(info)
new_dict = {"name" : "monalisa",
            "height" : "6 feet"}
info.update(new_dict) 
# update method will always take a dictionary as an input and then if there is any common key then its value gets updated as per the second dict,
# and if there is any new key : value pair, then it gets added to the first dict as it is.
print(info)
info["name"] = "charlie"
print(info)