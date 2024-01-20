#Escriba un programa que pida al usuario ingresar la altura y el ancho de un rectángulo y lo dibuje utilizando asteriscos:
h=int(input("Altura: "))
b=int(input("Ancho: "))
for j in range(h):
    for i in range(b):
        print("*",end="")
    print()
#...................
#Escriba un programa que dibuje el triángulo del tamaño indicado por el usuario de acuerdo al ejemplo:

ht=int(input("Altura del triangulo: "))
for j in range(ht+1):
    for i in range(j):
        print("*",end="")
    print()

#...................
#Escriba un programa que dibuje el hexágono del tamaño indicado por el usuario de acuerdo al ejemplo:
#Definimos una variable para dibujar los espacios
l=int(input("ingrese el lado del hexagono: "))
espacios = l-1
for i in range(l, 3*l, 2):
	print(" "*espacios + "*"*i)
	espacios -= 1
espacios = 1
for i in range(3*l-4, l-2, -2):
    print(" "*espacios + "*"*i)
    espacios+=1