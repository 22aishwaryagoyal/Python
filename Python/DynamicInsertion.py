import pymysql
try:
    d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')
    cur=d.cursor()
    a=int(input('Enter empno:'))
    b=input('Enter Name:')
    c=input('Enter City:')
    e=int(input('Enter Salary:'))
    sql="insert into employee values(%d,'%s','%s',%d)"%(a,b,c,e)
    cur.execute(sql)
    print('Record Saved')
    d.commit()
except Exception as ex:
    print(ex)

d.close()
