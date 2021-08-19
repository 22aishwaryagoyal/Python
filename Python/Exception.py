try:
    a=int(input('Enyter number'))
    if a<10:
        raise Exception()
    else:
        print('Ok')
except:
    print('Any Issue')
finally:
    print('Ends')

