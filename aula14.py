usuarios = []

def cadastro():
  nome = str(input("Digite seu nome: "))
  cpf = int(input("Digite seu cpf: "))
  senha = int(input("Digite sua senha: "))
  usuarios.append([nome, cpf, senha])

def login():
  cpf = int(input("Digite seu cpf: "))
  senha = int(input("Digite sua senha: "))
  for usuario in usuarios:
    if usuario[1] == cpf and usuario[2] == senha:
      print("Login bem-sucedido!")
      return
    print("Dados incorretos!")

def menu():
  while True:
    print("\n1. Cadastro")
    print("2. Login")
    print("3. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
      cadastro()
    elif escolha == '2':
      login()
    elif escolha == '3':
      print("Até logo!")
      return
    else:
      print("Opção inválida!")

menu()