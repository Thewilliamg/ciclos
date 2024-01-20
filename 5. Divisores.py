#Escriba un programa que entregue todos los divisores del número entero ingresado:
n=int(input("Ingrese numero para conocer los divisores: "))
tabla=[]
for i in range(n):
    if n%(n-i)==0:
        tabla.append(n-i)
tabla.sort()
def conversion(x):
    return str(x)
txt=""
listanueva=[]
for i in range(len(tabla)):
    listanueva=list(map(conversion,tabla))
    txt=txt+listanueva[i]+" "
print(txt)



