pop_a =  8000
pop_b = 20000
cont = 0

while pop_a < pop_b:
  pop_a = pop_a + (pop_a * 0.03)
  pop_b = pop_b + (pop_b * 0.015)
  cont += 1

print(f'Levo {cont} anos para que a Popu A superasse à Popu. B')
print(f'Pop A: {round(pop_a)} e Pop B: {round(pop_a)}')