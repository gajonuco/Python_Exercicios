ans = []
sim = 0
nao = 0
ans.append(str(input('Telefonou para a vítima? \n')))s
ans.append(str(input('Esteve no lugar do crime? \n')))
ans.append(str(input('Mora perto da vítima? \n')))
ans.append(str(input('Devia para a vítima? \n')))
ans.append(str(input('Ja trabalhou com a vítima?\n' )))
for i in ans:
  if i == 's':
    sim =+ 1
  elif i == 'n':
    nao =+ 1

print(ans[:])
print(sim)
print(nao)
if sim == 2:
  print('\nPessoa Suspeita')
elif sim == 3 or sim == 4:
  print('\nPessoa Cúmplice')
elif sim == 5:
  print('Assassino')
else:
  print('Inocente')