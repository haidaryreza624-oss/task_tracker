import sys
import crud
vector = sys.argv

def ask_int(msg,lst):
    while True:
        value = input(msg)
        if value in lst:
            return int(value)
            
def ask_str(msg):
    while True:
        value = input(msg)
        if len(value.strip()) > 0:
            return value

operations = ["add","update","delete","list","mark"]
try:
    
    operation = vector[1]
    
    if operation not in operations:
        raise TypeError()
    
    if operation == "add":
        title = ""
        mark_done = ""
        if len(vector)>2:
            title = ' '.join(vector[2:])
            mark_done = 0
        else:
            title = ask_str("Enter the Title: ")
            mark_done = ask_int("(0) for default (1) for in progress: ",["0","1"])

            
        
        crud.add(title,mark_done)
    
    elif operation == "update":
        title = ""
        id = 0
        if len(vector) > 2:
            id = vector[2]
            if len(vector) > 3:
                title = vector[3]
        else:
            id = ask_int("Enter Id to Update: ",[str(x) for x in range(0,1000)])
            title = ask_str("Enter New Title: ")
        
        if len(title.strip()) <= 0:
            title = ask_str("Etner The New Title: ")
        crud.update(id,"task",title)
        

                    

            
            
            
            


    

except Exception as e:
    print(e)
    # for i in operations:
    #     print(i)

