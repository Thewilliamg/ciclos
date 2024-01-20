#Escriba un programa que genere todas las potencias de 2, desde la 0-ésima hasta la ingresada por el usuario:
pot=int(input("Ingrese el numero de potencias: "))
potdos=[]
for i in range(pot+1):
    potdos.append(2**(i))
#print(potdos)
#imprimir sin comas ni "[]""
def conversion(k):
    return str(k)
lista=[]
txt=""
for i in range(pot+1):
    lista=list(map(conversion,potdos))
    txt=txt+lista[i]+" "
print(txt)