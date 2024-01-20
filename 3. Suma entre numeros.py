# Escriba un programa que pida al usuario dos números enteros, y luego entregue la suma de todos los números que están entre ellos.
# Por ejemplo, si los números son 1 y 7,
# debe entregar como resultado 2 + 3 + 4 + 5 + 6 = 20.
e1=int(input("ingrese el primer numero entero: "))
e2=int(input("ingrese el segundo numero entero: "))
if e1!=e2:
    if e1>e2:
        dif=e1-e2
        min=e2+1
    elif e1<e2:
        dif=e2-e1
        min=e1+1
    lsum=[]
    suma=0
    for i in range(dif-1):
        lsum.append(min+i)
        suma+=lsum[i]
    print(f"La suma es {suma}")
else:
    print("ERROR - ingrese dos numeros diferentes")
