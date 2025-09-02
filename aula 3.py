

        # Exercicio 5

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