#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

pop_a =  int(input('Digite a quant. da população "A": '))
tax_a = float(input('Digite a sua taxa % de crescimento: '))
pop_b = int(input('\nDigite a quant. da população "B": '))
tax_b = float(input('Digite a sua taxa % de crescimento: '))
cont = 0

while pop_a < pop_b:
  pop_a = pop_a + (pop_a * (tax_a / 100))
  pop_b = pop_b + (pop_b * (tax_b / 100))
  cont += 1

print(f'\nLevo {cont} anos para que a Popu A superasse à Popu. B')
print(f'Pop A: {round(pop_a)} e Pop B: {round(pop_a)}')