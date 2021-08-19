import pymysql
d=pymysql.connect(host='localhost',user='root',password='Cloud@123$',db='fis')
cur=d.cursor()
sql="select version()"
cur.execute(sql)
data=cur.fetchone()
print(data)
d.close()