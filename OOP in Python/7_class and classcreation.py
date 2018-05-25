x = [1,2,3,4]
y = 10

print(type(x),type(y),type(list))


# Creating class using type
def A_init(self,no):
    print('Object Of class A is initialized')
    self.no = no


# type('className', (inhertance), {class methods and variables})
A = type('A',(),{
    '__init__' : A_init
})

y = A(10)
# print(y.no)