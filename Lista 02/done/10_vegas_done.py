vida_calegario = 3
vida_apostador = 3 

for i in range (6): 
    palavra = str(input())
    acao = int(input())
    resposta = str(input())

    if acao == 1:
        palavra_invertida = ""
        for i in palavra:
            palavra_invertida = i + palavra_invertida

        if resposta == palavra_invertida:
            print("Rodada Concluída!")
            print(f"apostador perdeu uma vida")
            vida_apostador -= 1
        else:
            print("Rodada Concluída!")
            print(f"calegario perdeu uma vida")
            vida_calegario -= 1

    if acao == 2:
        binario = ""
        for i in palavra:
            binario = binario + str(format(ord(i), "08b")) 
        
        if resposta == binario:
            print("Rodada Concluída!")
            print("apostador perdeu uma vida")
            print("Como alguém consegue fazer isso de cabeça?")
            vida_apostador -= 1
        if resposta != binario:
            print("Rodada Concluída!")
            print(f"calegario perdeu uma vida")
            vida_calegario -= 1

    if vida_calegario == 0 or vida_apostador == 0:
        break

if vida_apostador > vida_calegario:
    print("Partida Concluída!")
    print("Vencedor: apostador")
    print("HAHAHA, acha mesmo que preciso trapacear para ganhar de você?")
else:
    print("Partida Concluída!")
    print("Vencedor: calegario")
    print("Droga, não acredito que eu perdi essa partida, achei que seria uma vitória fácil...")
