salario = float(input('Digite o seu salário:'))
aumento1 = 35/100 * salario
aumento2 = 15/100 * salario
reajuste1 = aumento1 + salario
reajuste2 = aumento2 + salario
if salario <= 300:
    print('Você teve um aumento de 35% e seu novo salário é R$', reajuste1)
else:
    print('Você teve um aumento de 15% e seu novo salário é R$', reajuste2)
                
