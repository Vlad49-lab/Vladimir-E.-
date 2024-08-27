# Crear un archivo llamado tarea02.py para determinar si los tipos de dato range cumplen:

# Mutabilidad
rango = range(10)
##rango[0] = 5
## print(rango)
##TypeError: 'range' object does not support item assignment


# Suma
rango01 = range(0, 10)
rango02 = range(11, 20)

## suma_r01_r02 = rango01 + rango02
### TypeError: unsupported operand type(s) for +: 'range' and 'range'

# Producto por un entero

## Rango_por_2 = rango * 2
## TypeError: unsupported operand type(s) for *: 'range' and 'int'

# Slicing y conversion a lista
Slicing_rango = list(rango[1:4])

print("Slicing para el rango:", Slicing_rango)
## El Slicing para rangos no lanza ningun TypeError
## Ademas, fue posible convertirlo a lista para visualizar todos los elementos

# Función len
print("Longitud del Rango:", len(rango))

##No hubo ningun problema para conocer la longitud del rango