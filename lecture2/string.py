# str1 = 'sam'
# str2 = "sam"
# str3 = '''sam'''
# # why three different representations ?
# reason = "apostrophe, that's it!"

# # escape sequence characters - used for formatting text - e.g. tab, new line, carriage return, etc.
# str = "let's try escape sequence\nright now!"
# print(str)
# str2 = "let's try escape sequence\tright now!"
# print(str4)

# #concatenation
# str1 = "sameer"
# str2 = "single"
# print(str1+str2)
# finalstr = str1 + str2
# print(finalstr)

# # length function
# str1 = "sam"
# len1 = len(str1)
# print(len1)
# str2 = "cool"
# str3 = str1 + " " + str2
# print(len(str3))

# # indexing
# # we can only access characters of a string using indexing but not modify them
# str = "sameer king"
# firstchar = str[0]
# print(firstchar)
# str[1] = "u"
# print(str) # error printed
# empty space is also a character

# # slicing
# str = "sameer"
# print(str[0:3])
# print(str[3:6])
# str2 = "superstar"
# print(str2[5:len(str2)])
# print(str2[5:]) # equivalent to str2[5:len(str2)]
# print(str2[:5]) # equivalent to str2[0:5]

# # negative slicing
# str = "apple"
# print(str[-5:-2])
# print(str[-5:]) # here we can't write str[-5:0] or str[-5:len(str)]
# print(str[:-1]) 
# print(str[-len(str):-1])
# print(str[:]) # equivalent to str
# negative indexing works only for slicing and not in general

# # string functions
# str = "i am sameer"
# print(str.endswith("er"))
# print(str.endswith("er "))

# str = "i am a good boy"
# print(str.capitalize())
# print(str) # these functions create a new string and not modify the original string
# str = str.capitalize()
# print(str)

# str = "hai apna dil toh awara"
# print(str.replace("a","o"))
# print(str.replace("apna","tera"))

# str = "toota toota ek parinda aise toota"
# print(str.find("ek"))
# print(str.find("q")) # -1 will be printed as negative indexing works only for slicing

# str = "taare zameen par"
# print(str.count("a"))
# print(str.count("zameen"))

