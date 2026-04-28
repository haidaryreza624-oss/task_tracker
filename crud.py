import json
def find_add_id():
    with open("data.json","rb")as f:
        a = json.load(f)
        try:
            id = a["used_ids"][-1]
        except:
            id = 0
        finally:
            return id,a

def write_json(obj):
    with open("data.json","w")as f:
        json.dump(obj,f)


def add(title:str,isinprogress=False):
    id,tasks = find_add_id()
    if len(title) == 0:
        raise TypeError("Must enter a value for title")
    
    obj = {"id":id+1,"task":title,"status":int(isinprogress)}
    tasks["tasks"][f'task{id+1}'] = obj
    tasks["used_ids"].append(id+1)
    try:
        write_json(tasks)
        return "Task Added sucussully"
    except:
        return "Something Wrong Happended"
    

    
def delete(id):
    with open("data.json","r")as f:
        a = json.load(f)
        try:
            obj = a["tasks"][f'task{id}']
            a["tasks"].pop(f'task{id}')
            while True:
                confirm = input(f'Are you sure to delete following records: \n{obj["task"]}?\ny/n:')
                if confirm.lower() in ['y','n']:
                    break
            if confirm == "y":
                write_json(a)          
                return "Delete Successfully"
            else:
                return "Delete was canceled"

        except:
            raise TypeError("The following id you requested does not exist")



def update(id,cat,value):
    with open("data.json","r")as f:
        a = json.load(f)
        try:
            obj = a["tasks"][f'task{id}']
            obj[cat] = value
            while True:
                confirm = input(f'Are you sure to Update following records: \n{obj["task"]}?\ny/n:')
                if confirm.lower() in ['y','n']:
                    break
            if confirm == "y":
                write_json(a)          
                return "Update Successfully"
            else:
                return "Update was canceled"
                
            

        except:
            raise TypeError("The following id you requested does not exist")

