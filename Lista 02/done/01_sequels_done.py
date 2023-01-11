quantidade_jogos = int(input())

for i in range(quantidade_jogos):
    nome = str(input())
    numero_sequencia = int(input())

    if numero_sequencia == 2:
        print ("Achei a sequel! Hora da diversão!")
    else:
        print (f"Achamos {nome} {numero_sequencia}, mas você ainda precisa jogar o ", end= "")
        for i in range (2, numero_sequencia-1):
            print(i, end=", ")
        print(numero_sequencia-1, end="")
        print(" antes desse.")

        
        
        
        
        
        
        
         
