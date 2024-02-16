a = int(input('Digite um numero 1: '))
b = int(input('Digite um numero 2: '))
c = int(input('Digite um numero 3: '))

#Menor valor
menor = a
if b<c and b<a:
    menor = b
if c<b and c<a:
    menor = c

#Maior valor
maior = a
if b>c and b>a:
    maior = b
if c>b and c>a:
    maior = c

print('O menor valor digitado é {}'.format(menor))
print('O maior valor digitado é {}'.format(maior))