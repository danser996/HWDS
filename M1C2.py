# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 22:01:06 2023

@author: _danser96
"""
import os
archivo = open(
    'D:/DataScience/Bootcamp/M1/Clase 02/Emisiones_CO2.csv', 'r', encoding='Windows-1252')

dicc_emisiones = {'cod_pais': [],
                  'nom_pais': [],
                  'region': [],
                  'anio': [],
                  'co2': [],
                  'co2_percapita': []}
