def rep(cont):
  return num - cont


num = int(input(print('Digite a quantidade de números: \n' )))
cont = num - 1
k = 1
for i in range(num):
  print('\n')
  seq = rep(cont)
  k = 1
  while k <= seq :
    print(f'{k} ', end = '')
    k += 1
  cont -= 1