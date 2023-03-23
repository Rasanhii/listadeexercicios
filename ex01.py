comoassim = []

while True:
    numeros = int(input("Insira um numero para acrescentar a lista: "))
    comoassim.append(numeros)
    fim = input("Deseja inserir novos números? Digite 's' para sim ou 'n' para não: ")
    if fim.lower() == 'n':
        break
numeros_pares = []
for i in comoassim:
    if i%2 == 0:
        numeros_pares.append(i)

print('Os numeros pares são:', numeros_pares)