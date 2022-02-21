num = list()
PAR = list()
IMPAR = []
for i in range(1,21):
  num.append(int(input('Digite o número: ')))
for j in num:
  if j % 2 == 0:
    PAR.append(j)
  else:
    IMPAR.append(j)
print(f'\nOs números: {num}')
print(f'Números pares: {PAR}')
print(f'Números impares: {IMPAR}')