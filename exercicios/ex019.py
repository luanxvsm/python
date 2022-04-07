n1 = int(input('Digite uma medida: '))
n2 = int(input('Digite outra medida: '))
n3 = int(input('Digite mais uma medida: '))

s1 = n1+n2
s2 = n1+n3
s3 = n2+n3

if n1 < s3 and n2 < s2 and n3 < s1:
    print('Essas medidas formam um triângulo')
else:
    print('Essas medidas não formam um triângulo')
