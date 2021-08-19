import sys
try:
    num1=int(sys.argv[1])
    num2=int(sys.argv[2])
    num3=num1/num2
    print(num3)
except IndexError:
    print('Missing Values')
except ValueError:
    print('Enter Correct Values')
except ZeroDivisionError:
    print('Zero Error')
    