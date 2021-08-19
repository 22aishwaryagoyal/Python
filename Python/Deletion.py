import pymysql
try:
    d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')
    cur=d.cursor()
    sql="delete from employee where empno=106"
    cur.execute(sql)
    print('Record deleted')
    d.commit()
except Exception as ex:
    print(ex)

d.close()
