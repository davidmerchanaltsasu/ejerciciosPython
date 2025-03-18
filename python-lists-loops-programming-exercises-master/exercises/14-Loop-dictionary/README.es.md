# `14` Loop A Dictionary

Los diccionarios nos permiten identificar cada elemento por una clave `key`, a diferencia de las listas en donde simplemente hay valores e índices. Para definir un diccionario, se encierra el listado de valores entre llaves. Las parejas de clave y valor se separan con comas, y la clave y el valor se separan con dos puntos: 

```py
{
    "clave": valor,
    "otra_clave": otro_valor, 
    ...
}
```

### Puedes pensar en un diccionario como en una lista con posiciones no numéricas:

```python
list = ["a", "b", "c"]
dictionary = { "one": "a", "two": "b", "three": "c"}
```

### Cómo obtener valores de un diccionario (muy similar a las listas):

```python
person = { "name": "Juan", "lastname": "Contreras" }
print(person["name"])  # Salida: "Juan"
```

### Cómo añadirle un nuevo valor a un diccionario:

```python
person["age"] = 22
print(person)  # Salida: { "name": "Juan", "lastname": "Contreras", "age": 22 }
```

### Para hacer un bucle en un diccionario, puedes hacer lo siguiente:

```python
spanish_translations = { "dog": "perro", "house": "casa", "cat": "gato" }

for key in spanish_translations:
    print(key)  # <-- Salida: "dog", "house", "cat"
    print(spanish_translations[key])  # <-- Salida: "perro", "casa", "gato"
```

## 📝 Instrucciones:

1. Añade programáticamente las siguientes traducciones al diccionario `spanish_translations`:

```txt
love -> amor
code -> codigo
smart -> inteligente
```

## 💻 Resultado esperado:

```py
{'dog': 'perro', 'house': 'casa', 'cat': 'gato', 'love': 'amor', 'code': 'codigo', 'smart': 'inteligente'}
```
