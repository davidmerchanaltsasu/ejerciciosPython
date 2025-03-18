mi_Producto1 = {
    "nombre": "coche",
    "codigo_producto": 23478,
    "precio": 10000
}
mi_Producto2 = {
    "nombre": "camion",
    "codigo_producto": 23477,
    "precio": 30000
}
mi_Producto3 = {
    "nombre": "moto",
    "codigo_producto": 23476,
    "precio": 2000
}

# Imprimir los productos de mi_Producto3
for clave, valor in mi_Producto3.items():
    print(clave, valor)

# Usar una lista para almacenar los productos
Sistema_inventario = [mi_Producto1, mi_Producto2]

# Agregar mi_Producto3 a la lista
Sistema_inventario.append(mi_Producto3)
print(Sistema_inventario)

# Eliminar mi_Producto3 de la lista
Sistema_inventario.remove(mi_Producto3)
print(Sistema_inventario)

# Obtener un producto específico (por ejemplo, mi_Producto2)
for producto in Sistema_inventario:
    if producto == mi_Producto2:
        print("Producto encontrado:", producto)

# Obtener valores de "codigo_producto"
codigo_productos = [producto["codigo_producto"] for producto in Sistema_inventario]
print("Códigos de productos:", codigo_productos)












