# Recursion is when function calls itself repeatedly
# loops and recursion are interconvertible
# in some cases recursion gives a simple code as compared to loops

# recursive function
# def show(n):
#     if(n==0): # base case, present in every recursive function
#         return
#     print(n)
#     show(n-1)
#     print("end",n)

# show(5) 

# infinite loop will keep working infinitely but infinite recursion will stop 
# after stack is full also called as stack overflow

# recursion is applicable wherever we have recurrence relation

# fact(n) = fact(n-1)*n

def fact(n):
    if(n==0 or n==1):
        return 1
    return n * fact(n-1)
    
print(fact(5))