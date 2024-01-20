n=1
m=0
while n!=0:
    n=int(input("Inserte la duracion del tramo (en minutos): "))
    m+=n
horas=m//60
minutos=m%60
if minutos>9:
    print(f"Tiempo total de viaje {horas}:{minutos} horas")
else:
    print(f"Tiempo total de viaje {horas}:0{minutos} horas")

