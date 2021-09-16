

def std(** students):
    
    for i in students.keys():
        print(i , " :  " , students[i])
        
        

    #end of std 

std(std1="name 1" , std2="name 2" ,std3="name 3"  )

#                   or
stdInfo={"std1":"stdName1" ,"std2":"stdName2" ,"std3":"stdName3"  }
std(**stdInfo)
