def changeString(character, string , stringLength):
    for i in range(stringLength):
        if i % 2 == 0:
            string[i] = character
    return string

character = input("Digite um caractere: ")
string = list(input("Digite uma string: "))
stringLength = len(string)

print(changeString(character, string, stringLength))