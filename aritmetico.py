#nome = input('Qual seu nome ? ')
#print('Prazer em conhecer você {:=^20}!', format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
s= n1+n2
su= n1-n2
m= n1*n2
di= n1/n2
d= n1//n2
po= n1**n2

print('A soma vale: {}, A Subtração vale: {}, A multiplicação vale: {} '.format(s, su, m), end='>>>>')
print(' A divisão vale: {:.2f}, A divisão por inteiro vale: {}'.format(di, d, po))