# Q1) Create a new file...

# f = open("practise.txt","w")
# f.write("Hi everyone")
# f.write(" Bye everyone") # this will be appended at end of Hi everyone
# f.write("\nWe are learning File I/O\nusing Java.\nI like programming in Java.")
# f.close()

##########################################################################

# Q2) WAF that replaces all occurences of "java" with "python" in above file.

# def replace(word1, word2):
#     with open("practise.txt","r") as f:
#         data = f.read()

#     data = data.replace(word1,word2)

#     with open("practise.txt","w") as f:
#         f.write(data)

# replace("Java", "Python")

#######################################################################

# Q3) Search if the word "learning" exists in the file or not.

# word = "learning"
# with open("practise.txt","r") as f:
#     data = f.read()

# if(word in data): # alternate to use string.find()
#     print("exists")
# else:
#     print("does not exist")

#######################################################################

# Q4) WAF to find in which line of the code does the word "learning" occur first. Print -1 if word not found.

# word = "learning"
# def find_line():
#     with open("practise.txt","r") as f:
#         line = True
#         i = 1
#         while line : # condition is false only when line becomes null, value is truthy and empty is falsy in python
#             line = f.readline()
#             if(word in line):
#                 print(i)
#                 return
#             i += 1
#     print("-1")

# find_line()

############################################################################

# Q5) From a file containing numbers separated by comma, print the count of even numbers

with open("numbers.txt","r") as f:
    data = f.read()

# num = ""
# count = 0
# for char in data:
#     if(char == ","):
#         if(int(num)%2 == 0): # here even though num will contain some empty space still it can be converted to int
#             count += 1
#         num = ""
#     else:
#         num += char

# if(int(num)%2 == 0): # this is because last number won't be covered in above loop
#     count += 1

# print(count)

# alternate code

# count = 0
# nums = data.split(",") # it will take it as a list of strings
# print(nums)
# for val in nums:
#     if(int(val) % 2 == 0):
#         count += 1

# print(count)

# str = " 23 "
# print(int(str)) # here space character won't make any problem but any other character will make a problem

# str = "2a"
# print(int(str)) # error invalid literal for int