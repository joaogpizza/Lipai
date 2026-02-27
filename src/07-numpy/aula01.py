""" Aula de numpy """

import numpy as np
from numpy.random import default_rng
from time import process_time
import matplotlib.pyplot as plt

a = np.array([[1,2,3,4,5,6],[3,4,5,6,7,8]])
print(a)
print(type(a))

zero_array = np.zeros(shape = (5,3,6))
print(zero_array)

um_array = np.ones((2,3))
print(um_array)

vazio = np.empty((3,4))
print(vazio)

# Dá uma sequência de números:
zero_dez = np.arange(10)
print(zero_dez)
pula_dois = np.arange(3,15,2)
print(pula_dois)

array_linear = np.linspace(0, 100 , num = 20, endpoint = False, retstep = True)
print(array_linear)

print(zero_array.shape)
print(zero_array.size)
print(zero_array.ndim)

a = np.array( [ 1, 2, 3])
print(a.shape)

a2 = a[np.newaxis,:]
print(a2.shape)
print(a2)

a2 = a[:,np.newaxis]
print(a2.shape)
print(a2)

a2[2][0] = 2
print(a2)

a = np.array( [1, 2, 3])
b = np.array( [4, 5, 6])

c=np.concatenate((a,b))
d=np.concatenate((b,a))

print(c)
print(d)

a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print('------------')
print(a[a<8])

a = np.array( [1, 2, 3])

print(a.max())
print(a.min())
print(a.mean())
print(a.sum())

rng= default_rng()
aleatorio = rng.integers(10, size=(2,4))
print(aleatorio)

a = np.array([1,3,4,5,6,5,7,8])
print("Essa é o array 'a':",a)
print("Esse é tipo de 'a':",type(a))
print('-------------------------------------')
lista_a=[1,3,4,5,6,5,7,8]
print("Essa é a 'lista_a':", lista_a)
print("Esse é tipo de 'lista_a':",type(lista_a))

#arrays não permitem tipos de dados distintos:
a = np.array([1,'Daniel',2,3,4,5,6,7,8])
print(a)
print(type(a[0]))

#já as listas sim:
lista_a = [1,'Daniel',2,3,4,5,6,7,8]
print(a)
print(type(lista_a[0]))

lista_a = list(rng.integers(10, 100, 10000000))
print(type(lista_a))
lista_b = list(rng.integers(10, 100, 10000000))
# c = lista_a*lista_b (Dá erro, por isso está comentada)

print(type(lista_a))
print(len(lista_a))

c=[]
t1 = process_time()
for i in range(len(lista_a)):
    c.append(lista_a[i] * lista_b[i])
t2 = process_time()

print(t2-t1)

a = rng.integers(10, 100, 10000000)
b = rng.integers(10, 100, 10000000)
print(type(a))
print(a)
t1a=process_time()
c=a*b
t2a=process_time()
print(t2a-t1a)

dados_x = rng.integers(20, size = 30)
dados_y = rng.integers(12, size = 30)

plt.scatter(x = dados_x, y = dados_y)
plt.show()
