def cadastrar_aluno(lista_principal):
    lista_aluno = []
    
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matrícula do aluno: ")
    idade = input("Digite a idade do aluno: ")
    curso = input("Digite o curso do aluno: ")
    horario = input("Digite o horário do aluno: ")
    
    lista_aluno.append(nome)
    lista_aluno.append(matricula)
    lista_aluno.append(idade)
    lista_aluno.append(curso)
    lista_aluno.append(horario)
    
    lista_principal.append(lista_aluno)
    print("Aluno cadastrado com sucesso!")

def listar_alunos(lista_principal):
    for aluno in lista_principal:
        print("Nome:", aluno[0])
        print("Matrícula:", aluno[1])
        print("Idade:", aluno[2])
        print("Curso:", aluno[3])
        print("Horário:", aluno[4])
        print()

def remover_aluno(lista_principal):
    matricula = input("Digite a matrícula do aluno que deseja remover: ")
    
    for aluno in lista_principal:
        if aluno[1] == matricula:
            lista_principal.remove(aluno)
            print("Aluno removido com sucesso!")
            break
    else:
        print("Aluno não encontrado.")

def menu():
    lista_principal = []
    
    while True:
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Remover aluno")
        print("0. Sair")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            cadastrar_aluno(lista_principal)
        elif opcao == '2':
            listar_alunos(lista_principal)
        elif opcao == '3':
            remover_aluno(lista_principal)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Digite novamente.")

menu()
