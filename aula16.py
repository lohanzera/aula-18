def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")
    return nome, cpf, senha

def fazer_login(usuarios):
    cpf_1 = input("Digite seu CPF: ")
    senha_1 = input("Digite sua senha: ")   

    for usuario in usuarios:
        if cpf_1 == usuario[1] and senha_1 == usuario[2]:
            print("Login efetuado com sucesso!")
            return True

    print("CPF ou senha incorrentos. Tente novamente.")
    return False

def main():
    usuarios = []
    while True:
        print("1. Cadastrar Usuário")
        print("2. Fazer Login")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            novo_usuario = cadastrar_usuario()
            if len(novo_usuario[1]) == 11 and novo_usuario[1].isdigit():
                usuarios.append(novo_usuario)
                print("Usuário cadastrado c om sucesso!")
            else:
                print("CPF inválido. O CPF deve conter apenas números e ter 11 digitos.")
        
        elif opcao == "2":
            if fazer_login(usuarios):
                break

        else:
            print("Opção Inválida!")