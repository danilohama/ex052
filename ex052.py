""" Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
"""
numero = int(input('Digite um número: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisível {} vezes'.format(numero, tot))
if tot == 2:
    print('Número primo')
else:
    print('não é PRIMO')
