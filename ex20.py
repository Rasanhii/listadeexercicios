palavras = input("Digite uma lista de palavras separadas por virgula: ").split(',')
new_list = []

for i in palavras:
    if len(i) % 2 != 0:
        new_list.append(i)

print("Palavras com número ímpar de letras:", new_list)