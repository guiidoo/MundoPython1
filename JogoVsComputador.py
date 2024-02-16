from random import randint
from time import sleep
print('---------Tente adivinhar o número---------')
num = int(input('Digite um numero: '))
n = randint(0,100)
print('-=-' * 20)
print('Processando...')
sleep(2)#faz o computador esperar
if num == n:
    print('Você ganhou !!!')
else:
    print('Voce perdeu para um computador')