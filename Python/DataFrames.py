import pandas as pd

#blank dataframe
#df=pd.DataFrame()

#2D format
#d=[32,4,67,5,89]
#df=pd.DataFrame(d)

#d=[['aishwarya',12],['Aman',21],['Surbhi',34]]
#df=pd.DataFrame(d,columns=['Name','RollNo'])
#print(df)

#d={'rollno':[101,102,103,104],'name':['a','b','c','d'],'marks':[56,67,78,89]}
#df=pd.DataFrame(d)

'''df=pd.DataFrame(d,index=['Rank1','Rank2','Rank3','Rank4'])
print(df)
print(df['rollno'])
df['promote']=df['marks']+10
print(df)'''

d={'empno':[101,102,103],'name':['Aish','Surbhi','Aman'],'Basic':[1000,2000,3000]}
df=pd.DataFrame(d)
df['HRA']=df['Basic']*0.12
df['Total']=df['HRA']+df['Basic']
print(df)