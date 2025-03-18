def cuenta_palabras_largas(cadena, longitud):
    suma = 0  # Definir suma dentro de la función
    for palabra in cadena.split(" "):
        if len(palabra) > longitud:  # Comparar con longitud
            suma += 1  # Incrementar la variable suma
    return suma  # Devolver el resultado

# Llamar a la función y mostrar el resultado
resultado = cuenta_palabras_largas("carrero blanco campeon de salto", 6)
print("El número de palabras de longitud mayor a la dada es:", resultado)