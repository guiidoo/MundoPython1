'''co= float(input('Qual o valor do cateto oposto ? '))
ca=float(input('Qual o comprimento de cateto adiacente ? '))
hi=(co**2+ca**2)**(1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

import math

co= float(input('Qual o valor do cateto oposto ? '))
ca=float(input('Qual o comprimento de cateto adiacente ? '))
hi= math.hypot(ca,co)
print('A hipotenusa vai medir {:.2f}'.format(hi))