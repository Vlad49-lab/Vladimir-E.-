#EJERCICIO 03
x = int(input('INTRODUCE EL INICIAL: '))
y = int(input('INTRODUCE EL FINAL: '))
rango = list(range(x, y+1))
serie = [0]

def wats(inicial, final, suma):
    final_serie = serie[-1]

    if final_serie < final:
        n = (rango[suma]**2)
        suma += 1
        serie.append(n)
        wats(inicial, final, suma)

    else:
        print(serie[1:-1])
        print(len(serie)-2)

wats(x, y, 0)