people = []

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.__citizenship = "Azerbaijani"
 
    def get_citizenship(self):
        return self.__citizenship

class PersonBehavior(Person):
    def greeting(self):
        return f"Hi, my name is {self.name}"

    def __add__(self, other):
        return self.age + other.age
    
    class Engineer(Person, PersonBehavior):
        def __init__(self, age, **kwargs):
            self.age = age
            super().__init__(**kwargs)

john = Engineer(name = "John", surname = "Doe") 

fatima = Person(name = "Fatima", surname = "Askerova")
#people.append(vars(fatima))
people.append(fatima.__dict__)

print(people)

#issubclass 
print(john.__citizenship)
print(issubclass(Engineer, Person))