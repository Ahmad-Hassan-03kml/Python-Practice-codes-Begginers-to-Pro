print("welcome to Python Era \n")

# glblvar="value"

# for i in range(1): # start of 

#     # here we will create a variable in local scope of for
#     lclvar=10
#     print(lclvar , "  Local var")
#     print(glblvar , " Global Var")



#     # end of for

x=100   # it is global varibale 
y=20
z=22

def func(  ):
    
     x = 200
     print(  "X == " , x  )
     print("total local variables  ==  " ,  len(locals()) ,"\n ",   locals() )

    

    # end of function

func() # function call of func

print(x)
print("total global variables  ==  " ,  len(globals()) ,"\n ",   globals() )

