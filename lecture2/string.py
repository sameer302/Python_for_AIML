# str1 = 'sam'
# str2 = "sam"
# str3 = '''sam'''
# # why three different representations ?
# reason = "apostrophe, that's it!"
# str = ""
# print(type(str))
# print(str)

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
# print(finalstr) # no space between both the strings

# length function
# str1 = "sam"
# len1 = len(str1)
# print(len1)
# str2 = "cool"
# str3 = str1 + " " + str2
# print(len(str3))
# empty space is also a character so it increases length of string

# indexing
# we can only access characters of a string using indexing but not modify them
# str = "sameer king"
# firstchar = str[-1]
# print(firstchar)
# str[1] = "u"  # error printed
# print(str)
# empty space is also a character

# # slicing
# str = "sameer"
# print(str[0:3])
# print(str[3:6])
# print(str[5:2]) # no output printed
# str2 = "superstar"
# print(str2[5:len(str2)])
# print(str2[5:]) # equivalent to str2[5:len(str2)]
# print(str2[:5]) # equivalent to str2[0:5]
# print(str2[:]) # equivalent to str2

# negative slicing
# str = "apple"
# print(str[-5:-2])
# print(str[-5:]) # here we can't write str[-5:0] or str[-5:len(str)]
# print(str[:-1]) # last character won't be printed
# print(str[-len(str):-1]) # last character won't be printed

# # string functions
# str = "i am sameer"
# print(str.endswith("er")) # prints True
# print(str.endswith("er ")) # prints False

# str = "i am a good boy"
# print(str.capitalize()) # capitalizes only first character
# print(str) # these functions create a new string and not modify the original string
# strings are immutable
# str = str.capitalize()
# print(str)

# str = "hai apna dil toh awara"
# print(str.replace("a","o"))
# print(str) # original string not modified
# print(str.replace("apna","tera"))

# str = "toota toota ek parinda aise toota"
# print(str.find("ek")) # prints index of first character of the string we are looking for 
# print(str.find("q")) # -1 will be printed but it does not mean negative index

# str = "taare zameen par"
# print(str.count("a"))
# print(str.count("zameen"))
