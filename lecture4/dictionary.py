# lists, tuples, dictionaries and sets are built in data structures in python

info = {
    "name" : "sameer",
    "subjects" : ["physiology","PHI","Communictions"],
    "topics" : ("dictionary","set"),
    "age" : 23,
    "is_adult" : True,
    10 : 96.6
}
print(type(info))
print(info)

# duplicate keys not allowed
# dictionary is unordered i.e. here we don't have indexing as in lists, string or tuple.
# dictionary is mutable
# we can have any immutable data type or structure as key but not mutable ones like lists or dictionary.
# for value, any data type and structure is allowed 

print(info["name"])
print(info["subjects"])
print(info[10])
print()