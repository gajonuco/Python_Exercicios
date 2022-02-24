
while True:
  fat = 0
  fatorial = []
  fat = int(input('Digite um número menor á 16: '))
  while fat > 16:
    fat = ('O número tem que ser menor á 16: ')
  resul = fat
  fatorial.append(fat)
  seq = fat - 1
  fatorial.append(seq)
  while seq > 1: 
    resul = resul * seq
    seq = seq - 1
    fatorial.append(seq)
  print(f'{fat}! = {fatorial[:]} = {resul}\n')