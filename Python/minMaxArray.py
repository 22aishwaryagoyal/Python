import numpy as np
x=np.array([[32,54,6],[12,54,2],[11,54,21],[8,9,11]])
print(np.amin(x))
print(np.amin(x,0))
print(np.amin(x,1))
print(np.max(x))
print(np.amax(x,0))
print(np.amax(x,1))