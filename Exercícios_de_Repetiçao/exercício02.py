#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

user = str(input('Digite o seu usuario: '))
password  = str(input('Digite a sua contrasenha: '))
while user == password:
  password = str(input('Digite de novo sua contrasenha: '))
print('Parabens!')
print('Cadastro concluído')