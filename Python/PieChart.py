import matplotlib.pyplot as plt

labels='UP','MP','AP','Delhi'
lit=[25,35,45,65]
col=['green','red','yellow','blue']
e=(0,0,0,0.1)
plt.pie(lit,labels=labels,explode=e)
plt.show()
