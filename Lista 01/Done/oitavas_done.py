nome_time_1 = str(input())
resultado_jogo1_time1 = str(input())
resultado_jogo2_time1 = str(input())
pontos1 = 0

nome_time_2 = str(input())
resultado_jogo1_time2 = str(input())
resultado_jogo2_time2 = str(input())
pontos2 = 0

nome_time_3 = str(input())
resultado_jogo1_time3 = str(input())
resultado_jogo2_time3 = str(input())
pontos3 = 0



if resultado_jogo1_time1 == "Ganhou":
    pontos1 += 3 
elif resultado_jogo1_time1 == "Empatou":
    pontos1 += 1

if resultado_jogo2_time1 == "Ganhou":
    pontos1 += 3 
elif resultado_jogo2_time1 == "Empatou":
    pontos1 += 1


if resultado_jogo1_time2 == "Ganhou":
    pontos2 += 3 
elif resultado_jogo1_time2 == "Empatou":
    pontos2 += 1 

if resultado_jogo2_time2 == "Ganhou":
    pontos2 += 3 
elif resultado_jogo2_time2 == "Empatou":
    pontos2 += 1   
    

if resultado_jogo1_time3 == "Ganhou":
    pontos3 += 3 
elif resultado_jogo1_time3 == "Empatou":
    pontos3 += 1

if resultado_jogo2_time3 == "Ganhou":
    pontos3 += 3 
elif resultado_jogo2_time3 == "Empatou":
    pontos3 += 1



if pontos1 > pontos2 and pontos1 > pontos3:
    if pontos2 > pontos3:
        print(f"Parabéns aos países {nome_time_1} e {nome_time_2}, vocês estão classificados para as oitavas de finais!!!")
    else:
        print(f"Parabéns aos países {nome_time_1} e {nome_time_3}, vocês estão classificados para as oitavas de finais!!!")

elif pontos2 > pontos1 and pontos2 > pontos3:
    if pontos1 > pontos3:
        print(f"Parabéns aos países {nome_time_1} e {nome_time_2}, vocês estão classificados para as oitavas de finais!!!")
    else:
        print(f"Parabéns aos países {nome_time_2} e {nome_time_3}, vocês estão classificados para as oitavas de finais!!!")

elif pontos3 > pontos1 and pontos3 > pontos2:
    if pontos1 > pontos2:
        print(f"Parabéns aos países {nome_time_1} e {nome_time_3}, vocês estão classificados para as oitavas de finais!!!")
    else:
        print(f"Parabéns aos países {nome_time_2} e {nome_time_3}, vocês estão classificados para as oitavas de finais!!!")




