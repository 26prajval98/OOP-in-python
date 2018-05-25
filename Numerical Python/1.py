import numpy as np

# Making arrays using np

# Using arange
a = np.arange(1, 10)
print(a)

a = np.arange(5.4)
print(a)

a = np.arange(0, 10, 0.8)
print(a)

a = np.arange(0.1, 10.8, 0.8, dtype=float)
print(a)

# Using linspace which is used for equally spaced numbers
a = np.linspace(1, 10)
print(a)

a = np.linspace(1, 10, 7)
print(a)

a = np.linspace(1, 10, 7, endpoint=False)
print(a)

# zero dimensional
x = np.arange(1,10)
print(x,np.ndim(x))

# Shape
x = np.array([[1, 2, 3, 4],[2, 3, 4, 5]])
print(np.shape(x))