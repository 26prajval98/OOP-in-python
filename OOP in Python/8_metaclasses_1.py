required = input('y or n\n')

isTrue = True if required == 'y' else False 

# Similar to meta classes decorator for that class

def classDecorator(cls):
    if isTrue:
        cls.Hallo = 'Hello'
        print('Hello')
    return cls

@classDecorator
class A:
    def __init__(self):
        print('initialised')
        print(self.__dict__)

a = A() 