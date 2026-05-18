def funcCheckNegative(ent1, ent2):
    if ent1 - ent2 < 0:
        print("ent1 - ent2 é negativo")
    if ent1 * ent2 < 0:
        print("ent1 * ent2 é negativo")
    if ent1 + ent2 < 0:
        print("ent1 + ent2 é negativo")
        
ent1 = int(input("Digite o primeiro número: "))
ent2 = int(input("Digite o segundo número: "))

funcCheckNegative(ent1, ent2)
