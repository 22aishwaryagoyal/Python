import matplotlib.pyplot as plt
import numpy as np

ct=['India','China','Uk']
pop=[1.35,1.80,1]
y=np.arange(len(ct))
#plt.bar(y,pop)
plt.barh(y,pop)
plt.xticks(y,ct)
plt.title('Pop Chart')
plt.show()