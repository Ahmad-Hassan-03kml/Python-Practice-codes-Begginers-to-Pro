print(" \n welcome to Python")
# n1 =int(input("entr number one: "))

# n2 =int(input("enter number two: "))

# if(n1>n2): # true
#     print(f"n1 {n1} is greter then n2 {n2}")
#     #nested if
#     if(n1%2==0):
#         print("n1 is even ")
#     #end of nested if


#     if(n1%2 != 0):
#         print("n1 is odd")

#         #end of nested if
    
    
# if(n2>n1): # flase
#     print(f"n2 {n2} is gretaer then n1 {n1}")
#     #nested if
#     if(n2%2==0):
#         print("n2 is even ")
#     #end of nested if


#     if(n2%2 != 0):
#         print("n2 is odd")

#     #end of next if



        # if else part 
# num1=201
# num2=100

# if(num1 > num2): # false
#         print("num1 is greater")

#         if(num1%2==0):
#                 print("num1 is even")
#         else:
#                 print("numn1 is odd")
#         # end of if
# else: # trues
#         print("num1 in not greater")
        # end of else

# apply on num2 
# if(num2 > num1):# false
#         print("num2 is greater")
#         # end of if
# else:
#         print("num2 is ot greater")




# short hand if else
# print("num1 is greater then num2 ") if(num1 > num2) else print("num2 is greater then num1")

marks=95

id = 30020

if(marks >=50 and  marks <60):
        print("your are passed with D")
        # end of condition
elif(marks >= 60 and marks < 70):
        print("your are passed with C")
elif(marks >=70  and marks < 80):
        print("your are passed with B")
elif(marks >= 80 and marks <90):
        print("your are passed with A")
elif(marks >=90 and marks <=100):
        print("your are passed with A+")
        if(id==3001):
                print("Id == 3001")
        elif(id==3002):
                print("id == 3002")
        else:
                print("unknown ID")
elif(marks < 50):
        print("your are Failed")
else:
        print("sorry you have entered wrong marks")

























