# Heaviside step function 
def heaviside(x):
  theta = None
  if x < 0:
    theta = 0.0
  elif x == 0:
    theta = 0.5
  else:
    theta = 1.0
  return theta

x = -3
theta = heaviside(x)
print("Theta(" + str(x) + ") = "+str(theta))
x = 0
theta = heaviside(x)
print("Theta(" + str(x) + ") = "+str(theta))
x = 3
theta = heaviside(x)
print("Theta(" + str(x) + ") = "+str(theta))
