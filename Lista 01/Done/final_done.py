nome_A = str(input())
ataque_A = int(input())
defesa_A = int(input())
folego_A = int(input())

nome_B = str(input())
ataque_B = int(input())
defesa_B = int(input())
folego_B = int(input())

sorte_1 = int(input())
sorte_2 = int(input())
sorte_3 = int(input())
sorte_4 = int(input())

gols_A = 0
gols_B = 0

Turno1 = True
Turno2, Turno3, Turno4, Final = False, False, False, False

canseira_A = 1 - ((5 - folego_A) / 10)
canseira_B = 1 - ((5 - folego_B) / 10)

if Turno1:
    print("Início de jogo!")
    print("1° tempo:")
    print(f"{nome_A} [{gols_A}-{gols_B}] {nome_B}")
    print(f"O time {nome_A} vem pressionando.")

    if sorte_1 == 1:
        ataque_A += 2

    if sorte_1 == 2:
        defesa_B += 2

    if ataque_A >= defesa_B:
        gols_A += 1
        print(f"GOOOOOOOOOOOOLLLLLL DO TIME {nome_A}!!!")
        if sorte_1 == 1:
            ataque_A -= 2
        if sorte_1 == 2: 
            defesa_B -= 2
    else:
        print(f"O ataque é interrompido! Ótima defesa do time {nome_B}")
        if sorte_1 == 1:
            ataque_A -= 2
        if sorte_1 == 2: 
            defesa_B -= 2

    Turno1 = False
    Turno2 = True

if Turno2:
    print(f"O time {nome_B} vem pressionando.")

    ataque_A = ataque_A * canseira_A
    defesa_A = defesa_A * canseira_A
    ataque_B = ataque_B * canseira_B
    defesa_B = defesa_B * canseira_B

    if sorte_2 == 1:
        ataque_B += 2

    if sorte_2 == 2:
        defesa_A += 2

    if ataque_B >= defesa_A:
        gols_B += 1
        print(f"GOOOOOOOOOOOOLLLLLL DO TIME {nome_B}!!!")
        if sorte_2 == 1:
            ataque_B -= 2
        if sorte_2 == 2: 
            defesa_A -= 2
    else:
        print(f"O ataque é interrompido! Ótima defesa do time {nome_A}")
        if sorte_2 == 1:
            ataque_B -= 2
        if sorte_2 == 2: 
            defesa_A -= 2

    Turno2 = False
    Turno3 = True

if Turno3:
    print("2° tempo:")
    print(f"{nome_A} [{gols_A}-{gols_B}] {nome_B}")
    print(f"O time {nome_B} vem pressionando.")

    ataque_A = ataque_A * canseira_A
    defesa_A = defesa_A * canseira_A
    ataque_B = ataque_B * canseira_B
    defesa_B = defesa_B * canseira_B

    if sorte_3 == 1:
        ataque_B += 2

    if sorte_3 == 2:
        defesa_A += 2

    if ataque_B >= defesa_A:
        gols_B += 1
        print(f"GOOOOOOOOOOOOLLLLLL DO TIME {nome_B}!!!")
        if sorte_3 == 1:
            ataque_B -= 2
        if sorte_3 == 2: 
            defesa_A -= 2
    else:
        print(f"O ataque é interrompido! Ótima defesa do time {nome_A}")
        if sorte_3 == 1:
            ataque_B -= 2
        if sorte_3 == 2: 
            defesa_A -= 2

    Turno3 = False
    Turno4 = True

if Turno4:
    print(f"O time {nome_A} vem pressionando.")

    ataque_A = ataque_A * canseira_A
    defesa_A = defesa_A * canseira_A
    ataque_B = ataque_B * canseira_B
    defesa_B = defesa_B * canseira_B

    if sorte_4 == 1:
        ataque_A += 2
        reset_A = True

    if sorte_4 == 2:
        defesa_B += 2
        reset_B = True

    if ataque_A >= defesa_B:
        gols_A += 1
        print(f"GOOOOOOOOOOOOLLLLLL DO TIME {nome_A}!!!")
    else:
        print(f"O ataque é interrompido! Ótima defesa do time {nome_B}")

    Turno4 = False
    Final = True

if Final:
    print(f"{nome_A} [{gols_A}-{gols_B}] {nome_B}")

    if gols_A > gols_B:
        print(f"ACABOOOOU!! O TIME {nome_A} É O CAMPEÃO!!!")
    elif gols_B > gols_A:
        print(f"Fim de jogo! O time {nome_B} é campeão.")
    else:
        print("Temos um empate! Será decidido em breve nos pênaltis. Fique ligado!")
