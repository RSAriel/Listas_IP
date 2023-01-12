#acho que o problema tem a ver com eu não estar considerando entradas repetidas como inválidas, mas não sei como fazer isso sem listas

print("Roteiro emitido!")
print("DIA:")
numero_atividades = 0
entrada_dia = 0
entrada_noite = 0

while True:
    entrada_dia = str(input())

    if entrada_dia != "Ir para a Praia do Amor" and entrada_dia != "Passeio de Lancha" and entrada_dia !="Surf na Praia de Pipa" and entrada_dia != "Por do sol no chapadão" and entrada_dia != "Passeio de buggy" and entrada_dia != "Arborismo e Tirolesa" and entrada_dia!= "NOITE":
        print("[INVALIDO]")
        continue

    if entrada_dia ==  "NOITE":
        print("NOITE:")
        break

    numero_atividades += 1
    print(entrada_dia)

if numero_atividades % 2 != 0:

    for i in range(2):
        entrada_noite = str(input())
        if entrada_noite != "Jantar gastronômico" and entrada_noite != "Passear pelo centrinho" and entrada_noite !="Luau" and entrada_noite != "Festa com DJ":
            print("[INVALIDO]")
            continue   
        
        numero_atividades += 1
        print(entrada_noite)

if numero_atividades % 2 == 0:
    while True:
        entrada_noite = str(input())

        if entrada_noite != "Jantar gastronômico" and entrada_noite != "Passear pelo centrinho" and entrada_noite !="Luau" and entrada_noite != "Festa com DJ" and entrada_noite != "Oba, Tudo planejado!!":
            print("[INVALIDO]")
            continue  

        if entrada_noite == "Oba, Tudo planejado!!":
            break  

        numero_atividades += 1 
        print(entrada_noite)

print(f"Venha curtir esse dia em Pipa com um roteiro com {numero_atividades} atividade(s)!")