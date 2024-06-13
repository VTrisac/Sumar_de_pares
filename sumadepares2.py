print("La suma de los números pares entre 1 y 100 es:")
numero = 1
suma = 0
while numero <= 100:
    numero += 1
    if numero >= 20 and numero <= 30:
        continue
    if numero % 2 == 0:
        suma += numero
print(suma)