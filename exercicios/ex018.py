n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

if (n3 < n1) and (n1 < n2):
    print (n1 + n2)
elif (n2 < n1) and (n1 < n3):
    print (n1 + n3)
else:
    print (n2 + n3)
    
