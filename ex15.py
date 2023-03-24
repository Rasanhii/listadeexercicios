a = input('Digite uma lista de números separados por vírgula: ')
a = a.split(',')
a = [int(i) for i in a]

unique = []
for i in a:
    if i not in unique:
        unique.append(i)

print('A nova lista de números sem duplicatas é:', unique)