vel = int(input('Qual a velocidade do carro ? '))
multa = (vel - 80) * 7
if vel > 80:
    print('''Você estava a {} sendo que o limite é de 80 
portanto devera pagar uma multa de R${} '''.format(vel, multa))

print('Dentro do limite de velocidade')
