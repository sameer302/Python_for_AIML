# collection = {1,2,2,3,"akkad","bakkad","bambe","bo","bo"}

# print(collection) # every time we print the order may change
# sets are unordered collection of unique elements
# duplicate elements are ignored while printing and even while counting
# print(len(collection))

# set can contain only immutable elements, this is necessary because lets say we created a list first and then added it as an element in set, 
# then we might think that anyways we can't access this list element so we will not be able to modify it and so it will follow the property of sets,
# but we can update the list outside the set where we first defined it and so this may create a problem with the functioning of the dictionary.

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
                        value : mutable     mutable
    set                 immutable           mutable
'''
'''
when we say a data structure is mutable it means we can add 
or remove elements from that DS.
and when we say elements of a DS are mutable it means we can
modify the element at a particular location.
'''

# Set Methods

# collection = set()
# collection.add(1)
# collection.add("sam")
# collection.add((1,2,3))
# collection.add(12.34)
# print(collection)
# collection.add([1,2,3]) # error: unhashable type: 'list'
# collection.add({1,2,3}) # error: unhashable type: 'set'

'''
hashable elements = immutable elements e.g., string, tuple
unhashable elements = mutable elements e.g., list, set, dictionary
'''
# collection = {12.34, 12.34, "sameer",55}
# collection.remove(12.34) # removes all instances of 12.34
# print(collection)

# collection.clear() # removes all elements from the set
# print(collection)
# print(len(collection))

# print(collection.pop()) # returns random element from the set

# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.union(set2)) # just like union of sets in maths, it does not modify the original sets but returns a new set
# print(set1) # no change
# print(set2) # no change
# print(set1.intersection(set2)) # just like intersection in maths, does not modfiy any set but returns a new set