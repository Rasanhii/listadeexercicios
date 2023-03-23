a = []

while True:
    numeros = int(input("Insira um numero para acrescentar a lista: "))
    a.append(numeros)
    fim = input("Deseja inserir novos números? Digite 's' para sim ou 'n' para não: ")
    if fim.lower() == 'n':
        break

logica = sum(a)
saber = len(a)
print('A média é de: ',logica/saber)
