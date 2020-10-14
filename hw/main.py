print("Welcome to the Address Book")
print ("Please enter contact info below")

class PersonInfo:
    def __init__(self, name, surname, number, category):
        self.name = name 
        self.surname = surname
        self.number = number
        self.category = category 

    def __str__(self):
        return f"{self.name} {self.surname} | {self.number} | {self.category}"
 
class Family(PersonInfo):
    pass

class Friends(PersonInfo):
    pass

class Colleagues(PersonInfo):
    pass


category = {
    'family' : [],
    'friends' : [],
    'colleagues' : []
}


name = input("Please, enter contact name: ")
surname = input("Please, enter contact surname: ")
number = input ("Please, enter phone number: ")
category = input("Choose category (Example: 1- family, 2-friends, 3-colleagues): ")


contact = list()
user_input = ""
 
while  user_input != "q":
    print("Available categories")
    print("1- Family")
    print("2- Friends")
    print("3- Colleagues")
    print("q- Quit Address Book")

    if user_input == 1:
        contact=Family(name = name, surname = surname, number = number, category = 'Family')
        category['family'].append(contact)

    elif user_input == 2:
        contact=Friends(name = name, surname = surname, number = number, category = 'Friends')
        category['friends'].append(contact)

    elif user_input == 3:
        contact=Family(name = name, surname = surname, number = number, category = 'Colleagues')
        category['colleagues'].append(contact)




new_contact = PersonInfo(name, surname, number, category)
print(new_contact)

print("Info will be added to the Address Book")

