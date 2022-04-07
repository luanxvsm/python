litros = float(input('Quantos litros você vai querer abastecer? '))
combustivel = input("Digite A para álcool ou G para gasolina: ")
preco = 0

if combustivel == "A" or combustivel == "a":
    preco = litros * 1.9
    if litros <= 20:
        preco -= 1.9 * litros * 3 / 100
    else:
        preco -= 1.9 * litros * 5 / 100
        
elif combustivel == "G" or combustivel == "g":
    preco = litros * 2.5
    if litros <= 20:
        preco -= 2.5 * litros * 4 / 100
    else:
        preco -= 2.5 * litros * 6 / 100
        
print(f"O preço a pagar é R${preco:.2f}")
