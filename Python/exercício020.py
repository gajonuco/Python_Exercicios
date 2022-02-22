num = int(input('Digite um número entre 0 e 10: '))
while (num < 0) or (num > 10):
    num = int(input('Digite de novo um número entre 0 e 10: '))
print('Perfeito!')
print(f'Seu número é: {num}')