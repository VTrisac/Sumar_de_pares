print("La suma de los números pares entre 1 y 100 es:")
numero = 1
suma = 0
while numero <= 100:
    if numero % 2 == 0:
        suma += numero
    numero += 1
print(suma)