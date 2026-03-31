import numpy as np
x = np.random.randint(1,10,(3,3))
y = np.random.randint(1,10,(3,3))
print("Matrix X:")
print(x)
print("Matrix Y:")
print(y)
z = x + y
print("Addition:")
print(z)
m = x @ y
print("Multiplication:")
print(m)
