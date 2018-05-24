"""Operator Overloading and magic methods"""

class Ball:
    def __init__(self,no,speed):
        self.no = no
        self.speed = speed
    
    # Add two stuff from same class or right does not support add
    def __add__(self,other):
        print(other.speed)
        return Ball(self.no+other.no,self.speed+other.speed)
    
    # Only when left operator does not support add
    def __radd__(self,other):
        return Ball(self.no,self.speed+other)

    # iadd += 
    def __iadd__(self,other):
        print("+= not =")

a = Ball(1,10)
b = Ball(1,100)

c = a + b

d = 10 + c

d += c