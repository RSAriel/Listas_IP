letra_sorteada = str(input())
quantidade_amigos = int(input())
estado_preferencia = str(input())
number = 0
numero_maior = 0
estado = 0
for i in range (quantidade_amigos):
    
    nome_amigo = str(input())
    estado_amigo = str(input())

    for letra in estado_amigo:
        if letra == letra_sorteada:
            number += 1 

    if numero_maior == 0:
        numero_maior = number
        estado = estado_amigo
        number = 0

    if numero_maior < number:
        numero_maior = number
        estado = estado_amigo
        number = 0

    if numero_maior == number:
       estado = estado_amigo
       number = 0
    

if estado_preferencia == estado:
    print(f"UHUL!!! Victor vai começar por {estado_preferencia} que é o estado que ele queria e ficara la por {numero_maior} dias.")

if estado_preferencia != estado:
    print(f"Eita!!! infelizmente, Victor terá que fazer uma viagem maior e começar pelo estado {estado} e ficara la por {numero_maior} dias.")
