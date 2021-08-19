import pymysql
import matplotlib.pyplot as plt

d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')
cur=d.cursor()
sql="select * from employee"
cur.execute(sql)
data=cur.fetchall()
name=[]
sal=[]
for res in data:
    name.append(res[1])
    sal.append(res[3])

plt.plot(name,sal)
plt.legend()
plt.xlabel('empname')
plt.ylabel('salary')
print(data)
d.close()