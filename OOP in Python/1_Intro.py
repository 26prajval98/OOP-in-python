"""Introduction to OOP in python 3 """

class Car:
    def __init__(self,company=None, name=None, key=None):
        self.company = company
        # Just a convention by programmer to show that the variable is protected 
        self._name = name
        self.__key = key

if __name__=="__main__":
    a = Car('Maruti Suzuki','WagonR','1234')
    a._name = "Swift"

