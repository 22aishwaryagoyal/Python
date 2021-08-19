import pymysql
try:
    d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')
    cur=d.cursor()
    sql="create table test(empno int,month varchar(20))"
    cur.execute(sql)
    print('Table created')
    d.commit()
except Exception as ex:
    print(ex)

d.close()