import numpy as np
ar = np.array([1,2,3,4,5])
result = np.where(ar % 2 == 0, ar**2, ar)
print(result)