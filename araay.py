from array import *

length = int(input("Enter the length of Array ::  "))

arr=array('i'  , []) # here ia empty array is initialized 

for i in range(length):

    arr.append( int(input("entre array value : "))  )
    # end of for 


for j in range(0,length):
    print("value  ", j+1 , "th is  ==>> " , arr[j])
    # end of for 


# arr1 = array( 'i'  , [1,2,33,44,55])

# for i in arr1:
#     print(i)
