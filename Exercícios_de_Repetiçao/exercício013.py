letter = []
cont = 0
for i in range(1, 11):
  letter.append((input(f'Digite o {i}º caracter: ')))
seq = 0
for k in letter:  
  if k.isupper == True:
    letter.pop(seq)
    letter.insert(seq, k.lower())
    seq =+ 1

for j in letter:
  if j == 'a' or 'e' or 'i'or 'o' or 'u':
    cont =+ 1
print('\n', letter[:])
print(f'Os 10 caracteres tem {cont} consoantes.')