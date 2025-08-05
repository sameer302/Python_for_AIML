# Q1) Write a recursive function to calculate the sum of first n natural numbers

# def sum_upto(n):
#     if(n==0):
#         return 0
#     return n + sum_upto(n-1)

# print(sum_upto(10))

#########################################################################

# Q2) Write a recursive function to print all elements in a list
# Hint : use list and index as parameters

# def print_elements(list, idx=0):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_elements(list,idx+1)

# digits = [1,2,3,4,5]
# print_elements(digits)