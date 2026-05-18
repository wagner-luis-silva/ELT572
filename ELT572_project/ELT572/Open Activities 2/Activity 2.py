import numpy as np
import random 

matriz = np.empty((5, 5), dtype=int)

for i in range(5):
    for j in range(5):
        matriz[i][j] = random.randint(0, 100)
    
for i in range(5):
    soma = 0
    for j in range(5):
        soma += matriz[i][j]
    print(f"Soma da linha {i + 1}: {soma}")
    

    