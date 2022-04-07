time1 = input('Digite o nome de um time: ')
time2 = input('Digite o nome de outro time: ')
gols1 = int(input('Quantidade de gols do primeiro time: '))
gols2 = int(input('Quantidade de gols do segundo time: '))

if gols1 > gols2:
    print('O time vencedor foi o:', time1)
elif gols2 > gols1:
    print('O time vencedor foi o:', time2)
else:
    print('A partida terminou empate')
