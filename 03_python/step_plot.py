# define the first function 
def heaviside(x):
  theta = None
  if x < 0:
    theta = 0
  elif x > 0:
    theta = 0.5
  else:
    theta = 1
  return theta

import matplotlib.pyplot as plt





x=[]
x.append(4)

#for i in range(17):
#  x.append(4-0.5*i)
while min(x) > -4:
  x.append(min(x)-0.5)
  print(x)


#theta=[]
#for k in range(len(x)):
#  temp = heaviside(x[k])
#  theta.append(temp)

#for k in range(len(x)):
#  print("x =, theta=",x[k],theta[k])


#plt.plot(x, theta, '-o', color="red", linewidth=2)
#plt.show()
