a = input('Digite uma lista de números separados por vírgula: ')
a = a.split(',')
a = [int(i) for i in a]

tres = []

for i in a:
    if i % 3 == 0:
        tres.append(i)

# Imprime a lista de números divisíveis por 3
print('Os números divisíveis por 3 são:', tres)