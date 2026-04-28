import json
with open("data.json","rb")as f:
    a = json.load(f)
    ids = a["used_ids"]
    print(ids)
data = {"id":1,"task_name":"Hello world"}
with open("data.json","rb",) as f:
    a = json.load(f)
    print(a['tasks'])