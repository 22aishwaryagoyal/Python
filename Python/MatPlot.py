import matplotlib.pyplot as plt

'''x=[10,22,35]
y=[20,10,25]
#plt.plot(x,y)
plt.plot(x,y,'--r')
x2=[11,23,31]
y2=[20,24,32]
plt.plot(x2,y2,'--g')'''

'''states=['Delhi','AP','MP']
pop=[1.2,4.9,3.8]
plt.plot(states,pop)
plt.title('Pop in Crore')
plt.xlabel('States')
plt.ylabel('Population')'''

'''sem=[1,2,3]
m1=[34,90,65]
m2=[54,76,43]
plt.plot(sem,m1,label='Aishwarya')
plt.plot(sem,m2,label='Surbhi')
plt.legend()
plt.xlabel('Sem.')
plt.ylabel('Marks.')'''

sem1=[1,3,5]
m1=[34,90,65]
sem2=[2,4,6]
m2=[54,76,43]
plt.bar(sem1,m1,color='r')
plt.bar(sem2,m2,color='b')
plt.title('Bar Chart..')
plt.show()