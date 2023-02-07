# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 20:05:55 2023

@author: _danser96

home work, M1C1
"""

from functools import reduce


def NumeroBinario(numero):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 retorna nulo.
    '''
    if (type(numero) is int) and (numero >= 0):
        lista = []
        bandera = True
        aux = numero
        while bandera:
            resto = aux % 2
            aux = aux // 2
            lista.append(resto)
            if aux == 0:
                bandera = False
        lista = list(reversed(lista))
        return int(reduce(lambda x, y: x + str(y), lista, ''))
    else:
        return None


def FraccionABinario(numero):
    if (type(numero) is float) and (numero > 0 and numero < 1):
        lista = []
        bandera = True
        aux = numero
        while bandera:
            aux *= 2
            lista.append(int(aux))
            if aux == 1:
                bandera = False
            aux -= int(aux)
        return reduce(lambda x, y: x + str(y), lista, '0.')
    else:
        return None


for i in range(100):
    print(f'Numero {i} en binario: {NumeroBinario(i)}')
print()
lista = [1/2, 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9]
for i in lista:
    print(f'Numero {i} en binario: {FraccionABinario(i)}')
