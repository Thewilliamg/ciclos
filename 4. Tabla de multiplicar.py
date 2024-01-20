#Los números deben estar alineados a la derecha.
for i in range(1,11):
    for j in range(1,11):
        print("{:>4}".format(i*j),end="")
    print()
