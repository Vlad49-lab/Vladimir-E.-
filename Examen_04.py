# EJERCICIO 04 (LO HICE EN CASA POR QUE ME PUSE NERVIOSO EN EL EXAMEN Y NO LO PUDE HACER, ME QUEDE
# BLOQUEADO, PERO LO HICE SIN CONSULTAR NADA, SOLO FUERON LOS NERVIOS Y EL TIEMPO)
introduccion = input('INTRODUCE UNA CADENA: ')
rango = int(input('INTRODUCE EL NUMERO DE ELEMENTOS A CONSIDERAR: '))

cadena_final = introduccion

def cadena(cadena_final):
    if len(cadena_final) < rango:
        cadena_final *= 2
        cadena(cadena_final)

    else:
        return cadena_final

cadena(introduccion)
lista_cadena = list(cadena_final[0:rango])
print(lista_cadena)

suma = 0

for x in lista_cadena:
    if x == 'a':
        suma += 1
        continue
    else:
        continue

print(suma)
