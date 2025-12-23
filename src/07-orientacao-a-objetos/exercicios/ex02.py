""" Exercício 02 S3.A3 """

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

# Testando a classe
projeto1 = Projeto(133, 'Pesquisa', 'Juan')
projeto2 = Projeto.from_string('1,Laboratório de Desenvolvimento de Software,Pedro Gomes')
projeto3 = Projeto(133, 'Teste de classes', 'Yuri Alberto Protagonista')

projetos = [projeto1, projeto2, projeto3]
for projeto in projetos:
    print(projeto)

print('--------------')
print(projeto1 == projeto3)
print('--------------')

projetosConjunto = { projeto1, projeto2, projeto3 }
for projeto in projetosConjunto:
    print(projeto)
