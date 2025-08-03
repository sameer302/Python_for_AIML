# Q1) search for a element in a tuple

tup = (1,3,2,5,4,6,2,3)
x = 2
i = 0
# for el in tup:
#     if(el == x):
#         print("found at index: ",i)
#     i+=1

for el in tup:
    if(el == x):
        print("found at index: ",i)
        break
    i+=1