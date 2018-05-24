class A:
    rm = 1
    def __init__(self,x):
        self.x = x
        
    #Can be used as a constructor 
    @classmethod 
    def constructA(cls,x):
        return cls(x)

    @classmethod
    def setX(cls,x):
        cls.rm = x

    @staticmethod
    def checkRm(val):
        if(val>10):
            return True
        else:
            return False

x = A(10)
y = A.constructA(1)

x.setX(100)

print(x.rm, y.rm, A.rm)
print(A.checkRm(10),x.checkRm(100),y.checkRm(9))
        