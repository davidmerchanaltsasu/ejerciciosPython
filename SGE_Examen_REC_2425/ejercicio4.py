
def es_perfecto(numero):
    suma_divisores = 0
    divisores = []

    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
            divisores.append(i)

    print(f"Divisores de {numero}: {divisores}")


    return suma_divisores == numero


numero = int(input("Ingrese un número: "))


if es_perfecto(numero):
    print(True)  # Si el número es perfecto
else:
    print(False)  # Si el número no es perfecto
