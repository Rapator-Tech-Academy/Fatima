from exeption import UserNotFound

class TestClass:
    pass

myDict = {}

try:
    print(myDict['user'])
except:
    print("Not Found") 