#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

num = int(input('Digite um número entre 0 e 10: '))
while (num < 0) or (num > 10):
    num = int(input('Digite de novo um número entre 0 e 10: '))
print('Perfeito!')
print(f'Seu número é: {num}')