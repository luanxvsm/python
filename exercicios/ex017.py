ano1 = int(input('Em que ano você nasceu? '))
ano2 = int(input('Em que ano estamos? '))
idade = ano2 - ano1

if idade >= 16:
    print('Você ja tem a idade para votar, tire seu título de eleitor e venha fazer o seu papel de cidadão(a)')
else:
    print('Você ainda não tem idade para votar nas eleições')
