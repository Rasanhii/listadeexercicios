#Daqui eu estou fazendo de casa e testando a função split()
a = input('Digite uma lista de números separados por vírgula: ')
a = a.split(',')
a = [int(i) for i in a]

for n in a:
    if n > 10:
        print(n)