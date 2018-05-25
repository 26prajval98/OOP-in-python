class A:
    def __init__(self):
        print('A')
        super().__init__()

class B(A):
    def __init__(self,first, **k):
        self.first = first
        print('B: {}'.format(self.first))
        super().__init__(**k)

class C(A):
    def __init__(self,last, **k):
        self.last = last
        print('C: {}'.format(self.last))
        super().__init__(**k)

class D(B,C):
    def __init__(self,first,last):
        print('D')
        super().__init__(first=first,last=last)

D('first','last')

print(D.__mro__)