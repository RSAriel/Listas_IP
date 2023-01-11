nome1 = str(input())
nome2 = str(input())

lances = 0
gols_time1 = 0
gols_time2 = 0

#1
lance_time1 = str(input())
lances += 1

if lance_time1 == "Gol":
    gols_time1 += 1


#2
lance_time2 = str(input())
lances += 1

if lance_time2 == "Gol":
    gols_time2 += 1


#3
lance_time1 = str(input())
lances += 1

if lance_time1 == "Gol":
    gols_time1 += 1


#4
lance_time2 = str(input())
lances += 1

if lance_time2 == "Gol":
    gols_time2 += 1


#5
lance_time1 = str(input())
lances += 1

if lance_time1 == "Gol":
    gols_time1 += 1


#6
lance_time2 = str(input())
lances += 1

if lance_time2 == "Gol":
    gols_time2 += 1



if gols_time1 == 3 and gols_time2 == 0:
    print(f'{nome1} vence a disputa de pênaltis por {gols_time1} a {gols_time2} e avança de fase!')
elif gols_time2 == 3 and gols_time1 == 0:
    print(f'{nome2} vence a disputa de pênaltis por {gols_time2} a {gols_time1} e avança de fase!')
else:
    
    #7
    lance_time1 = str(input())
    lances += 1

    if lance_time1 == "Gol":
        gols_time1 += 1

    if gols_time1 == 4 and gols_time2 <= 1:
        print(f'{nome1} vence a disputa de pênaltis por {gols_time1} a {gols_time2} e avança de fase!')
    elif gols_time1 <= 1 and gols_time2 == 3:
        print(f'{nome2} vence a disputa de pênaltis por {gols_time2} a {gols_time1} e avança de fase!')
    else:
        #8
        lance_time2 = str(input())
        lances += 1

        if lance_time2 == "Gol":
            gols_time2 += 1

        if gols_time1 > gols_time2 + 1 :
            print(f'{nome1} vence a disputa de pênaltis por {gols_time1} a {gols_time2} e avança de fase!')
        elif gols_time2 > gols_time1 + 1:
            print(f'{nome2} vence a disputa de pênaltis por {gols_time2} a {gols_time1} e avança de fase!')
        else:
            #9
            lance_time1 = str(input())
            lances += 1

            if lance_time1 == "Gol":
                gols_time1 += 1    

            if (gols_time1 == 5 and gols_time2 == 3) or (gols_time1 == 4 and gols_time2 == 2) or (gols_time1 == 3 and gols_time2 == 1) or (gols_time1 == 2 and gols_time2 == 0): 
                print(f'{nome1} vence a disputa de pênaltis por {gols_time1} a {gols_time2} e avança de fase!')
            elif (gols_time2 == 4 and gols_time1 == 3) or (gols_time2 == 3 and gols_time1 == 2) or (gols_time2 == 2 and gols_time1 == 1) or (gols_time2 == 1 and gols_time1 == 0):
                print(f'{nome2} vence a disputa de pênaltis por {gols_time2} a {gols_time1} e avança de fase!')
            else:
                #10
                lance_time2 = str(input())
                lances += 1

                if lance_time2 == "Gol":
                    gols_time2 += 1

                if gols_time1 > gols_time2:
                    print(f"{nome1} vence a disputa de pênaltis por {gols_time1} a {gols_time2} e avança de fase!")
                if gols_time2 > gols_time1:
                    print(f"{nome2} vence a disputa de pênaltis por {gols_time2} a {gols_time1} e avança de fase!")
                elif gols_time1 == gols_time2:
                    print(f"Ambas as seleções terminaram com {gols_time2} gols, mas o desempate vai ficar para outro dia.")
                   
