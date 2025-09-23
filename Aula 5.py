# Exercício 1
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Opa! meu nome é {self.nome}, tenho {self.idade} anos.")

# Exercício 2
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return 2 * (self.largura + self.altura)

    # Exercício 3
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
