student = {'name': 'Fatima', 'surname': 'Askerova', 'age': 22, 'group': 'Rapator', "courses": "Python"}
print(student['name'])

#print(student.get('phone number', 'Not Found'))
student['phone number'] = '051 403 87 45'

student['courses'] = 'Python Programming'
student.update ({'name': 'Bla-bla', 'age' : 27, 'group' : 'Blank' })

del student['age']
name = student.pop('name')

print(len(student)) 

print(student.keys()) #all keys
print(student.values()) #all values
print(student.items()) #keys and values 

for key, value in student.items():
    print(key,value)

print(student)


#methods 
student = {'name': 'Fatima', 'surname': 'Askerova', 'age': 22, 'group': 'Rapator', "courses": "Python"}

student_copy = student.copy()
print(student_copy)

#student.clear()

print(student)



