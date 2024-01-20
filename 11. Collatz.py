# Desarrolle un programa que entregue la secuencia de Collatz de un número entero

n = int(input('Numero entero: '))
while n!=1:
    print(int(n), end=' ')
    if n%2==0:
        n /= 2
    else:
        n = n*3+1
print(1)

# Desarrolle un programa que grafique los largos de las secuencias de Collatz de los números enteros
# positivos menores que el ingresado por el usuario

n = int(input('Numero entero: '))
k=0
for i in range(1,n+1):
    k=i
    len=1
    while k!=1:
        len+=1
        if k%2==0:
            k /= 2
        else:
            k = k*3+1
    largof = len * '*'
    print(f'{i} {largof}')