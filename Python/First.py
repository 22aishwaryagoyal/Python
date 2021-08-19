import sys
x=int(sys.argv[1])
operator=(sys.argv[2])
y=int(sys.argv[3])
if sys.argv[2]=='+':
    print('Addition=',(x+y))
if sys.argv[2]=='-':
    print('Subtraction=',(x-y))
if sys.argv[2]=='*':
    print('Multiplication=',(x*y))
if sys.argv[2]=='/':
    print('Division=',(x/y))