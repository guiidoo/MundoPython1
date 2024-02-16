salario=float(input('Qual o salario ? '))
if salario > 1250:
    sup = salario (salario * 10/100)
    print('Seu salario de {} teve um aumento de 10% e esta {} '.format(salario, sup))
else:
    sup = salario + (salario * 15/100)
    print('Seu salario de {} teve um aumento de 15% e esta {} '.format(salario, sup))
