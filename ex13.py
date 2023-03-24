a = input('Digite uma lista de números separados por vírgula: ')
a = a.split(',')
a = [int(i) for i in a]


if len(a) < 2:
    print('A lista deve ter pelo menos dois números.')
else:
    ale = sorted(a, reverse=True)
    doisnum = ale[1]

    print('O segundo número mais alto é:', doisnum)