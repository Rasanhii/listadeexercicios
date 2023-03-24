#Mds como fica mais fácil
a = input('Digite uma lista de números separados por vírgula: ')
a = a.split(',')
a = [int(i) for i in a]
this_is_where = input('Digite o nome que deseja verificar na lista: ')

if this_is_where in a:
    print('O nome está na lista')
else:
    print('O nome não está na lista')