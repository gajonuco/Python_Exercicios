#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.

from random import randint
num = randint(1,10)
print(f'Tabuada de {num}: \n')
for i in range(1,11):
  resul = num * i
  print(f'{num} x {i} = {resul}')