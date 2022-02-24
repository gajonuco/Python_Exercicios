fat = int(input('Digite o fatorial: '))
fatorial = []
resul = fat
fatorial.append(fat)
seq = fat - 1
fatorial.append(seq)
while seq > 1: 
 resul = resul * seq
 seq = seq - 1
 fatorial.append(seq)
print(f'{fat}! = {fatorial[:]} = {resul}')
