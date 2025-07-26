str = "apple"
print(str[-5:-2])
print(str[-5:]) # here we can't write str[-5:0] or str[-5:len(str)]
print(str[:-1]) 
print(str[-len(str):-1])