a = input('Digite uma lista de números separados por vírgula: ')
a = a.split(',')
a = [int(i) for i in a]

dupla = []
unique = []
for i in a:
    if i in unique:
        dupla.append(i)
    else:
        unique.append(i)


print('Os números que aparecem mais de uma vez na lista original são:', dupla)