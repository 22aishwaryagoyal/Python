import pandas as pd

st={'rollno':101,'name':'Aishwarya','city':'Bangalore','marks':95}
#s=pd.Series(st)
s=pd.Series(st,index=['city','name','rollno','marks'])
print(s)