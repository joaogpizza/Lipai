""" Exercício 03 S3.A3 """

# Classes Aluno e Projeto (dos exs anteriores)

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

class Projeto:
    """ Classe Projeto """
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
    
    @classmethod
    def from_string(cls, string):
        codigo, titulo, responsavel = string.split(',')
        return cls(int(codigo), titulo, responsavel)
    
    def __str__(self):
        return f'Projeto[codigo={self.codigo}, titulo={self.titulo}, responsavel={self.responsavel}]'
    
    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        return False
    
    def __hash__(self):
        return hash(self.codigo)
    
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, valor):
        if not isinstance(valor, int):
            raise ValueError('Código deve ser um inteiro')
        if valor <= 0:
            raise ValueError('Código <= 0')
        self._codigo = valor

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, valor):
        if not valor:
            raise ValueError('Titulo nulo/vazio')
        self._titulo = valor
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, valor):
        if not valor:
            raise ValueError('Email nulo/vazio')
        self._email = valor

class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto
    
    @classmethod
    def from_string(cls, string):
        partes = string.split(',')
        return cls(codigo = partes[0],
                   data_inicio = partes[1],
                   data_fim = partes[2],
                   aluno = Aluno.from_string(partes[3] + ',' + partes[4] + ',' + partes[5]),
                   projeto = Projeto.from_string(partes[6] + ',' + partes[7] + ',' + partes[8])
                  )
    
    def __str__(self):
        return (f'Participação[codigo={self.codigo}, data de inicio={self.data_inicio}, ' + 
                f'data de fim = {self.data_fim}, aluno = {self.aluno}, projeto = {self.projeto}')
    
    def __eq__(self, valor):
        if isinstance(valor, self.__class__):
            return self.codigo == valor.codigo
        return False
    
    def __hash__(self):
        return hash(self.codigo)
    
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, valor):
        if not valor:
            raise ValueError('Código nulo/vazio')
        self._codigo = valor
    
    @property
    def data_inicio(self):
        return self._data_inicio
    
    @data_inicio.setter
    def data_inicio(self, valor):
        if not valor:
            raise ValueError('Data de início nula/vazia')
        self._data_inicio = valor

    @property
    def data_fim(self):
        return self._data_fim
    
    @data_fim.setter
    def data_fim(self, valor):
        if not valor:
            raise ValueError('Data de fim nula/vazia')
        self._data_fim = valor
    
    @property
    def aluno(self):
        return self._aluno
    
    @aluno.setter
    def aluno(self, valor):
        if not valor or not isinstance(valor, Aluno):
            raise ValueError('Aluno informado incorretamente')
        self._aluno = valor

    @property
    def projeto(self):
        return self._projeto
    
    @projeto.setter
    def projeto(self, valor):
        if not valor or not isinstance(valor, Projeto):
            raise ValueError('Projeto informado incorretamente')
        self._projeto = valor

# Testando a classe
aluno1 = Aluno.from_string('SP0101,João da Silva,joao@email.com')
aluno2 = Aluno.from_string('MG0202,Breno Bidon,bidon@corinthians.com')
projeto1 = Projeto.from_string('123321,Pesquisa sobre Corinthians,Yuri Alberto')
projeto2 = Projeto.from_string('122221,Vasco é minusculo,Memphis Depão')

participacao1 = Participacao('SP471231', '23/04/2025', '21/12/2025', aluno1, projeto1)
participacao2 = Participacao('RJ000000', '23/04/25', '21/12/2025', aluno2, projeto1)
participacao3 = Participacao('SP471231', '01/09/1910', '22/12/2025', aluno2, projeto2)

participacoes = [participacao1, participacao2, participacao3]
for participacao in participacoes:
    print(participacao)

print('-------------------')
print(participacao1 == participacao3)
print('-------------------')

participacoesConjunto = {participacao1, participacao2, participacao3}
for participacao in participacoesConjunto:
    print(participacao)
