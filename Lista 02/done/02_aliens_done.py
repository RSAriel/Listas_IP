frase = ""
contador = 0

while frase != "O relógio descarregou!" or frase != "Por hoje já deu":
    frase = str(input())
    contador += 1

    if frase == "O relógio descarregou!":
        print(f"Corra Ben! Você já derrotou {contador-1} aliens")
        break
    elif frase == "Por hoje já deu":
        print(f"Muito Ben Ben! hehe você derrotou {contador-1} aliens hoje")
        break
