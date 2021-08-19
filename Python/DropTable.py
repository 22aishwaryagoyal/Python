import pymysql
try:
    d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')
    cur=d.cursor()
    sql="drop table test"
    cur.execute(sql)
    print('Table deleted')
    d.commit()
except Exception as ex:
    print(ex)

d.close()
