    # Exercícios 1
'''
class Conta:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def ver_saldo(self):
        print(f"Conta {self.numero} - Saldo: R${self.saldo:.2f}")


class ContaCorrente(Conta):
    pass


class ContaPoupanca(Conta):
    pass


class Cliente:
    def __init__(self, nome, conta_corrente, conta_poupanca):
        self.nome = nome
        self.conta_corrente = conta_corrente
        self.conta_poupanca = conta_poupanca


cc = ContaCorrente(101, 500)
cp = ContaPoupanca(202, 1000)
cliente = Cliente("João", cc, cp)

cliente.conta_corrente.depositar(200)
cliente.conta_corrente.ver_saldo()
cliente.conta_poupanca.sacar(300)
cliente.conta_poupanca.ver_saldo()
'''
# Exercícios 2
'''
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, combustivel, portas):
        super().__init__(marca, modelo, ano)
        self.combustivel = combustivel
        self.portas = portas

    def exibir(self):
        print(f"Carro: {self.marca} {self.modelo} {self.ano}, {self.portas} portas, Combustível: {self.combustivel}")


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas, partida):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas
        self.partida = partida

    def exibir(self):
        print(f"Moto: {self.marca} {self.modelo} {self.ano}, {self.cilindradas}cc, Partida: {self.partida}")

carro = Carro("Toyota", "Corolla", 2023, "Flex", 4)
moto = Moto("Honda", "CB 500", 2022, 500, "Elétrica")

carro.exibir()
moto.exibir()

# Exercícios 3

class Funcionario:
    def __init__(self, nome, email, salario):
        self.nome = nome
        self.email = email
        self.salario = salario

class Desenvolvedor(Funcionario):
    def __init__(self, nome, email, salario, linguagens):
        super().__init__(nome, email, salario)
        self.linguagens = linguagens

    def exibir_linguagens(self):
        print(f"Desenvolvedor {self.nome} programa em: {', '.join(self.linguagens)}")


class Gerente(Funcionario):
    def __init__(self, nome, email, salario, departamento):
        super().__init__(nome, email, salario)
        self.departamento = departamento

    def exibir_departamento(self):
        print(f"Gerente {self.nome} é responsável pelo departamento: {self.departamento}")


class Mentor:
    def __init__(self, horas_disponiveis):
        self.horas_disponiveis = horas_disponiveis

    def mentorear(self):
        print(f"Disponível para mentoria por {self.horas_disponiveis} horas.")

class DevMentor(Desenvolvedor, Mentor):
    def __init__(self, nome, email, salario, linguagens, horas_disponiveis):
        Desenvolvedor.__init__(self, nome, email, salario, linguagens)
        Mentor.__init__(self, horas_disponiveis)


class GerenteMentor(Gerente, Mentor):
    def __init__(self, nome, email, salario, departamento, horas_disponiveis):
        Gerente.__init__(self, nome, email, salario, departamento)
        Mentor.__init__(self, horas_disponiveis)


# Exemplo de uso:
dev = DevMentor("Ana", "ana@empresa.com", 8000, ["Python", "Java"], 5)
ger = GerenteMentor("Carlos", "carlos@empresa.com", 12000, "TI", 3)

dev.exibir_linguagens()
dev.mentorear()
ger.exibir_departamento()
ger.mentorear()
'''