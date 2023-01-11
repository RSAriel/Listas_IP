nome1 = str(input())
bolas_area1 = int(input())
finalizacoes1 = int(input())
gols1 = int(input())

if finalizacoes1 == 0:
    aproveitamento1 = 0
else:
    aproveitamento1 = gols1 / finalizacoes1

nome2 = str(input())
bolas_area2 = int(input())
finalizacoes2 = int(input())
gols2 = int(input())

if finalizacoes2 == 0:
    aproveitamento2 = 0 
else:
    aproveitamento2 = gols2 / finalizacoes2

nome3 = str(input())
bolas_area3 = int(input())
finalizacoes3 = int(input())
gols3 = int(input())

if finalizacoes3 == 0:
    aproveitamento3 = 0
else:
    aproveitamento3 = gols3 / finalizacoes3

melhor1= nome1
melhor2= nome2
melhor3= nome3

bom = False

if bolas_area1 == bolas_area2 and bolas_area2 == bolas_area3 and bolas_area3 == bolas_area1:
    print("Tite está mais indeciso do que nunca!")
    if aproveitamento1 > aproveitamento2 and aproveitamento2 > aproveitamento3: 
        melhor1 = nome1
        melhor2 = nome2
        melhor3 = nome3
        if bolas_area1 > 10: bom = True
        else: bom = False
    elif aproveitamento1 > aproveitamento3 and aproveitamento3 > aproveitamento2: 
        melhor1 = nome1
        melhor2 = nome3
        melhor3 = nome2
        if bolas_area1 > 10: bom = True
        else: bom = False
    elif aproveitamento2 > aproveitamento3 and aproveitamento3 > aproveitamento1: 
        melhor1 = nome2
        melhor2 = nome3
        melhor3 = nome1
        if bolas_area2 > 10: bom = True
        else: bom = False
    elif aproveitamento2 > aproveitamento1 and aproveitamento1 > aproveitamento3:      
        melhor1 = nome2
        melhor2 = nome1
        melhor3 = nome3 
        if bolas_area2 > 10: bom = True
        else: bom = False
    elif aproveitamento3 > aproveitamento1 and aproveitamento1 > aproveitamento2:
        melhor1 = nome3
        melhor2 = nome1
        melhor3 = nome2
        if bolas_area3 > 10: bom = True
        else: bom = False
    elif aproveitamento3 > aproveitamento2 and aproveitamento2 > aproveitamento1:
        melhor1 = nome3
        melhor2 = nome2
        melhor3 = nome1
        if bolas_area3 > 10: bom = True
        else: bom = False

elif bolas_area1 != bolas_area2 and bolas_area1 != bolas_area3 and bolas_area2 != bolas_area3: 
    if bolas_area1 > bolas_area2 and bolas_area1 > bolas_area3:
        melhor1 = nome1
        if bolas_area1 > 10: bom = True
        else: bom = False
        if bolas_area2 > bolas_area3:
            melhor2 = nome2
            melhor3 = nome3
        else:
            melhor2 = nome3
            melhor3 = nome2 
    # 1 > 2 > 3
    # 1 > 3 > 2
    elif bolas_area2 > bolas_area1 and bolas_area2 > bolas_area3:
        melhor1 = nome2
        if bolas_area2 > 10: bom = True
        else: bom = False
        if bolas_area1 > bolas_area3:
            melhor2 = nome1
            melhor3 = nome3
        else:
            melhor2 = nome3
            melhor3 = nome1
    # 2 > 1 > 3
    # 2 > 3 > 1
    elif bolas_area3 > bolas_area1 and bolas_area3 > bolas_area2:
        melhor1 = nome3
        if bolas_area3 > 10: bom = True
        else: bom = False
        if bolas_area1 > bolas_area2:
            melhor2 = nome1
            melhor3 = nome2
        else:
            melhor2 = nome2
            melhor3 = nome1
    # 3 > 1 > 2
    # 3 > 2 > 1

elif bolas_area1 == bolas_area2:

    if bolas_area1 > bolas_area3:
        print("Tite está mais indeciso do que nunca!")
        if aproveitamento1 > aproveitamento2:
            melhor1 = nome1
            melhor2 = nome2
            melhor3 = nome3
            if bolas_area1 > 10: bom = True
            else: bom = False
        if aproveitamento2 > aproveitamento1:
            melhor1 = nome2
            melhor2 = nome1
            melhor3 = nome3
            if bolas_area2 > 10: bom = True
            else: bom = False
    elif bolas_area3 > bolas_area1:  
        if aproveitamento1 > aproveitamento2:
            melhor1 = nome3
            melhor2 = nome1
            melhor3 = nome2
            if bolas_area3 > 10: bom = True
            else: bom = False
        if aproveitamento2 > aproveitamento1:
            melhor1 = nome3
            melhor2 = nome2
            melhor3 = nome1
            if bolas_area3 > 10: bom = True
            else: bom = False

elif bolas_area1 == bolas_area3:

    if bolas_area1 > bolas_area2:
        print("Tite está mais indeciso do que nunca!")
        if aproveitamento1 > aproveitamento3:
            melhor1 = nome1
            melhor2 = nome3
            melhor3 = nome2
            if bolas_area1 > 10: bom = True
            else: bom = False
        if aproveitamento3 > aproveitamento1:
            melhor1 = nome3
            melhor2 = nome1
            melhor3 = nome2
            if bolas_area3 > 10: bom = True
            else: bom = False
    elif bolas_area2 > bolas_area1:
        if aproveitamento1 > aproveitamento3:
            melhor1 = nome2
            melhor2 = nome1
            melhor3 = nome3
            if bolas_area2 > 10: bom = True
            else: bom = False
        if aproveitamento3 > aproveitamento1:
            melhor1 = nome2
            melhor2 = nome3
            melhor3 = nome1
            if bolas_area2 > 10: bom = True
            else: bom = False   

elif bolas_area2 == bolas_area3:

    if bolas_area2 > bolas_area1:
        print("Tite está mais indeciso do que nunca!")
        if aproveitamento2 > aproveitamento3:
            melhor1 = nome2
            melhor2 = nome3
            melhor3 = nome1
            if bolas_area2 > 10: bom = True
            else: bom = False
        if aproveitamento3 > aproveitamento2:
            melhor1 = nome3
            melhor2 = nome2
            melhor3 = nome1
            if bolas_area3 > 10: bom = True
            else: bom = False
    if bolas_area1 > bolas_area2:
        
        if aproveitamento2 > aproveitamento3:
            melhor1 = nome1
            melhor2 = nome2
            melhor3 = nome3
            if bolas_area1 > 10: bom = True
            else: bom = False
        if aproveitamento3 > aproveitamento2:
            melhor1 = nome1
            melhor2 = nome3
            melhor3 = nome2
            if bolas_area1 > 10: bom = True
            else: bom = False    


print(melhor1)
print(melhor2)  
print(melhor3)
print("Finalmente o técnico da seleção brasileira liberou a escalação completa do time! O ponta-direita escolhido foi…") 
if bom == True:
    print(f"{melhor1}! Dessa vez o hexa vem pra casa!!")  
elif bom == False:
    print(f"{melhor1}?! Sei não hein Galvão…")
        


