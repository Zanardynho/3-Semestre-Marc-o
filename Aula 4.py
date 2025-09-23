        # Exercicio 1
'''
numeros = [1, 2, 3, 4, 5]
soma = sum(numeros)

print("A soma é:", soma)
'''
        # Exercicio 2
'''
entrada = input("Digite os números : ")

numeros = [int(x) for x in entrada.split()]

maior = max(numeros)
menor = min(numeros)

print("Maior número:", maior)
print("Menor número:", menor)
'''
        # Exercicio 3
'''
notas = []

for i in range(4):
    nota = float(input(f"Digite a {i+1} nota:"))
    notas.append(nota)

    media = sum(notas)
    media = media/4

print("A média das notas é: ", media)
'''

        # Exercicio 4
'''
tarefas = []

while True:
    print("""
           Lista de Tarefas
          """)
    print("""1 - Adicionar tarefa""")
    print("""2 -  Remover tarefa""")
    print("""3 -  Listar tarefas""")
    print("""4 -       Sair""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada!")

    elif opcao == "2":
        tarefa = input("Digite a tarefa a ser removida: ")
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print("Tarefa removida!")
        else:
            print("Tarefa não encontrada.")

    elif opcao == "3":
        if len(tarefas) == 0:
            print("Nenhuma tarefa na lista.")
        else:
            print("""
                  
                  Suas tarefas:
                  
                  """)
            for i, t in enumerate(tarefas, start=1):
                print(f"{i}. {t}")

    elif opcao == "4":
        print("Saindo")
        break

    else:
        print("Opção inválida, tente novamente!")
'''
        # Exercicio 5
'''
notasalunos = {}

while True:
    print("""
          Menu:
          """)
    print("1 - Adicionar aluno e notas")
    print("2 - Mostrar médias")
    print("3 - Sair")
    
    op = input("Escolha uma opção: ")
    
    if op == "1":
        nome = input("Digite o nome do aluno: ")
        notas = []
        for i in range(0, 4):
            nota = float(input(f"Digite a {i+1}ª nota: "))
            notas.append(nota)
        notasalunos[nome] = notas 
        
    elif op == "2":
        if not notasalunos:
            print("Nenhum aluno cadastrado ainda.")
        else:
            print("Alunos e suas notas:")
            print(notasalunos) 
            
            medias = {}
            for aluno, notas in notasalunos.items():
                medias[aluno] = sum(notas) / len(notas)
            
            print("Retorno")
            print(medias) 
            
    elif op == "3":
        print("Saindo")
        break
        
    else:
        print("Opção inválida!")