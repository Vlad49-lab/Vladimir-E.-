#EJERCICIOS 01 y 02
# Crear una función que reciba un entero $n$ y devuelva el $n$-ésimo término de la serie de Fibonacci.
x = int(input('INTRODUCE UN NUMERO: '))
serie = [0, 1]
print(x)

def fibo(long, ser, aum, ant):
    if aum != long:
        aum += 1
        ser += ant
        serie.append(ser)
        ant = serie[-2]
        fibo(long, ser, aum, ant)

    else:
        print(serie)
        print('El ultimo numero es: ', serie[-1])

fibo(x, 1, 0, 0)
