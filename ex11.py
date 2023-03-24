a = input('Digite uma lista de números separados por vírgula: ')
a = a.split(',')
a = [int(i) for i in a]
in_my_head = 0

for i in a:
    if int(i) % 2 != 0:
        in_my_head += int(i)

print('A soma de todos os números ímpares na lista é: ', in_my_head)