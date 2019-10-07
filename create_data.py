import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

sigma = 0.3
x = np.random.rand(100) * 2 - 1
print(x)
y = np.sin(math.pi * x) + sigma * np.random.randn(len(x))
# y = x ** 3 + x ** 2 + sigma * np.random.randn(len(x))
print(y)

d = pd.DataFrame(zip(x, y))
print(d)
d.to_csv('./d.csv', header=['x', 'y'], index=None)

plt.plot(x, y, 'o')
plt.show()
