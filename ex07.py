a = []

while True:
    numeros = input("Insira um palavra para acrescentar a lista: ")
    a.append(numeros)
    fim = input("Deseja inserir novos números? Digite 's' para sim ou 'n' para não: ")
    if fim.lower() == 'n':
        break

maior = ""
menor = a[0]
zero = 0
for i in a:
    if len(i) > len(maior):
        maior = i
    if len(i) < len(menor):
        menor = i

print('O maior nome é:',maior)
print('O menor nome é:',menor)