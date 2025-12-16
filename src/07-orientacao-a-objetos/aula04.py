""" Aula 04 - Propriedades """

# forma de controlar acesso aos atributos de uma instancia
# formas personalizadas de obter e alterar o valor de um atributo

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # getter
    @property
    def base(self):
        return self._base
    
    # setter
    @base.setter
    def base(self, value):
        if value <= 0.0:
            raise ValueError('A base deve ser maior que zero')
        self._base = value

    # getter
    @property
    def altura(self):
        return self._altura

    # setter
    @altura.setter
    def altura(self, value):
        if value <= 0.0:
            raise ValueError('A altura deve ser maior que zero')
        self._altura = value

    @classmethod
    def from_list(cls, lista):
        return cls(lista[0], lista[1])
    
    @classmethod
    def from_string(cls, rep_retangulo):
        base, altura = rep_retangulo.split(sep=',')
        return cls(float(base), float(altura))
    
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


retangulo1 = Retangulo(3.0, 3.0)

retangulo1.base = 3.0
retangulo1.altura = 3.0
print(retangulo1.base)
