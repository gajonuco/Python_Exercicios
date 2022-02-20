import statistics
num = list()
for i in range(5):
  num.append(int(input(f'Digite a {i + 1}º nota: ')))

print(f'A media das notas é: {statistics.mean(num)}')