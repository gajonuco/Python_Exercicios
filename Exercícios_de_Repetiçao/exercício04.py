#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

pop_a =  8000
pop_b = 20000
cont = 0

while pop_a < pop_b:
  pop_a = pop_a + (pop_a * 0.03)
  pop_b = pop_b + (pop_b * 0.015)
  cont += 1

print(f'Levo {cont} anos para que a População A superasse à População B')
print(f'Pop A: {round(pop_a)} e Pop B: {round(pop_a)}')