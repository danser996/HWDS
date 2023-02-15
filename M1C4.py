# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 20:02:53 2023

@author: _danser96
"""

'''
A partir del CSV hospitales2.csv, generar un archivo CSV de salida, que contenga los siguientes
campos en este orden:
latitude
longitude
name
label
Con los correspondientes datos extraídos del CSV original, el campo name tiene que corresponder
con la dirección del hospital, y el campo label con el nombre del hospital.
'''
# leer archivo csv para dataframe
from matplotlib import pyplot as plt
import pandas as pd
df = pd.read_csv(r'D:\DataScience\Bootcamp\M1\Clase 04\hospitales2.csv')
print(df.head())
print()
df.WKT = df.WKT.str.replace('POINT ', '')
df.WKT = df.WKT.str.replace('(', '')
df.WKT = df.WKT.str.replace(')', '')
print(df.head())
print()
# crear el natafram que pide el cliente
df[['latitude', 'longitude']] = df.WKT.str.split(' ', expand=True)
df2 = df[['latitude', 'longitude', 'NOMBRE', 'DOM_NORMA']]
# cambiar nombres de la columndas del dataframe
df2.rename(columns={'NOMBRE': 'name',
                    'DOM_NORMA': 'label'},
           inplace=True)
# poner las coordenadas como float
df2.latitude = df2.latitude.astype(float)
df2.longitude = df2.longitude.astype(float)
print(df2.head())
print()
df2.to_csv('DF_HW4.csv')

# practica de matplotlib, grafciar longitud vs latitude
plt.scatter(df2.latitude,
            df2.longitude,
            marker='*',
            linewidths=4,
            color='r')
plt.title('longitud VS latitude')
plt.xlabel('latitude')
plt.ylabel('longitude')
plt.grid()
plt.show()
