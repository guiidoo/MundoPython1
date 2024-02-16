nome = str(input('Digite seu nome: ')).strip() # tira os espaços
print('Analisando o seu nome....')
print('Seu nome maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('O numero de letras são {}'.format(len(nome) - nome.count(' ')))
#print(('Quantas letra tem o primeiro nome'.format(nome.find(' '))))
separa = nome.split()
print(' Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len (separa[0])))