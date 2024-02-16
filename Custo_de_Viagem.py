num = int(input('Qual a distancia em Km ? '))
#preço = num * 0.50 if num<=200 else num * 0.45 (versão simplificada)
if num <= 200:
    preço = num * 0.50
else:
    preço = num * 0.45

print('O preço para sua passagem será de R${}'.format(preço))