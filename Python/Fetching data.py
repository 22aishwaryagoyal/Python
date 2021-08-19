import pymysql
d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')
cur=d.cursor()
sql="select * from employee"
cur.execute(sql)
data=cur.fetchall()
for res in data:
    print('Empno..',res[0])
    print('Name..',res[1])
    print('City..',res[2])
    print('Salary..',res[3])
d.close()