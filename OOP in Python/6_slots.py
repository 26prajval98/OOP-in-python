"""Slots are used to create a slotted objects and dynamically created attributes can be avoided """

class A:
    __slots__ = ['val']

    def __init__(self, val):
        self.val = val
    
a = A(100)

print(a.val)

# a.x = 'a' Gives Error
