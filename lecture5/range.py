# range function returns a sequence of numbers, by default starting from
# zero and increments by 1 and stops before a specified number
# syntax, range(start?, stop, step?)
# ? implies that these are optional but stopping value is must

# seq = range(5) # values from 0 to 4 stored in seq
# print(type(seq)) # class 'range'
# print(seq) # range(0,5) printed


# i=0
# while i<=4:
#     print(seq[i])
#     i+=1

# for i in range(10): # range(stop)
#     print(i) # prints from 0 to 9

# for i in range(3,10): # range(start, stop)
#     print(i) # prints from 3 to 9

# for i in range(3,10,2): # range(start, stop, step)
#     print(i) # prints 3,5,7,9

# Q1) print all even numbers from 1 to 10
# for i in range(2,11,2):
#     print(i)

# Q2) print all odd numbers from 1 to 10
# for i in range(1,10,2):
#     print(i)