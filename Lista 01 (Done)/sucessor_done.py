sim = True
nao = False

nome_narrador_1 = str(input())
bordao_narrador_1 = str(input())
e_carismatico_narrador_1 = str(input())

if e_carismatico_narrador_1 == "sim":
    e_carismatico_narrador_1 = True
else:
    e_carismatico_narrador_1 = False


emocao_narrador_1 = int(input())
pontuacao_1 = 0

nome_narrador_2 = str(input())
bordao_narrador_2 = str(input())
e_carismatico_narrador_2 = str(input())

if e_carismatico_narrador_2 == "sim":
    e_carismatico_narrador_2 = True
else:
    e_carismatico_narrador_2 = False

emocao_narrador_2 = int(input())
pontuacao_2 = 0


pontuacao_1 =+ emocao_narrador_1

if e_carismatico_narrador_1 == True:
    pontuacao_1 += 10

if bordao_narrador_1 == "PROOOO FUNDO DO GOOOL":
    pontuacao_1 += 15
elif bordao_narrador_1 == "EU QUERO É GRITAR GOL":
    pontuacao_1 -= 10
elif bordao_narrador_1 == "VOCÊ. É. RIDÍCULO":
    pontuacao_1 += 18
elif bordao_narrador_1 == "QUEM SABE NA BOLA PARADA":
    pontuacao_1 -= 5
else: 
    pontuacao_1 += 10

pontuacao_2 =+ emocao_narrador_2

if e_carismatico_narrador_2 == True:
    pontuacao_2 += 10

if bordao_narrador_2 == "PROOOO FUNDO DO GOOOL":
    pontuacao_2 += 15
elif bordao_narrador_2 == "EU QUERO É GRITAR GOL":
    pontuacao_2 -= 10
elif bordao_narrador_2 == "VOCÊ. É. RIDÍCULO":
    pontuacao_2 += 18
elif bordao_narrador_2 == "QUEM SABE NA BOLA PARADA":
    pontuacao_2 -= 5
else: 
    pontuacao_2 += 10

if pontuacao_1 > pontuacao_2:
    print(f'O(a) narrador(a) escolhido(a) é {nome_narrador_1}! Ele(a) será um(a) sucessor(a) digno(a) para o grande Galvão.')
else:
    print(f'O(a) narrador(a) escolhido(a) é {nome_narrador_2}! Ele(a) será um(a) sucessor(a) digno(a) para o grande Galvão.')


