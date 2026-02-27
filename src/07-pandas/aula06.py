import pandas as pd

# Parte 6

notas = pd.DataFrame({
    'nome': ['João', 'Maria', 'José', 'Alice'],
    'idade': [20, 21, 19, 20],
    'nota_final': [5.0, 10.0, 6.0, 10.0]
})
print(notas)

print(notas.sort_values(by='nota_final'))

print(notas.sort_values(by='nota_final', ascending=False))

print(notas.sort_values(by=['nota_final', 'nome'], ascending=[False, True]))

print(notas)
print(notas.sort_values(by=['nota_final', 'nome'], ascending=[False, True], inplace=True))
print(notas)
