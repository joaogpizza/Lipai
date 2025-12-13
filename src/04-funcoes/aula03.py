""" Aula 03 - Entendendo *args e *kwargs """

def world_cup_titles(country, *args):
    print('Country: ', country)
    for title in args:
        print('year: ', title)

world_cup_titles('Brasil', '1958', '1962', '1970', '1994', '2002')
world_cup_titles('Espanha', '2010')

def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')
    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount
    return value

final_price = calculate_price(100.0)
print(final_price)

final_price = calculate_price(100.0, discount=5.0)
print(final_price)

final_price = calculate_price(100.0, tax_percentage=7)
print(final_price)

final_price = calculate_price(100.0, tax_percentage=7, discount=5.0)
print(final_price)

# Testando os dois juntos
def calcular_preco(*args, **kwargs):
    porcentagem_imposto = kwargs.get('porcentagem_imposto')
    desconto = kwargs.get('desconto')

    resultado = []
    for item in args:
        if porcentagem_imposto:
            item += item * (porcentagem_imposto / 100)
        if desconto:
            item -= desconto
        resultado.append(item)
    return resultado

print('----')
valores = calcular_preco(10.0, 23.0, 118.0, 23.7, desconto=3.0, porcentagem_imposto=10.0)
print(valores)
