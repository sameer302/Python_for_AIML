# syntax = right way to write a code
# by default in vs code tab = 4spaces, useful for indentation
# age = 17
# if(age >= 18):
#     print("can vote and drive")
#     print("can marry")
# else:
#     print("can't marry")



# if(True):
#     print("amar hai hum")



# light = "green"
# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("look")
# else:
#     print("light is broken")

# print("end of code")

# we should have at least one if at the starting before using elif
# above we can also use if instead of all elif but the difference between both is that, in case of if, the condition will always be checked while in case of elif, the condition is checked only if the previous if or elif condition was false.
# else condition should always be at the last and can be used only once while if and elif can be used any number of times.



# marks = int(input("enter students marks : "))
# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80):
#     grade = "B"
# elif(marks >= 70 and marks < 80):
#     grade = "C"
# else:
#     grade = "D"

# print("grade of the student ->", grade)



# nesting of conditional statements
marks = 40
if(marks >= 50):
    if(marks >= 100):
        print("invalid marks")
    else:
        print("passed")
else:
    print("fail")

