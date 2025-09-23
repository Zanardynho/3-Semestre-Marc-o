# Exercício 1
'''
numero = int(input("Digite o número para verificação: "))
if numero % 2 == 1:
    print("Número Impar")
else:
    print("Número Par")
'''
# Exercício 2
'''
print("Iniciemos a calculadora: ")
op = str(input("""Qual operação deseja? 
           * - Multiplicação")
           / - Divisão
           + - Soma
           - - Subtração
            """))
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if op == "*":
    print(f"{n1} * {n2} = ", n1*n2)
elif op == "/":
    print(f"{n1} / {n2} = ", n1/n2)
elif op == "+":
    print(f"{n1} + {n2} = ", n1+n2)
else:
    print(f"{n1} - {n2} = ", n1-n2)
'''
       # Exercicio 3
'''
soma_notas: int = 0
contador: int = 0

while contador < 4:
    nota: int = int(input(f"Digite a {contador + 1}º nota: "))
    if 0 <= nota <= 10:
       soma_notas += nota
       contador += 1

media: float = soma_notas / 4
print(f"Média: {media}")

if media >= 7:
    print("Aprovado!")
elif 4 <= media < 7:
    print("Recuperação")
else:
    print("Reprovado!")
'''
    # Exercício 4
'''
print("############# Tabuada Papai #############")
cont = 0
ntab = int(input("Digite o Número a qual quer ver a Tabuada: "))

while cont <= 10:
    print(f"{ntab} X {cont} =", ntab*cont)
    cont += 1      
'''
    # Exercicio 3

'''
soma_notas: int = 0
contador: int = 0

while contador < 4:
    nota: int = int(input(f"Digite a {contador + 1}º nota: "))
    if 0 <= nota <= 10:
       soma_notas += nota
       contador += 1

media: float = soma_notas / 4
print(f"Média: {media}")

if media >= 7:
    print("Aprovado!")
elif 4 <= media < 7:
    print("Recuperação")
else:
    print("Reprovado!")
'''
    # Exercício 5
'''
soma_notas: int = 0
contador: int = 0

while contador < 4:
    nota: int = int(input(f"Digite a {contador + 1}º nota: "))
    if 0 <= nota <= 10:
       soma_notas += nota
       contador += 1

media: float = soma_notas / 4
print(f"Média: {media}")

if media >= 7:
    print("Aprovado!")
elif 4 <= media < 7:
    print("Recuperação")
else:
    print("Reprovado!")
'''
    # Exercício 6
'''
pares = 0
print ("Números pares de 1 a 100")
while pares <= 100:
    print(pares)
    pares += 2
'''
    # Exercício 7
'''
import random

print("Bem-vindo ao jogo de adivinhação!")
print("Números de 1 a 100.\n")

numero_secreto = random.randint(0, 100)
tentativas = 0

while True:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("O número é MAIOR!")
    elif palpite > numero_secreto:
        print("O número é MENOR!")
    else:
        print(f"Parabéns! {numero_secreto} em {tentativas} tentativas!")
        break
'''    
    # Exercício 8
'''
palavra_secreta = input("Digite a palavra secreta: ")
palavra_tentativa = []
letras_tentadas = []
tentativas_total: int = 5
tentativa_atual: int = 0


def inicializar_palavra_tentativa() -> None:
    print(f"A palavra tem {len(palavra_secreta)} letras.")
    for _ in palavra_secreta:
        palavra_tentativa.append("_")


def imprimir_palavra_tentativa() -> str:
   palavra = "".join(palavra_tentativa)
   return palavra


def pedir_letra() -> bool:
    letra_tentativa = input("Digite uma letra: ")
    tem_letra = False
    if letra_tentativa not in letras_tentadas:
        for index, letra in enumerate(palavra_secreta):
            if letra == letra_tentativa:
                palavra_tentativa[index] = letra
                tem_letra = True
        letras_tentadas.append(letra_tentativa)
    else:
        tem_letra = True
        print(f"Letra '{letra_tentativa}' já foi tentada!")
        print(letras_tentadas)
    return tem_letra


def imprimir_forca() -> None:
   if tentativa_atual == 0:
       print("""
              |-------|
              |       |
              |
              |
              |
           ___|____
       """)
   elif tentativa_atual == 1:
        print("""
               |-------|
               |       |
               |      (_)
               |
               |
            ___|____
        """)
   elif tentativa_atual == 2:
        print("""
               |-------|
               |       |
               |      (_)
               |       |
               |
            ___|____
        """)
   elif tentativa_atual == 3:
        print("""
            |--------
            |       |
            |      (_)
            |      /|\\
            |
         ___|____
        """)
   elif tentativa_atual == 4:
        print("""
               |--------
               |       |
               |      (_)
               |      /|\\
               |       |
            ___|____
        """)
   elif tentativa_atual == 5:
        print("""
               |--------
               |       |
               |      (_)
               |      /|\\
               |       |
            ___|____  / \\
        """)


inicializar_palavra_tentativa()


while True:
    print(imprimir_palavra_tentativa())

    tem_letra = pedir_letra()
    if not tem_letra:
        tentativa_atual += 1

    imprimir_forca()

    print(f"Suas tentativas: {tentativa_atual}")
    if tentativa_atual >= tentativas_total:
        print("Game Over!")
        break

    if imprimir_palavra_tentativa() == palavra_secreta:
        print("Parabéns você ganhou!!")
        print(f"Palavra secreta: {palavra_secreta}")
        break
    '''