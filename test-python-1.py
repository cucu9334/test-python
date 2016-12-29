import numpy as np
import matplotlib.pyplot as plt

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[1, 0, -1], [1, 1, 0]])
print(x)
print(y)


x = range(100)
y = [ i*i for i in x]
plt.plot(x, y)
plt.show( )