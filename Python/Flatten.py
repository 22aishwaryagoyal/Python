import numpy as np
x=np.array([[32,54,6],[12,54,2],[11,54,21],[8,9,11]])
print(x.flatten())
print(x.flatten(order='F'))