

def add(n ,*num): # veriable list of arguments is passed
    print("Recieved Numbers = ", num)
    # print(type(num))
    # print(num[3])
    print("Addition == " , num[0] +num[1] + num[2] +num[3])
    addition = 0
    for i in range(0 , len(num)):
        addition = addition+num[i]


    print("For loop rzlt  == " ,  addition)
    # end of function



add(1,2,3,4,5)  # function call
