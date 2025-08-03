# range function returns a sequence of numbers, by default starting from
# zero and increments by 1 and stops before a specified number
# syntax, range(start?, stop, step?)
# ? implies that these are optional but stopping value is must

# seq = range(5) # values from 0 to 4 stored in seq
# print(seq)
# i=0
# while i<=4:
#     print(seq[i])
#     i+=1

# for i in range(10): # range(stop)
#     print(i)

# for i in range(3,10): # range(start, stop)
#     print(i)

# for i in range(3,10,2): # range(start, stop, step)
#     print(i)

# Q1) print all even numbers from 1 to 10
# for i in range(2,11,2):
#     print(i)

# Q2) print all odd numbers from 1 to 10
for i in range(1,10,2):
    print(i)