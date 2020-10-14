from stories import story, arguments, Success, Failure, Result

from factories import StudentFactory, StaffFactory, LessonsFactory 
from entities import Student, Staff, Lessons
from repository import Repository


student_factory = StudentFactory(Student)
staff_factory = StaffFactory(Staff)
lessons_factory = LessonsFactory(Lessons)
repo = Repository()

class CreateStudent:
    @story
    @arguments('name', 'surname', 'phone_number')
    def run(I):
        I.validate
        I.build_entity
        I.persist
        I.done


    def validate(self, ctx):
        return Success()

    def build_entity(self, ctx):
        ctx.entity = student_factory.create(
            name = ctx.name,
            surname = ctx.surname,
            phone_number = ctx.phone_number,
            )
        return Success()

    def persist(self, ctx):
        ctx.result = repo.persist_student(vars(ctx.entity))
        return Success()
    
    def done(self, ctx):
        return Result(ctx.entity)

