# fazer duas funções interligadas, função 1 - cadastrar usuario,  função 2 - login(informar sucesso no login se acertar a senha e informar falha se errar)

#para cadastro, solicitar dados atraves do input: nome, cpf e senha;
#para fazer login, solicitar cpf e senha;

def cadastro(cadastro1):
    print("bem vindo ao sistema de cadastro")
    while True: 
        try:
            cadnome = input("digite seu nome: ")
            cadcpf = int(input("digite seu cpf: "))
            cadsenha = int(input("digite sua senha: "))
            break   
        except ValueError: 
            print("Para CPF e Senha são permitidos somente números!") 

    
    cadastro1.append([cadnome, cadcpf, cadsenha])
    print (cadastro1)



def login(cadastro1):
    print("SISTEMA DE LOGIN")
    logcpf = int(input("Digite seu login: "))
    logsenha = int(input("Digite sua senha: "))

    for usuario in cadastro1:
        if logcpf == usuario[1] and logsenha == usuario[2]:
            print("login feito com sucesso")
            return True
        
    print("CPF ou senha incorretos. Tente novamente.")
    return False

#preciso comparar as funções // o que foi digitado no login com o que foi cadastrado

def menu():
    cadastro1 = []
    while True:
        print("Bem vindo ao PC")
    
    
        escolha = input("Escolha a opção desejada(1 / 2): ")

        if escolha in  ('1', '2'):
            if escolha == '1':
             cadastro(cadastro1)
            elif escolha == '2':
                login(cadastro1)
                break
            else: 
                break

menu()
