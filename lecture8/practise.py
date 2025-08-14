'''
 Q1) Create student class that takes name and marks of 3 subjects as arguments in constructor.
 Then create a method to print the average
'''

# class Student:
#     def __init__(self, name, m1, m2, m3):
#         self.name = name
#         self.maths_marks = m1
#         self.science_marks = m2
#         self.english_marks = m3

#     def average(self):
#         avg = (self.maths_marks + self.science_marks + self.english_marks)/3
#         print(f"Hi {self.name} your average is: {avg}")
    
# S1 = Student("sam",99,99,99)
# S1.average()

# S1.name = "clark"
# S1.average()

##############################################################################

'''
Q2) Create Account class with 2 attributes - balance and account number.
Create methods for debit, credit and printing the balance
'''

# class Account:
#     def __init__(self,name,bal,acc_no):
#         self.name = name
#         self.balance = bal
#         self.account_number = acc_no

#     def debit(self, debit_amount):
#         self.balance -= debit_amount
#         print("Rs.", debit_amount ,"debited from your account")
#         self.print_balance()

#     def credit(self, credit_amount):
#         self.balance += credit_amount
#         print("Rs.", credit_amount ,"credited to your account")
#         self.print_balance()


#     def print_balance(self):
#         print("Your balance is:",self.balance)

# acc1 = Account("sam",100,1234)
# acc1.print_balance()
# acc1.debit(50)
# acc1.credit(60)