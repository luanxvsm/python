num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
acao = int(input('Qual ação você vai querer realizar? '))
cod1 = (num1 + num2)/2
cod2 = num1 - num2
cod3 = num1 * num2
cod4 = num1/num2

if acao == 1:
    print('A média entre os números é:', cod1)
elif acao == 2:
    print('A diferença entre os números é:', cod2)
elif acao == 3:
    print('O produto entre os números é:', cod3)
elif acao == 4:
    print('A divisão entre esses números é:', cod4)
else:
    print('Este código não é válido')
    
