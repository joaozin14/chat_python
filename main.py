from bd import conecta_bd, inserir_dados, obter_dados, excluir_cliente, alterar_telefone
from time import sleep

def menu_principal():
    print("""
    Olá, sou o chat desenvolvido pelo Dev João!
    """)
    executando = True  # Variável de controle para o loop principal
    while executando:
        cpf = input("Por favor, digite seu CPF: ")
        dados = obter_dados(cpf)

        if dados:
            print("\nDados encontrados:")
            for dado in dados:
                print(dado)
            executando = menu_opcoes(cpf)  # Se o usuário sair, a execução será interrompida
        else:
            print(f"Nenhum cliente encontrado para o CPF '{cpf}'.")
            if deseja_cadastrar():
                cadastrar_usuario(cpf)
                executando = False  # Encerra o programa após o cadastro
            else:
                print("\nAté mais e tenha um bom dia!")
                executando = False

def menu_opcoes(cpf):
    while True:
        escolha = input(f"""
        O que deseja fazer?
            1 - Inserir novos dados
            2 - Excluir seus dados
            3 - Ler seus dados 
            4 - Alterar o telefone 
            5 - Sair
        Escrever: """)
        
        if escolha == "1":
            print("Inserindo novos dados...")
            sleep(2)
            cadastrar_usuario_novo()
        elif escolha == "2":
            print("Excluindo seus dados...")
            sleep(2)
            excluir_cliente(cpf)
            print("Dados excluídos com sucesso")
        elif escolha == "3":
            print("\nLendo seus dados...")
            dados = obter_dados(cpf)
            if dados:
                for dado in dados:
                    print(dado)
            else:
                print("Nenhum dado encontrado.")
        elif escolha == "4":
            telefone = input("\nDigite o telefone para alteração: ")
            alterar_telefone(telefone, cpf)
            print("Telefone alterado com sucesso")
        elif escolha == "5":
            print("\nAté mais e tenha um bom dia!")
            return False  # Indica ao menu principal que o programa deve encerrar
        else:
            print("\nDigite uma opção válida.")

def deseja_cadastrar():
    while True:
        escolha = input("""
        Deseja fazer o cadastro?
            1 - Sim
            2 - Não
        Escrever: """)
        if escolha == "1":
            return True
        elif escolha == "2":
            return False
        else:
            print("\nDigite uma opção válida.")

def cadastrar_usuario(cpf):
    print("\nÓtimo, vamos começar seu cadastro!")
    nome = input("\nDigite o seu nome: ")
    data_nasc = input("Digite sua data de nascimento: ")
    telefone = input("Digite seu telefone: ")
    print("Inserindo no nosso banco de dados...")
    sleep(2)
    inserir_dados(cpf, nome, data_nasc, telefone)
    print(f"Dados incluídos com sucesso, senhor(a) {nome}!")

def cadastrar_usuario_novo():
    print("\nÓtimo, vamos começar seu cadastro!")
    cpf = input("\nDigite seu cpf: ")
    nome = input("Digite o seu nome: ")
    data_nasc = input("Digite sua data de nascimento: ")
    print("Inserindo no nosso banco de dados...")
    sleep(2)
    inserir_dados(cpf, nome, data_nasc)
    print(f"Dados incluídos com sucesso, senhor(a) {nome}!")

menu_principal()
