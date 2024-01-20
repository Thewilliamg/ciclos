#Desarrolle un programa que permita trabajar con las potencias fraccionales de dos, es decir: en forma decimal:
a="Potencia"
b="Fraccion"
c="Suma"
print(f"{a}   {b}   {c}")
exponente=1
sum=0.5
fraccion=0.5
while fraccion>0.000001:
    print(str(exponente).ljust(10), end=" ")
    print(str(round(fraccion,4)).ljust(10), end=" ")
    print(round(sum,4))
    exponente+=1
    fraccion=0.5**exponente
    sum+=fraccion