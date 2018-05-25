# Selecting meta classes to work on __new__ or __init__ is based on intution

# A metaclass which changes all the attributes to lower


class lower(type):
    def __new__(cls, clsname, supercls, clsattr):
        newclsattr = {}
        for key in clsattr:
            newclsattr[key.lower()] = clsattr[key]
        # returning type.new(cls, clsname, supercls, newclsattr) is same as returning the following
        return type(clsname,supercls,newclsattr)

class A(metaclass = lower):
    ABCD = 10

a = A()

# print(a.ABCD) Error
# print(a.abcd) No Error
