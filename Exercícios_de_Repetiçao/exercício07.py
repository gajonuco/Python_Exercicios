]#Faça um programa que leia 5 números e informe o maior número.

num = list()
for i in range(1,6):
  num.append(int(input(f'Introduzca o {i}º número: ')))

print(f'O maior número é: {max(num)}')