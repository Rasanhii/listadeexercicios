banana = []

while True:
    palavra = input("Insira uma palavra para acrescentar a lista: ")
    banana.append(palavra)
    fim = input("Deseja inserir novos números? Digite 's' para sim ou 'n' para não: ")
    if fim.lower() == 'n':
        break

chuva = []
for i in banana:
    if i[0] == 'a':
        chuva.append(i)

print('As palavras que começam com "a" são:',chuva)