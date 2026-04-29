import sys
import crud
vector = sys.argv
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
            istitlValid = True
            
            while istitlValid:
                
                title = str(input("The Task Title: "))
                if len(title.strip()) > 0:
                    istitlValid = False
                while True and mark_done not in ["0","1"]:
                    mark_done = str(input("(1) for in progress and (0) for not in progress: "))
                    if mark_done in ["0", "1"]:
                        break

            mark_done = int(mark_done)
        
        crud.add(title,mark_done)
    

except:
    print("Error")
    # for i in operations:
    #     print(i)

