class Person:
    def __init__(self, name, surname):
        self.name = name 
        self.surname = surname

class Student(Person):
    """Accepts name=str, surname=str, team=str, age=int"""
    school = "Tech Academy"
    
    type = "human" #class attribute 

    def __init__(self, team: str, age: int =22, **kwargs): 
        self.team = team
        self.age = age
        super().__init__(**kwargs)
    
    def __add__(self, others):
        #return self.age + other.age
        result = self.age
        for other in others:
            result += other.age
        return result

    #class method  
    def greeting(self):
        return f"Hi, my name is {self.name} {self.surname}"

class Teacher(Person):
    pass

fatima = Student(
    name = "Fatima",
    surname = "Askerova",
    team = "Rapator"
)

ugur = Student(
    name = "Ugur",
    surname = "Quliyev",
    team = "Rapator",
    age = 18
)

mirelesger = Student(
    name = "Mirelesger",
    surname = "Shabanovv",
    team = "Rapator",
    age = 18
)

xaqani = Student(
    name = "Xaqani",
    surname = "Mirzoyev",
    team = "Rapator",
    age = 18
)

rauf = Student(
    name = "Rauf",
    surname = "Bayramov",
    team = "Rapator",
    age = 18
)

print(fatima + [ugur, mirelesger, xaqani])

arzu = Teacher(
    name = "Arzu",
    surname = "Huseynov"
)

print(fatima.greeting())
print(fatima.__doc__)
print(dir(Student))

"""
setattr()
getattr()
delattr()

"""
#why i get an error here?
#setattr(fatima, 'pc', 'Asus')
#print(fatima.pc)


academy = getattr(fatima, 'school', "T")
print(academy)

delattr(fatima, 'age')
print(fatima.age) 