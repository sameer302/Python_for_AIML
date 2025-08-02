# collection = {1,2,2,3,"akkad","bakkad","bambe","bo","bo"}

# print(collection) # every time we print the order may change
# sets are unordered collection of unique elements
# duplicate elements are ignored while printing and even while counting
# print(len(collection))

# set can contain only immutable elements

# collection = {} # empty dictionary
# print(type(collection))
# collection = set() # empty set
# print(type(collection))

# set is mutable but the elements of the set are immutable
'''
    data structure      elements            self
    string              immutable           immutable
    list                mutable             mutable
    tuple               immutable           immutable
    dictionary          key : immutable     mutable
    dictionary          value : mutable     mutable
    set                 immutable           mutable
'''
'''
when we say a data structure is mutable it means we can add 
or remove elements from that DS.
and when we say elements of a DS are mutable it means we can
modify the element at a particular index.
'''

# Set Methods

# collection = set()
# collection.add(1)
# collection.add("sam")
# collection.add((1,2,3))
# collection.add(12.34)
# print(collection)
# collection.add([1,2,3]) # error: unhashable type: 'list'

'''
hashable elements = immutable elements e.g., string, tuple
unhashable elements = mutable elements e.g., list, set, dictionary
'''
collection = {12.34, 12.34, "sameer",55}
# collection.remove(12.34) # removes all instances of 12.34
# print(collection)

# collection.clear()
# print(collection)
# print(len(collection))

# print(collection.pop())
# print(collection.pop()) # returns random values

# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.union(set2)) # just like union of sets in maths
# print(set1) # no change
# print(set2) # no change
# print(set1.intersection(set2)) # just like intersection in maths