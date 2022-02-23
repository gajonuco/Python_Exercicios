usuario = list()
name = str(input('Nome(maior que tres caracteres): '))
while len(name) <= 3:
  name = str(input('Digite de novo e correctamente o "Nome": '))
usuario.append(name)

idade = int(input('\nIdade(entre 0 e 150): '))
while (idade<0) or (idade>150):
  idade = int(input('Digite de novo e correctamente a "Idade": '))
usuario.append(idade)

salario = float(input('\nDigite o salário(maior que zero): '))
while salario<0:
  salario = float(input('Digite de novo e correctamente o "Salario": '))
usuario.append(salario)

est_civil = str(input("\nEstado Civil('s', 'c', 'v', 'd'):"))
while est_civil != 's' and est_civil != 'c' and est_civil !='v' and est_civil != 'd':
  est_civil = str(input('Digite de novo e correctamente o "Estado Civil": '))
usuario.append(est_civil)

sexo = str(input('\nSexo("f" ou "m"): '))
while sexo != 'f' and sexo != 'm':
  sexo = str(input('Digite de novo e correctamente o "Sexo": '))
usuario.append(sexo)

print('\nParabens!')
print(f'Seus dados são:\n {usuario[:]}')