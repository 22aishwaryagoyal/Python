import pandas as pd

data={'country':['India','US','UK'],'gdp':[5,9,8]}
df=pd.DataFrame(data,columns=['country','gdp'])
df.plot(x='country',y='gdp',kind='bar')