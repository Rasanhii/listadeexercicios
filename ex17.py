a = input('Digite uma lista de números separados por vírgula: ')
a = a.split(',')
a = [int(i) for i in a]

estamos = []

for i in a:
        estamos.append(i)

print('Os nomes que contêm a letra "e" são:', estamos)