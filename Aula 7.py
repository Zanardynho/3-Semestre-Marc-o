# Exercício 1
'''
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido.")

    def exibir_saldo(self):
        print(f"Titular: {self.__titular} - Saldo: R${self.__saldo:.2f}")
'''
    # Exercício 2
'''
class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    # Getters
    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_altura(self):
        return self.__altura

    # Setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        if idade > 0:
            self.__idade = idade

    def set_altura(self, altura):
        if altura > 0:
            self.__altura = altura
'''
    # Exercício 3
'''
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade

    def set_preco(self, preco):
        if preco > 0:
            self.__preco = preco

    def set_quantidade(self, quantidade):
        if quantidade >= 0:
            self.__quantidade = quantidade


class Eletronico(Produto):
    def calcular_desconto(self, percentual):
        return self.get_preco() * (1 - percentual / 100)


class Alimento(Produto):
    def verificar_validade(self, valido: bool):
        if valido:
            return "Produto dentro da validade."
        else:
            return "Produto vencido!"


class Vestuario(Produto):
    def calcular_desconto(self, percentual):
        return self.get_preco() * (1 - percentual / 100)
'''