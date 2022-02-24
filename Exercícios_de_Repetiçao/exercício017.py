import random
vet1 = []
vet2 = []
vet3 = []
lista = []
for i in range(1,11):
  vet1.append(random.randint(1,51))
  vet2.append(random.randint(1,51))
  vet3.append(random.randint(1,51))
for n in range(0,10):
  lista.append(vet1[n])
  lista.append(vet2[n])
  lista.append(vet3[n])
print(f'Vector 1:\n {vet1}')
print(f'\nVector 2:\n {vet2}')
print(f'\nVector 3:\n {vet3}')
print(f'\nLista:\n {lista}')