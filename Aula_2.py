print('''
####### Paulo Henrique Silva Zanardi #######
####### 	  3º Semestre - ADS	     #######
''')
'''
print("Atividade 1")

nome = str = "Paulo"
email = str = "pzdacb@uol.com"

print(f"Olá {nome}, seu email é {email}.")

print("Atividade 2")
nome = str(input("Digite seu nome: "))
email = str(input("Digite seu email: "))

print(f"Olá {nome}, seu email é {email}.")

print("Atividade 3")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite sua peso: "))

imc = peso / (altura * altura)

print(f"Seu IMC É: {imc}")

print("Atividade 4")
nota1 = float(input("Digite sua nota 1: "))
nota2 = float(input("Digite sua nota 2: "))
nota3 = float(input("Digite sua nota 3: "))
nota4 = float(input("Digite sua nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"Sua média é: {media}")

print("Atividade 5")
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Maior de idade!")
else:
    print("Menor de idade!")

print("Atividade 6")
senha1 = str(input("Digite sua senha antiga: "))
senha2 = str(input("Digite sua senha nova: "))

senha_igual = senha1 == senha2
print(senha_igual)

print("Atividade 7")
nome = str(input("Digite seu nome: "))
email = str(input("Digite seu email: "))

nome1 = str(input("Digite seu nome: "))
email1 = str(input("Digite seu email: "))

comparacao = (nome == nome1) and (email == email1)
print(comparacao)
'''

