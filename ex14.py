a = input('Digite uma lista de números separados por vírgula: ')
a = a.split(',')
a = [int(i) for i in a]

abacate = sorted(a)
anao = abacate[1]

print('O segundo número mais baixo é:', anao)