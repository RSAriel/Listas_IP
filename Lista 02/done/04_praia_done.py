acao = 0
protetor = False
dinheiro = 0.0
clima= True
while acao != "ir para a praia":
    acao = str(input())

    if acao == "separar dinheiro":
        mais_dinheiro = float(input())
        dinheiro += mais_dinheiro
    if acao == "passar protetor":
        protetor = True
    if acao =="choveu":
        clima = False
    if acao == "parou de chover":
        clima = True
    else:
        continue

if clima == True:
    print("Hoje tem sol e mar!")
    if protetor == False:
        if dinheiro < 10:
            print("Você não chegou muito bem, chame um médico!")
        else:
            print("O novo camarão do CIn foi criado")
    else:
        if dinheiro < 10:
            print("Só faltou uma aguinha de coco...")
        else:
            print("Aí sim! Hoje rendeu!")
else:
    print("Hoje não vai dar pra ir, chuvinha barrou")
    

