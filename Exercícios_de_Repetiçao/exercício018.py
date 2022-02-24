import random, statistics
temp = []

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for i in range(1,13):
  temp.append(round(random.uniform(0,46), 2))
media = statistics.mean(temp)
print(f'\nTemperatura media do ano:: {media:.2f}\n' )
print('Meses com a temperatura acima da media: ')
for j in range(1,13):
  if temp[j-1] > media:
    print(f' {j}-{meses[j-1]}',end=' ')
print('\nTemperatura media de todos os meses: \n', temp[:])