import json

with open("./d.json", mode = "r") as f:
    data = json.loads(f.read())

for item in data:
    for key, value in item["fields"].items():
        print(key, value)
        if isinstance(value, int):
            item["fields"][key] = str(item["fields"][key])
            
    print()
    print()

# result = map(str, (key, value))
# newList = list(result)
    
    
    


    

        
    



        

   
        