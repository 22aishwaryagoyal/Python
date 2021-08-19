
x=input('Enter file to read')
f=open(x,'r')
st=f.read(2000)
print(st)
f.close()