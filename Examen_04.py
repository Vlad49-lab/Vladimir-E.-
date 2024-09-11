# EJERCICIO 04 (LO HICE EN CASA POR QUE ME PUSE NERVIOSO EN EL EXAMEN Y NO LO PUDE HACER, ME QUEDE
# BLOQUEADO, PERO LO HICE SIN CONSULTAR NADA, SOLO FUERON LOS NERVIOS Y EL TIEMPO)
introduccion = list(input('INTRODUCE UNA CADENA: '))
rango = int(input('INTRODUCE EL NUMERO DE ELEMENTOS A CONSIDERAR: '))

cadena_final = introduccion


while len(cadena_final) <= rango:
    cadena_final *= 2

else:
    lista_cadena = cadena_final[0:rango]
    print(lista_cadena)



suma = 0

for x in lista_cadena:
    if x == 'a':
        suma += 1
        continue
    else:
        continue

print(suma)
