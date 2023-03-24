a = input('Digite uma lista de números separados por vírgula: ')
a = a.split(',')
a = [int(i) for i in a]

in_my_mind = list(set(a))

print('A lista sem duplicatas é:', in_my_mind)
