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

def Fahrenheit_to_Kelvin(F):
    """convert"""
    K=0.0
    K = (F-32)*(5/9) + 273.15
    return K

def Kelvin_to_Celsius(K):
    C = 0.0
    C = K-273.15
    return C

#F =32
#K = Fahrenheit_to_Kelvin(F)
#C = Kelvin_to_Celsius(K)
#print("When F = ", F, "K = ",K, "C = ", C)


