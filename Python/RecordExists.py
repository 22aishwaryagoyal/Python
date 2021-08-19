import pymysql
try:
    d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')
    p=int(input('Enter empno-'))
    
    cur=d.cursor()
    sql="select * from employee where empno=%d"%(p)
    cur.execute(sql)
    d.commit()
    data=cur.fetchone()
    if data!=None:
        print('ALREADY PRESENT')
    else:
        b=input('Enter Name:')
        c=input('Enter City:')
        e=int(input('Enter Salary:'))
        sql="insert into employee values(%d,'%s','%s',%d)"%(p,b,c,e)
        cur.execute(sql)
        print('Record Saved')
        d.commit()
   
    
except Exception as ex:
    print(ex)

d.close()
