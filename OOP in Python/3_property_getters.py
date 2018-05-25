# @property is a getter then setters can be used

class Person:
    def __init__(self,first=None,last=None):
        self.first = first
        self.last = last
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    @fullname.setter
    def fullname(self,fullname):
        self.first,self.last = fullname.split(' ')

p_1 = Person('Harry','Potter')
print(p_1.fullname)

p_1.first = 'Hairy'
print(p_1.fullname)

p_1.fullname = 'Emma Watson'

print('{} {} {}'.format(p_1.first,p_1.last,p_1.fullname))