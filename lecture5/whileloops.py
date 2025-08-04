# while loop

# count = 1
# while count<=5:
#     print("hello",count)
#     count += 1 # no special increment operator in python like x++
# print("end of loop")



# break and continue

i = 0
x = 19
y = 7
list = [2,3,5,7,11,13,17,19,23,29]
while i<=10:
    if(list[i] == y):
        i+=1
        continue
    if(list[i]==x):
        break
    print(list[i])
    i+=1
# 32:35