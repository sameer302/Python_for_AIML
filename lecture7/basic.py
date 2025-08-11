## opening a file

# two types of files to open, text and binary, by default its text
# so just writing "r" works in place of "rt" but for binary we need to write 
# as "rb" or "wb" depending on what we want to do

# f = open("demo.txt") 
# # by default its read
# if not in the same folder then we need to mention the complete path of the file that we want to open

# f = open("demo.txt","r") 


# f = open("demo.txt","rt")

## reading the file

# data = f.read()
# print(data)
# print(type(data))

# data1 = f.read()
# print(data1) # nothing will be printed as cursor it at the end
# print(type(data1))

# import os
# print(os.getcwd()) 

# data = f.read(10) # read only first 10 characters
# print(data)


# line1 = f.readline()
# print(line1)
'''we will get extra line after line1 is printed this is because in the text file
as we pressed enter to write in next line so by default there a newline character \n 
is added which is not directly visible but it is present and also read hence we get
a new line'''

# line2 = f.readline()
# print(line2)

# line3 = f.readline()
# print(line3)

# line4 = f.readline()
# print(line4)
'''so once we have read all the lines, after that if we try to use readline()
it will print empty line as there is nothing to read similarly if we try to use readline() after using read()
then also only empty lines will be printed, its just like the cursor is moved and wherever
the cursor is currently from there the printing starts. If we want to use readline()
after using read() then we need to close the file and open it again'''

# f.close()

# f = open("demo.txt","w")
# print(f.read()) # will give error as file is not opened in read mode
# f.write("D") # even if we write a single character and there are many characters already in the file, then also firstly complete data will
# be removed and then the new data will be written

# f = open("demo.txt","a")
# print(f.read()) # will give error as file is not opened in read mode
# f.write(" Ab nahi udega!:)")
# f.write("\nnext line me likhega ab")

# f = open("sample.txt","r") # error: file not found

# f = open("sample1.txt","w") # this creates a new file if not present already
# f = open("sample2.txt","a") # this creates a new file if not present already


# f = open("demo.txt","r+") # combined mode, both read and write
# f.write("A ") # here the pointer starts from the first character and then it updates the data
# # sequentially without overwriting the complete file as "w"
# print(f.read()) # the printing will start from where the pointer is present currently i.e. where the last character was written

# f = open("demo.txt","w+") # this is also combined mode both read and write, opens the file in truncated form i.e. all data is wiped up
# print(f.read()) # empty line is printed
# f.write("abc") # abc is written
# print(f.read()) # nothing is printed as now the pointer is at the end
# f.seek(0) # brings the pointer back to the begining of file
# print(f.read()) # now abc is printed

# f = open("demo.txt","a+") # combined mode both read and append
# print(f.read()) # nothing printed as pointer is at the end
# f.write(" abc") # abc appended at the end
# print(f.read()) # nothing is printed as pointer is at the end
# f.seek(0)
# print(f.read())

# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data) # here we don't need to close the file stream as with does that by default

# with open("demo.txt","w") as f:
#     f.write("jugrafiya")
#     print(f.read()) # error as we opened file in write mode

# import os
# os.remove("sample1.txt")

# f = open("sample.txt","w")
# f.close()

# import os
# os.remove("sample.txt") # cross aayega filename pe
# we can remove a file only if it is closed but if its open then we cannot close it.

# f.close()