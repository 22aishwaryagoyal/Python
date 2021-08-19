import pandas as pd
#df=pd.read_csv('salaries.csv')

#Top 5 Records
#print(df.head())

#Top 2 Records
#print(df.head(2))

#bottom 5 Records
#print(df.tail())

#bottom 3 Records
#print(df.tail(3))

#Tells the datatype and in place of string shows object
#print(df.dtypes)

#No of rows and columns
#print(df.shape)

#print 0 to 2
#print(df[0:3])
#print row 4 onwards
#print(df[4:])

#row 0 to 1 & column 0 to 2
#print(df.iloc[0:2,0:3])
#print(df)

#Conditional data
#dt=df[(df['salary']>90000) & (df['discipline']=='B')]
#print(dt)

#Handling Missing Values
#replace  by sum.max,min
#df['service'].fillna(df['service'].sum(),inplace=True)

#all null removed
#dt=df.dropna()
#print(dt)


#insert new column
#df.insert(6,'test',df['service']+20)

#append
'''df=pd.read_csv('salaries.csv')
df1=pd.read_csv('salaries1.csv')
df2=df.append(df1)
print(df2)'''

#merging two CSV files
'''df=pd.read_csv('Emp.csv')
df1=pd.read_csv('EmpGrade.csv')
print(pd.merge(df,df1,on='EmpNo'))'''

#Sorted data-Ascending
'''df=pd.read_csv('salaries.csv')
print(df.sort_values('salary'))'''

#Descending Order
'''df=pd.read_csv('salaries.csv')
print(df.sort_values('salary',ascending=False))'''

#group on base of rank and sum of salary
'''df=pd.read_csv('salaries.csv')
dc=df.groupby(['rank'])
print(dc['salary'].sum())'''

#Summarized Data
'''df=pd.read_csv('StudentDataForPivot.csv')
print(pd.pivot_table(df,index=['Name','Subject'],values='Score',aggfunc='sum'))'''

'''import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')
plt.plot(df['EmpCode'],df['Payment'],color='red',linestyle='--',linewidth=5)
plt.show()'''

'''import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')
dfg=df.groupby('City')
total=dfg['Payment'].sum()
total.plot(kind='bar')'''

#Histogram
'''import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')
plt.hist(df['Payment'],bins=5)
plt.show()'''


#pieChart
'''import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')
c=df.groupby(df['City'])
cp=['red','green','blue']
c.sum().plot(kind='pie',y='Payment')'''

#Scatter Chart
import matplotlib.pyplot as plt
df=pd.read_csv('EmpData.csv')
plt.scatter(df['Payment'],df['NoOfHours'],marker='o')
plt.show()