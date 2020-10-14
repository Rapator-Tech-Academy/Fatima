class BaseEntity:
    def __init__(self, name, surname, phone_number):
        self.___name = name
        self.___surname = surname
        self.phone_number = phone_number
  
    def get_name(self):
        return self.___name

    def get_surname(self):
        return self.___surname


class Students(BaseEntity):
    pass


class Staff(BaseEntity):
    def __init__(self, pay, **kwargs):
        self.pay = pay 
        super().__init__(**kwargs)


class Lessons:
    def __init__(self, time, subject, team):
        self.time = time
        self.subject = subject
        self.team = team
        



