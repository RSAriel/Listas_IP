ganhou1, ganhou2, ganhou3, ganhou4 = False, False, False, False 


FavoritismoBr = int(input())

NomeOp1 = str(input())
FavoritismoOP1 = int(input())
GolsBr1 = int(input())
GolsOp1 = int(input())

if GolsBr1 > GolsOp1:
    if GolsBr1 - GolsOp1 < 3:
        FavoritismoBr += (GolsBr1 - GolsOp1)*10
    else: FavoritismoBr += 30
    print("Quem é que segura o Brasil???")
    ganhou1 = True
    
elif GolsBr1 == GolsOp1:
    if FavoritismoBr > FavoritismoOP1 or FavoritismoBr == FavoritismoOP1:
        print("No sufoco, o Brasil conseguiu ganhar!!!")
        ganhou1 = True
    else:
        print("Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...")

else: print(f"Infelizmente essa seleção dx {NomeOp1} era muito forte para o Brasil.")


if ganhou1:

    NomeOp2 = str(input())
    FavoritismoOP2 = int(input())
    GolsBr2 = int(input())
    GolsOp2 = int(input())

    if GolsBr2 > GolsOp2:
        if GolsBr2 - GolsOp2 <3:
            FavoritismoBr += (GolsBr2 - GolsOp2)*10
        else: FavoritismoBr += 30

        print("Quem é que segura o Brasil???")
        ganhou2 = True
    elif GolsBr2 == GolsOp2:
        if FavoritismoBr > FavoritismoOP2 or FavoritismoBr == FavoritismoOP2:
            print("No sufoco, o Brasil conseguiu ganhar!!!")
            ganhou2 = True
        else:
            print("Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...")
    else: print(f"Infelizmente essa seleção dx {NomeOp2} era muito forte para o Brasil.")


if ganhou2:

    NomeOp3 = str(input())
    FavoritismoOP3 = int(input())
    GolsBr3 = int(input())
    GolsOp3 = int(input())

    if GolsBr3 > GolsOp3:
        if GolsBr3 - GolsOp3 <3:
            FavoritismoBr += (GolsBr3 - GolsOp3)*10
        else: FavoritismoBr += 30

        print("Quem é que segura o Brasil???")
        ganhou3 = True
    elif GolsBr3 == GolsOp3:
        if FavoritismoBr > FavoritismoOP3 or FavoritismoBr == FavoritismoOP3:
            print("No sufoco, o Brasil conseguiu ganhar!!!")
            ganhou3 = True
        else:
            print("Foi no detalhe! Mas infelizmente o Brasil esta eliminado da copa...")
    else: print(f"Infelizmente essa seleção dx {NomeOp3} era muito forte para o Brasil.")


if ganhou3:

    NomeOp4 = str(input())
    FavoritismoOP4 = int(input())

    if FavoritismoBr > FavoritismoOP4 or FavoritismoBr == FavoritismoOP4:
        print("O BRASIL VAI SER HEXAAAAAAAA")
    else: print(f"O nosso Brasil foi vice, não conseguindo bater a seleção dx {NomeOp4} na simulação")




