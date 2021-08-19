import sys
try:
    num1=int(sys.argv[1])
    num2=int(sys.argv[2])
    num3=num1/num2
    print(num3)
except Exception as ex:
    print('Any Issue',ex)
finally:
    print('The ends')