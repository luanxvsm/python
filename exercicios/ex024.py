morangos = int(input('Digite a quantidade de morangos [kg]: '))
macas = int(input('Digite a quantidade de maças [kg]: '))
precoMorango1 = morangos * 2.00
precoMorango2 = morangos * 1.80

precoMaca1 = macas * 1.50
precoMaca2 = macas * 1.10

print('quantidade de maçãs: ', macas,'kg')
print('Quantidade de morangos: ', morangos,'kg')

if morangos > 5:
    precoCertoMorango = precoMorango1
else:
    precoCertoMorango = precoMorango2

if macas > 5:
    precoCertoMaca = precoMaca1
else:
    precoCertoMaca = precoMaca2

precoTotal = precoCertoMaca + precoCertoMorango

if precoTotal > 25 or (macas + morangos) > 8:
    print('Preço final R$', (precoTotal - (precoTotal * 0.1)))
else:
    print('Preço final R$', precoTotal)
