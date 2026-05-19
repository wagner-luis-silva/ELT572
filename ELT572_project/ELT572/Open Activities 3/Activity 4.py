numeros = [1, 2, 3, 4, 5, 6]
resultado = []

for i in range(len(numeros)):
    if i % 2 == 0:
        resultado.append(numeros[i] ** 2)
    else:
        resultado.append(numeros[i] * 2)

print(resultado)

resultado_final = sum(resultado)
print(resultado_final)

