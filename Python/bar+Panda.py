
import pandas as pd
import matplotlib.pyplot as plt


d={'empno':[101,102,103],'name':['Aish','Surbhi','Aman'],'Salary':[1000,2000,3000]}
df=pd.DataFrame(d)
df['Tax']=df['Salary']*0.30
plt.bar(df['name'],df['Tax'],color='r')
plt.title('Bar Chart..')
plt.show()