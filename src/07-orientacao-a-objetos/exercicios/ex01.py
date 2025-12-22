""" Exercicio 01 S3.A3 """

class Aluno:
    """ Classe Principal do exercício """
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email
    
    @classmethod
    def from_string(cls, string):
        """ Pega uma string do tipo 'Prontuario,Nome,Email' para criar um Aluno """
        prontuario, nome, email = string.split(',')
        return cls(prontuario, nome, email)
    
    def __str__(self):
        return f'Aluno[prontuario={self.prontuario}, nome={self.nome}, email={self.email}]'
    
    @property
    def prontuario(self):
        return self._prontuario
    
    @prontuario.setter
    def prontuario(self, valor):
        if valor:
            self._prontuario = valor
        else:
            raise ValueError('Prontuario nulo/vazio')
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        if valor:
            self._nome = valor
        else:
            raise ValueError('Nome nulo/vazio')
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        if valor:
            self._email = valor
        else:
            raise ValueError('Email nulo/vazio')
    
    def __eq__(self, value):
        """ 2 Alunos são iguais se tiverem o mesmo prontuário """
        if isinstance(value, self.__class__):
            return self.prontuario == value.prontuario
        return False
    
    def __hash__(self):
        return hash(self.prontuario)

# Testando a classe
aluno1 = Aluno('SP0101', 'João da Silva', 'joao@email.com')
aluno2 = Aluno.from_string('SP0202,Pâmela da Silva,pamela@email.com')
aluno3 = Aluno('SP0101', 'Maria da Silva', 'maria@email.com')

alunos = [aluno1, aluno2, aluno3]
for aluno in alunos:
    print(aluno)
print('--------------------')
print(aluno1 == aluno3)
print('--------------------')
alunosConjunto = { aluno1, aluno2, aluno3 }
for aluno in alunosConjunto:
    print(aluno)
