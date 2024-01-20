#Desarolle un programa para estimar el valor de π usando la siguiente suma infinita:
#π=4(1−1/3+1/5−1/7+1/9…)
n=int(input("Ingrese la cantidad de terminos de la suma para evaluar pi---->"))
suma=0
k=1
if n>0:
    for i in range(1,n+1): 
        if i%2==0:
            suma-=4/k
        else:
            suma+=4/k  
        k+=2     
    print(suma)
else:
    print("Ingrese un numero válido(entero), vuelva a intentarlo")