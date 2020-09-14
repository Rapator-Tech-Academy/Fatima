#dictionary 
#myDict = {} or myDict = dict({})

rapator = {"current lesson": "Python", "students" : 5, "mentor" : 1, "teacher" : 1}

#access elements in dictionary
print(rapator['students']) #output error, if there is no element with that key
print(rapator.get('mentor')) 

#add and change
rapator['students'] = 6
rapator ['add'] = "new element added"

#delete or remove 
print(rapator.pop("add"))
print(rapator.popitem())
del rapator["mentor"]

rapator = {"current lesson": "Python", "students" : 5, "mentor" : 1, "teacher" : 1}
rapator.update({'update' : 'upd mthd'})

for item in rapator.items():
    print(item)

for key, value in rapator.items():
    print(f"key : {key}, value : {value}")

print(rapator)

#list
cities = ["Istanbul", "Baku", "Tbilisi", "Moscow"]
upper_cities = [item.upper() for item in cities]
upper_cities = [item.upper() for item in cities if len(item) > 5]
print(upper_cities)

#dict
squares = {x : x*x for x in range(11)}
print (squares)

#dictionary operations (in, not in) 
print(1 in squares)
print(11 in squares)
print(22 not in squares)

#sorted
print(sorted(rapator))