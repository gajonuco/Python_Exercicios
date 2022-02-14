import statistics
alum_aprov = not_aprov = notas = []
alum_repro = not_repro = []
for i in range(1,5):
  print(f'Digite as notas do {i}º alumno: \n')
  for j in range(1,5):
    notas.append(float(input(f'{j}º Nota: ')))
  media = statistics.mean(notas)
  alumnos.append(notas[:])
  if media >= 7.0:
    alum_aprov.append(i)
    not_aprov.append(media)
    notas.clear()
  else:
    alum_repro.append(i)
    not_repro.append(media)
    notas.clear()

print(f'Alumnos aprovados:\n {not_aprov}')
print(f'\nAlumnos reprovados:\n {not_repro}')