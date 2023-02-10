# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 16:02:53 2023

@author: _danser96
"""
##########################################################################
archivo = open('D:/DataScience/Bootcamp/M1/Clase 02/Emisiones_CO2.csv')

dicc_emisiones = {'cod_pais': [],
                  'nom_pais': [],
                  'region': [],
                  'anio': [],
                  'co2': [],
                  'co2_percapita': []}

# otra alternativa
next(archivo)
for linea in archivo:
    # print(repr(linea))  # para ver la representacion de un espacio
    # print(repr(linea))  # para ver la representacion de un espacio
    linea = linea.strip()  # para sacar el \n
    campos = linea.split('|')
    # print(campos)
    # break
    dicc_emisiones['cod_pais'].append(campos[0])
    dicc_emisiones['nom_pais'].append(campos[1])
    dicc_emisiones['region'].append(campos[2])
    dicc_emisiones['anio'].append(campos[3])
    dicc_emisiones['co2'].append(campos[4])
    dicc_emisiones['co2_percapita'].append(campos[5])

archivo.close()

# # valor faltante
# cont = 0
# for clave in dicc_emisiones:
#     for elemento, in dicc_emisiones[clave]:
#         if not elemento:
#             cont += 1


# normalizar los datos de co2 para que sean flotantes
def normalizacion(lista):
    for indice, elemento in enumerate(lista):
        if elemento:
            elemento = elemento.replace('.', '')
            elemento = elemento.replace(',', '.')
            elemento = float(elemento)
        else:
            elemento = None
        lista[indice] = elemento
    return lista


dicc_emisiones['co2'] = normalizacion(dicc_emisiones['co2'])
dicc_emisiones['co2_percapita'] = normalizacion(
    dicc_emisiones['co2_percapita'])

# transformar el año
for i in range(len(dicc_emisiones['anio'])):
    dicc_emisiones['anio'][i] = int(dicc_emisiones['anio'][i])
