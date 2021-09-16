"""In this video we will disuss about tuple in python """
# list1=[1,2,3,"str1"]  #list is muatable able to change
# print(list1)

# list1[1]=200 # new value  assigend to list1 at 2 nd index
# list1.append("new value at last index")

# print(list1)
tpl1=(1,2,3.3,"four" ,True)
print(tpl1)

# tpl1[1]="new value"
# print(tpl1)

print(tpl1[-3:-1])

print(tpl1*5)

tpl2=(111,222,333,444)
newtpl=tpl1+tpl2
print("\n\n   new tuple  \n\n" , newtpl)
