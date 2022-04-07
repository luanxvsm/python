golsFla = int(input('Digite a quantidade de gols do flamengo:'))
golsVas = int(input('digite a quantidade de gols do vasco:'))

if golsFla > golsVas:
    print('O flamengo venceu!!')
elif golsVas > golsFla:
    print('O vasco venceu!!')
else:
    print('A partida terminou empatada')
