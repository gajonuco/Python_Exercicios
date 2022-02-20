print('Faça seu cadastro com suas seguintes condiçoes:',
      'Nome: maior que 3 caracteres;',
      'Idade: entre 0 e 150;',
      'Salário: maior que zero;',
      "Sexo: 'f' ou 'm';",
      "Estado Civil: 's', 'c', 'v', 'd'; ")
name = []
nome = input('Nome: ')
name = nome

idade = int(input('Idade: '))
salario = float(input('Salario: '))
sexo = input('Sexo: ')
estado_civil = input('Digite seu estado civil: ')
tam = len(name)
if tam <= 3:
   nome2 = print('Digite o nome novamente:')
   name = nome2
elif idade < 0 and idade > 150:
  idade2 = print('Digite a idade novamente:')
  idade = idade2
elif salario < 0:
  salario2 = print('Digite o salario novamente:')
  salario = salario2
elif sexo != 'f' or 'm':
  sexo2 = print('Digite o sexo novamente:')
  sexo = sexo2
elif estado_civil != 's' or 'c' or 'v' or 'd':
  estado_civil2 = input('Digite novamente o Estado Civil: ')
  estado_civil = estado_civil2