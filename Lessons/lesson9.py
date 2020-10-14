#python object & class oop

class myClassName:
    def __init__(self, name, surname, age): 
        self.name = name
        self.surname = surname
        self.age = age
        self.nationality = "Azerbaijani"


def introduce(self):
    print("hi, my name is {self.name}")

@property #no need for (), when you call func
def general_data(self):
    return {
        'name' : self.name,
        'surname' : self.surname,
        'age' : self.age
    }

print(general_data)

fatima = Person (name= "Fatima", surname= "Askerova", age= 22)
 