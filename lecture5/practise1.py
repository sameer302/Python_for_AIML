# Q1) print numbers from 1 to 100

# i = 1
# while i<= 100 : # stopping condition 
#     print(i)
#     i+=1



# Q2) print numbers from 100 to 1

# i = 100
# while i>=1 :
#     print(i)
#     i -= 1



# Q3) print the multiplication table of a number n.

# n = int(input("enter the number: "))
# i = 1
# while i<=10 :
#     print(n," * ",i," = ",n* i)
#     i += 1



# Q4) print the elements of the following list using a loop:

# [1,4,9,16,25,36,49,64,81,100]
# i = 0
# list = [1,4,9,16,25,36,49,64,81,100]
# while i<len(list) :
#     print(list[i])
#     i += 1



# Q5) Search for a number x in this tuple using loop

tup = (1,4,9,16,25,36,49,64,81,100,49)
i = 0
while i<len(tup): # traversing tuple
    if(tup[i] == 49):
        print("found at index",i)
        break
    i += 1