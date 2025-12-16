""" Aula 06 - equal e hash code """

nome1 = 'João'
nome2 = 'João'

print(nome1 == nome2)


class Pessoa:
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    
    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.cpf == value.cpf
        return False
    
    def __hash__(self):
        return hash(self.cpf)
    
    def __repr__(self):
        return f'Pessoa({self.cpf},{self.nome})'


pessoa1 = Pessoa('100100100-10', 'João')
pessoa2 = Pessoa('100100100-10', 'João')
pessoa3 = Pessoa('100100100-11', 'Maria')

pessoas = {pessoa1, pessoa2, pessoa3}
print(pessoas)
print(pessoa1 == pessoa2)


pessoas_lista = [pessoa1, pessoa2, pessoa3]
print(pessoas_lista)

print(pessoas_lista.count(pessoa1))
