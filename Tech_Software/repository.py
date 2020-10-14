import json

class Repository:

    def persist_student(self, payload):
        with open('student.json', 'w') as file:
            file.write(json.dumps(payload))