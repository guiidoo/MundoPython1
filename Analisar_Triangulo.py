print('-=-' * 10)
print('Analisador de triângulos')
print('-=-' * 10)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1< r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos {}, {}, {} podem formar um triangulo'.format(r1,r2,r3))
else:
    print('Os segmentos {}, {}, {} não podem formar um triangulo'.format(r1,r2,r3))