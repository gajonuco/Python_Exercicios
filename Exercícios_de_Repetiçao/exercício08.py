#Faça um programa que leia 5 números e informe a soma e a média dos números.
from statistics import mean
num = list()
for i in range(1,6):
  num.append(int(input(f'Introduzca o {i}º número: ')))

print(f'\nA suma dos números é: {sum(num)}')
print(f'A media dos números é: {mean(num)}')