n1 = int(input('Digite a sua primeira norta: '))
n2 = int(input('Digite a sua segunda norta: '))
n3 = int(input('Digite a sua terceira norta: '))
mediaExercicios = int(input('Digite a média dos exercícios: '))

mediaDeAproveitamento = (n1 + n2*2 + n3*3 + mediaExercicios)/7

if mediaDeAproveitamento >= 9:
    print('Você teve nota conceito A')
elif mediaDeAproveitamento >= 7.5 and mediaDeAproveitamento < 9:
    print('Você teve nota conceito B')
elif mediaDeAproveitamento >= 6 and mediaDeAproveitamento < 7.5:
    print('Você teve nota conceito C')
else:
    print('Você teve nota conceito D')

