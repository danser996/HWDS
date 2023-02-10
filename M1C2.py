# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 22:01:06 2023

@author: _danser96
"""

archivo = open(r'D:\DataScience\Bootcamp\M1\Clase 02/Emisiones_CO2.csv')
dicc_emisiones = {'cod_pais': [],
                  'nom_pais': [],
                  'region': [],
                  'anio': [],
                  'co2': [],
                  'co2_percapita': []}

# organizamos el diccionario con los valores de las rspectivas keys
next(archivo)  # para saltar una linea del archivo(encaezados)
for linea in archivo:
    linea = linea.strip()  # para sacar el \n
    campos = linea.split('|')  # me retorna una lista separando al encotrnar |
    for i, j in enumerate(dicc_emisiones.keys()):
        dicc_emisiones[j].append(campos[i])

archivo.close()  # para cerrar el archivo del buffer de python y alguien mas si requiere pueda utilizarlo

# Hacer ETL - extraction transform and load
# poner el año como integer
for i, j in enumerate(dicc_emisiones['anio']):
    dicc_emisiones['anio'][i] = int(j)

# cambiar el formato de numero y convertirlo a float


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

# filtrar en diccionarios
filtro_anio = 2010
filtro_region = 'América Latina y Caribe'
emisiones = 0
for i in range(len(dicc_emisiones['region'])):
    if dicc_emisiones['region'][i] == filtro_region and dicc_emisiones['anio'][i] == filtro_anio and dicc_emisiones['co2'][i] != None:
        emisiones += dicc_emisiones['co2'][i]
