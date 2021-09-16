
num1=200
num2=20
# if(num1 > num2): # true
#     print("num1 is greater0")
#     #end of if
# if(num2 > num1): # false
#     print("num2 is greater")
#     #end of if
# else: # false
#     print("both are equals")


# def func():
#     print("function is called")

# func()

# print("total global variables  ==>  ",len(globals()) , "\n")

# d = dict(globals())  

# print(d["keys"])


# print(" Keys    :   values"   )

# for i in d:
#     print(i ,"    :    " , d[i])



# print(num1)
# print("out put of  __doc__ \n" )
# print(num1.)

# print( )

num1=10

# x,y=1
# # ternary operator
# print("i am first string list") if(num1==110) else print("i am second strign")

# x=0 if(num1 == 0) else y=0
# print(x)
# print(y)


# how return works in function

# def func(x):
#     print("line befor return ")
#     if(x==4):
#         return 0
#     else:
#         print("line after return")

# print(func(5))


# here we will get input WindowsError
def intIn(prmsg , errmsg=None): # by default value is None of errmsg or set by method call
    while True:
        try:

            return int(input(prmsg))
            # code which can make a mistake 
            #end of try 
        except ValueError:
            if(errmsg is not None):

                print(errmsg)
                # end of if
            #end of value error

        #end of while true
    # end of intIn


# now we can take input on the behalf of argument placed in intIn()
# agr sirf msg pass krenge to 
number = intIn("Enter Valid Integer Number: "  , "Not Valid Entry of Integer Input")

