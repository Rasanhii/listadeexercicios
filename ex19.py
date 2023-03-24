b = int(input('Digite o número pelo qual deseja dividir: '))
a = input('Digite uma lista de números separados por vírgula: ')
a = a.split(',')
a = [int(i) for i in a]

c = []

for i in a:
    if i % a == 0:
        c.append(i)

print('Os números divisíveis por', b, 'são:', c)