from datetime import datetime

funcionarios = []

def adicionar():
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário: "))
    data = datetime.now().strftime("%d/%m/%Y")
    funcionarios.append([nome, salario, data])
    print("Funcionário cadastrado!")

def listar():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    
    print("Nome | Salário | Data de Cadastro")
    print("---------------------------------")
    for f in funcionarios:
        print(f"{f[0]} | R$ {f[1]} | {f[2]}")

def buscar():
    nome = input("Digite o nome para buscar: ")
    for f in funcionarios:
        if nome in f[0]:
            print("Encontrado:", f[0], "-", f[1], "-", f[2])

def media():
    total = 0
    for f in funcionarios:
        total += f[1]
    media = total / len(funcionarios)
    print("Média salarial:", media)

while True:
    print("\n1 - Adicionar funcionário")
    print("2 - Listar funcionários")
    print("3 - Buscar funcionário")
    print("4 - Média salarial")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        buscar()
    elif opcao == "4":
        media()
    elif opcao == "0":
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")
