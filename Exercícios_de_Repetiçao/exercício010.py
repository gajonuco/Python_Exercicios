num = []
intv = []
for i in range(1,3):
  num.append(int(input('Digite um número: ')))

last = num[-1]
intervalo = num[0]

while intervalo < last - 1:
  intervalo = intervalo + 1
  intv.append(intervalo)
suma = sum(intv)
print(f'\nO intervalo é: {intv[:]}')
print(f'A suma dos intervallos é: {suma}')