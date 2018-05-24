"""Abstarct classes in python"""

from abc import abstractmethod, ABC

class A(ABC):
    @abstractmethod
    def something(self):
        print('Done Something')

class B(A):
    def something(self):
        print('No more abstract')

a = B()
a.something()