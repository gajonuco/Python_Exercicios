print('Faça seu cadastro com suas seguintes condiçoes:')
print('Nome: maior que 3 caracteres;')
print('Idade: entre 0 e 150;')
print('Salário: maior que zero;')
print("Sexo: 'f' ou 'm';")
print("Estado Civil: 's', 'c', 'v', 'd'; ")
name = []
nome = input('Nome: ')
name = nome
while len(name) <= 3:
   nome2 = input('Digite o nome novamente:')
   name = nome2
idade = int(input('Idade: '))
if idade < 0:
  idade2 = input('Digite a idade novamente:')
  idade = idade2
elif idade > 150:
  idade2 = input('Digite a idade novamente:')
  idade = idade2

salario = float(input('Salario: '))
while salario < 0.0:
  salario2 = input('Digite o salario novamente:')
  salario = salario2
  
sexo = input('Sexo: ')
while (sexo != 'f' or 'm'):
  sexo2 = input('Digite o sexo novamente:')
  sexo = sexo2
estado_civil = input('Digite seu estado civil: ')
while(estado_civil != 's' or 'c' or 'v' or 'd'):
  estado_civil2 = input('Digite novamente o Estado Civil: ')
  estado_civil = estado_civil2
