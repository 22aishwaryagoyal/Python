x=input('Enter file name')
f=open(x,'r')
st=f.read(5000)
c=0
d=0
e=0
fd=0
for r in st:
    if r.isdigit():
        c=c+1;
    if r.isupper():
        d=d+1
    if r.islower():
        e=e+1
    if r.isspace():
        fd=fd+1
print('Digits ',c)
print('Upper',d)
print('Lower ',e)
print('spaces',fd)
f.close()