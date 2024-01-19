n=int(input("Ingrese un numero: "))
tabla=[]
for k in range(1,11):
    tabla.append(k)
for i in list(tabla):
    print(f" {n} x {tabla[i-1]} = {tabla[i-1]*n}")
