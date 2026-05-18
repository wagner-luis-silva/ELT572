import numpy as np

notas = np.zeros(5, dtype=float)

for i in range(5):
    valor = float(input(f"Informe a nota da atividade {i + 1}: "))
    while valor < 0 or valor > 100:
        print("Valor inválido. A nota deve estar entre 0 e 100.")
        valor = float(input(f"Informe a nota da atividade {i + 1}: "))
    notas[i] = valor

media = 0
for i in range(5):
    media += notas[i]
media /= 5
print(f"Média das notas: {media:.1f}")

if media >= 60.0:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado")
