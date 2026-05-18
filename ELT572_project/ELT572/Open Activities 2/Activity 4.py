def changeString(character, string , stringLength):
    for i in range(stringLength):
        if i % 2 == 0:
            string[i] = character
    print(string)
    
character = input("Digite um caractere: ")
string = list(input("Digite uma string: "))
stringLength = len(string)

changeString(character, string, stringLength)
