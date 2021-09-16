print("welcome to python \n ")

# name = input("Enter Your Name:") # my name
# age =input("Enter Your Age:") # 22
# print(f"name is {name}  and type is {type(name)}")
# print(f"age is {age}  and type is  {type(age)}")

n1=input("Enter number One in float): ")
n1=float(n1)

n2=float(input("Enter Number Two float: "))

print(f"NUmber one == {n1}  Type == {type(n1)}")
print(f"NUmber two == {n2}  Type == {type(n2)}")

print(f"Addition ===  {n1+n2}") # 20





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

