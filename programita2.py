#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:24:40 2020

@author: Edgard Gonzalez
"""
import pandas as pd

excel = pd.read_excel('ingresos.xlsx')
print(excel)

while (input("Quiere agregar nuevo dato? (si/no): ").lower() == "si"):
    nueva_fecha = input("Agregar Fecha (dd/mm/yyyy): ")
    nueva_venta = int(input("Agregar $ de Venta (00000): "))
    nueva_publicidad = int(input("Agregar $ de Publicidad (00000): "))
    excel = excel.append(
        {'Fecha': nueva_fecha,
         'Venta': nueva_venta,
         'Publicidad': nueva_publicidad},
        ignore_index=True
        )
    print("Se ha agregado ", nueva_venta, "en venta y ", nueva_publicidad,
          "en Publicidad", ", con fecha ", nueva_fecha)
    print(excel)

print("No se agregará nuevo dato")
excel.to_excel("ingresos.xlsx")