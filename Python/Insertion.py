import pymysql
try:
    d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')
    cur=d.cursor()
    sql="insert into employee values(106,'Tanishka','Pune',30000)"
    cur.execute(sql)
    print('Record Saved')
    d.commit()
except Exception as ex:
    print(ex)

d.close()