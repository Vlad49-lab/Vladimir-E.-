# 01 PROMEDIO DEL TOTAL
calif_1 = 10
calif_2 = 7
calif_3 = 4
calificacion = (.15 * calif_1) + (.35 * calif_2) + (.5 * calif_3)

print(calificacion)

# Matriz y cuarto valor

matriz = [ [1, 1, 1, 3], [2, 2, 2, 7], [3, 3, 3, 9], [4, 4, 4, 13] ]
print("La matriz inicial es: ", matriz)


cuarto_elemento = [matriz[0][3],matriz[1][3],matriz[2][3],matriz[3][3]]

for x in cuarto_elemento:

    if x == matriz[0][3]:
        if x != matriz[0][0] + matriz[0][1] + matriz [0][2]:
            matriz[0][3] = matriz[0][0] + matriz[0][1] + matriz [0][2]


        else:
          pass

    elif x == matriz[1][3]:
        if x != matriz[1][0] + matriz[1][1] + matriz [1][2]:
            matriz[1][3] = matriz[1][0] + matriz[1][1] + matriz [1][2]


        else:
           pass

    elif x == matriz[2][3]:
        if x != matriz[2][0] + matriz[2][1] + matriz [2][2]:
            matriz[2][3] = matriz[2][0] + matriz[2][1] + matriz [2][2]


        else:
            pass

    elif x == matriz[3][3]:
        if x != matriz[3][0] + matriz[3][1] + matriz [3][2]:
            matriz[3][3] = matriz[3][0] + matriz[3][1] + matriz [3][2]


        else:
            pass

    else:
        print('no es posible')

print('la matriz corregida es', matriz)

