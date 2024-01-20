# El número de Euler, e ≈ 2,71828, puede ser representado como la siguiente suma infinita:
# Desarrolle un programa que entregue un valor aproximado de e, calculando esta suma hasta que la diferencia 
# entre dos sumandos consecutivos sea menor que 0,0001.
import math
suma=1
k=0
val=2
while val>=0.0001:
    suma+=1/math.factorial(k+1)
    k+=1
    val=1/math.factorial(k)-1/math.factorial(k+1)
    print(round(val,8))
print(f"El ultimo iterado es {k}, valor aproximado de e = {suma}.")