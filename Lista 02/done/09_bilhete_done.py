n_sorteado_binario = str(input())
n_sorteado = str(int(n_sorteado_binario, 2))


acertou = False
bilhete_premiado = False 

if n_sorteado == "1" or n_sorteado == "2" or n_sorteado == "3" or n_sorteado == "4" or n_sorteado == "5":
    bilhete_premiado = True

for i in range(3): 
    palpite = str(input())

    if palpite == n_sorteado:
        acertou = True
        break
    if i != 2:
        print(f"Resposta incorreta. Mas não desista! Você ainda tem {2-i } chance(s).")

if acertou == False:
    if bilhete_premiado == True:
        print("Infelizmente mais uma resposta incorreta.")
        print("Agradecemos sua participação!")
        print("Seu bilhete era premiado. Que pena!")
    else:
        print("Infelizmente mais uma resposta incorreta.")
        print("Agradecemos sua participação!")
        print("Pelo menos seu bilhete não era premiado.")
        print("Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!")
        
if acertou == True:
    print("Parabéns!! Você acertou!")
    
    if n_sorteado == "1":
        print("Férias inesquecíveis estão te esperando!")
        print("Seu destino será Porto de Galinhas (BRA).")
        print("Prepare-se para viver dias incríveis desfrutando das riquezas naturais da nossa região!")
    elif n_sorteado == "2":
        print("Férias inesquecíveis estão te esperando!")
        print("Seu destino será Fernando de Noronha (BRA).")
        print("Belíssimas praias estão por vir.")
        print("Não esqueça o protetor solar.")
    elif n_sorteado == "3":
        print("Férias inesquecíveis estão te esperando!")
        print("Seu destino será Gramado (BRA).")
        print("Aproveite passeios e paisagens espetaculares no sul do país!")
    elif n_sorteado == "4":
        print("Férias inesquecíveis estão te esperando!")
        print("Seu destino será Berlim (ALE).")
        print("Desfrute de muita cultura e de experiências incríveis!")
        print("Prepare os casacos de frio!")
    elif n_sorteado == "5":
        print("Férias inesquecíveis estão te esperando!")
        print("Seu destino será Tóquio (JPN).")
        print("Viva uma experiência inesquecível explorando um país do outro lado do mundo.")
        print("Prepare-se para muitas horas de voo!")
    else:
        print("Mas, infelizmente, hoje não é o seu dia de sorte.")
        print("Apesar de ter dado a resposta correta, seu bilhete não oferece nenhum prêmio.")
        print("Sinta-se à vontade para conhecer nossos pacotes e outras promoções imperdíveis com um de nossos vendedores!")
