class StudentFactory:
    def __init__(self, builder):
        self.builder = builder
    
    def createStudent(self, **kwargs):
        return self.builder(
            name=kwargs.get('name'),
            surname=kwargs.get('surname'),
            phone_number=kwargs.get('phone_number'),
        )


class StaffFactory:
    def __init__(self, builder):
        self.builder = builder

    def createStaff(self, **kwargs):
        return self.builder(
            name=kwargs.get('name'),
            surname=kwargs.get('surname'),
            phone_number=kwargs.get('phone_number'),
            pay=kwargs.get('pay')
        )


class LessonsFactory:

    def __init__(self, builder):
        self.builder = builder
    
    def createLessons(self, **kwargs):
        return self.builder(
            time=kwargs.get('time'),
            subject=kwargs.get('subject'),
            team=kwargs.get('team'),
        )






    