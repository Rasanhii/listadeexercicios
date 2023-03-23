a = []

while True:
    numeros = input("Insira um numero para acrescentar a lista: ")
    a.append(numeros)
    fim = input("Deseja inserir novos números? Digite 's' para sim ou 'n' para não: ")
    if fim.lower() == 'n':
        break

maior = max(a)
menor = min(a)

print(maior)
print(menor)