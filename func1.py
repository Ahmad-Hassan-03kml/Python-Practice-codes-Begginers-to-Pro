
print("welcome to python \n")

# def funcName():
#     # print("str message")
#     return "pakistan is my beloved land"
#     #end of function



# # var1 = funcName() # function call
# print(funcName())



# def add():
#     n1= int(input("ENter number one:  "))
#     n2=int(input("ENter number two:  "))

#     # print("addition === {}".format(n1+n2) ) #30
#     return n1+n2


# # addition= add() #40
# print("Addition == > " , add())



def funcAdd(p1 , p2 ):
    print("parameter one  == {}".format(p1))
    print("parameter two  == {}".format(p2))
    print("addition ==   " ,p1+p2 )
    return p1+p2
    # end of functio
    

def funcSub(p1 , p2 ):
    print("parameter one  == {}".format(p1))
    print("parameter two  == {}".format(p2))
    print("Subtraction ==   " ,p1-p2 )
    return p1-p2
    # end of functio




p1 = int(input("ENter number one:  "))
p2 = int(input("ENter number two:  "))
# add=funcAdd(p1 , p2 )
# print("add === ", add)
print(funcSub(p1,p2))
print(funcSub(100 , 50))

