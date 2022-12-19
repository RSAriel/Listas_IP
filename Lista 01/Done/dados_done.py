ano = int(input())

nome_selecao1 = str(input())
vitorias_time1 = int(input())
empates_time1 = int(input())
pontos1= (vitorias_time1 * 3) + empates_time1

nome_selecao2 = str(input())
vitorias_time2 = int(input())
empates_time2 = int(input())
pontos2 = (vitorias_time2 * 3) + empates_time2

nome_selecao3 = str(input())
vitorias_time3 = int(input())
empates_time3 = int(input())
pontos3 = (vitorias_time3 * 3) + empates_time3

tipo_consulta = str(input())

if tipo_consulta == "Critério Geral":
    if pontos1 > pontos2:
        if pontos1 > pontos3:
            lugar1 = nome_selecao1
            pontof1 = pontos1
            if pontos2 > pontos3:
                lugar2 = nome_selecao2
                pontof2 = pontos2
                lugar3 = nome_selecao3
                pontof3 = pontos3
            else:
                lugar2 = nome_selecao3
                pontof2 = pontos3
                lugar3 = nome_selecao2
                pontof3 = pontos2
        else:
            lugar1 = nome_selecao3
            pontof1 = pontos3
            lugar2 = nome_selecao1
            pontof2 = pontos1
            lugar3 = nome_selecao2 
            pontof3 = pontos2

    elif pontos2 > pontos3:
        if pontos2 > pontos1:
            lugar1 = nome_selecao2
            pontof1 = pontos2
            if pontos1 > pontos3:
                lugar2 = nome_selecao1
                pontof2 = pontos1
                lugar3 = nome_selecao3
                pontof3 = pontos3
            else:
                lugar2 = nome_selecao3
                pontof2 = pontos3
                lugar3 = nome_selecao1
                pontof3 = pontos1

    else: 
        lugar1 = nome_selecao3
        pontof1 = pontos3
        lugar2 = nome_selecao2
        pontof2 = pontos2
        lugar3 = nome_selecao1
        pontof3 = pontos1

if tipo_consulta == "Ordem Lexicográfica":
    if nome_selecao1 > nome_selecao2:
        if nome_selecao1 > nome_selecao3:
            terceiro = nome_selecao1
            pontof3 = pontos1
            if nome_selecao2 > nome_selecao3:
                segundo = nome_selecao2
                pontof2 = pontos2
                primeiro = nome_selecao3
                pontof1 = pontos3
            else:
                segundo = nome_selecao3
                pontof2 = pontos3
                primeiro = nome_selecao2
                pontof1 = pontos2
        else:
            terceiro = nome_selecao3
            pontof3 = pontos3
            segundo = nome_selecao1
            pontof2 = pontos1
            primeiro = nome_selecao2 
            pontof1 = pontos2

    elif nome_selecao2 > nome_selecao3:
        if nome_selecao2 > nome_selecao1:
            terceiro = nome_selecao2
            pontof3 = pontos2
            if nome_selecao1 > nome_selecao3:
                segundo = nome_selecao1
                pontof2 = pontos1
                primeiro = nome_selecao3
                pontof1 = pontos3
            else:
                segundo = nome_selecao3
                pontof2 = pontos3
                primeiro = nome_selecao1
                pontof1 = pontos1
    else: 
        terceiro = nome_selecao3
        pontof3 = pontos3
        segundo = nome_selecao2
        pontof2 = pontos2
        primeiro = nome_selecao1
        pontof1 = pontos1


if tipo_consulta == "Critério Geral":
    print(f"A classificação na copa de {ano} foi:")
    print(f"{lugar1} - {pontof1}")
    print(f"{lugar2} - {pontof2}")
    print(f"{lugar3} - {pontof3}")

if tipo_consulta == "Ordem Lexicográfica":
    print(f"O times por ordem Lexicográfica da copa de {ano} são:")
    print(f"{primeiro} - {pontof1}")
    print(f"{segundo} - {pontof2}")
    print(f"{terceiro} - {pontof3}")
