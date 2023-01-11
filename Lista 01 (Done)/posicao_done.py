nome = str(input())

goleiros = ('Alisson', 'Ederson', 'Weverton')
zagueiros = ('Marquinhos', 'Thiago Silva', 'Éder Militão', 'Bremer')
laterais = ('Daniel Alves', 'Danilo', 'Alex Sandro', 'Alex Telles')
meias = ('Casemiro', 'Fabinho', 'Fred', 'Bruno Guimarães', 'Lucas Paquetá', 'Everton Ribeiro')
atacantes = ('Neymar', 'Raphinha', 'Vini Jr.', 'Antony', 'Richarlison', 'Rodrygo', 'Pedro', 'Gabriel Jesus', 'Gabriel Martinelli')

if nome in goleiros:
    posicao = "goleiro"
elif nome in laterais:
    posicao = "lateral"
elif nome in zagueiros:
    posicao = "zagueiro"
elif nome in meias:
    posicao = "meia"
elif nome in atacantes:
    posicao = "atacante"
else:
    posicao = "não foi convocado"

if posicao == "não foi convocado":
    print (f'{nome} {posicao}, mas quem sabe na próxima?')
else:
    print (f'{nome} foi convocado e jogará como {posicao}!')

