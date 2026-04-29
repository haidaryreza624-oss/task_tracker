import sys
import crud
import json
vector = sys.argv

with open('data.json',"r")as f:
    a = json.load(f)
    b =     len(a["used_ids"])
    

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
    
    if operation.lower() not in operations:
        raise TypeError()
    
    if operation.lower() == "add":
        title = ""
        mark_done = ""
        if len(vector)>2:
            title = ' '.join(vector[2:])
            mark_done = 0
        else:
            title = ask_str("Enter the Title: ")
            mark_done = ask_int("(0) for default (1) for in progress: ",["0","1"])

            
        
        crud.add(title,mark_done)
    
    elif operation.lower() == "update":
        title = ""
        id = 0
        if len(vector) > 2:
            id = vector[2]
            if len(vector) > 3:
                title = vector[3]
        else:
            id = ask_int("Enter Id to Update: ",[str(x) for x in range(1,b+1)])
            title = ask_str("Enter New Title: ")
        
        if len(title.strip()) <= 0:
            title = ask_str("Etner The New Title: ")
        crud.update(id,"task",title)
        
    elif operation.lower() =="delete":
        id = 0
        if len(vector) > 2:
            id = vector[2]
        else:
            id = ask_int("Enter The id to delete: ",[str(x) for x in range(1,b+1)])
        crud.delete(id=id)

    elif operation.lower() =="list":
        if len(vector) > 2:
            param = vector[2]
        else:
            param = "-a"
        crud.list(params=param)
            

    elif operation.lower() == "mark":
        if len(vector) > 2:
            id = vector[2]
            if len(vector) > 3:
                param = vector[3]
            else:
                param = ""
                while param.lower() not in ["d","p"]:
                    param = ask_str("(p) for progress (d) for Completion: ")
                param = f'-{param}'
                
        else:
            param = ""
            while param.lower() not in ["d","p"]:
                param = ask_str("(p) for progress (d) for Completion: ")
            param = f'-{param}'
            id = ask_int("Enter Task Id: ",[str(x) for x in range(1,b+1)])

        
        if param =="-p":
            try:
                cur= a["tasks"][f'task{id}']['status']
                if cur == 1: cur = 0
                if cur == 0: cur =1
            except:
                raise TypeError("Id Not found")
        
            crud.update(id=id,cat='status',value=cur)
        if param == '-d':
            crud.update(id=id,cat='done',value=1)
        
            

            
            
            
            
            


    

except Exception as e:
    print(e)
    # for i in operations:
    #     print(i)

