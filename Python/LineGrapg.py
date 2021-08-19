import pandas as pd

data={'year':[1971,1981,1991,2001,2011],'pop':[50,73,81,98,111]}
df=pd.DataFrame(data,columns=['year','pop'])
df.plot(x='year',y='pop',kind='line')

