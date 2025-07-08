''' two types:
1) Type conversion - implicit done by interpreter itself
2) Type casting - explicit done manually by programmer
'''
a = 2
b = 2.5
print(a+b) # a is implicitly typecasted to 2.0

c = "5"
d = 5
# print(c + d) # c is not implicitly typecasted to int and hence error occurs
print(int(c) + d) # explicit type casting

e = "sam"
f = 6
# print(int(e) + f) # type casting works only if data is logically convertible

g = 123
h = str(g)
print(type(h))