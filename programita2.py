#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 20:24:40 2020

@author: Edgard Gonzalez
"""
import pandas as pd

AgregarNuevo = input("Quiere agregar nuevo dato? (si/no): ")

while AgregarNuevo == "si":
    NuevaFecha = input("Agregar Fecha (dd/mm/yyyy): ")
    NuevaVenta = int(input("Agregar $ de Venta (00000): "))
    NuevaPublicidad = int(input("Agregar $ de Publicidad (00000): "))
    print("Se ha agregado ", NuevaVenta, "en venta y ", NuevaPublicidad,
          "en Publicidad", ", con fecha ", NuevaFecha)
    data = pd.DataFrame(columns=('Fecha', 'Venta', 'Publicidad'))
    data.loc[len(data)] = [NuevaFecha, NuevaVenta, NuevaPublicidad]
    print(data)
    data.to_excel("ingresos.xlsx")
    AgregarNuevo = input("Quiere agregar nuevo dato? (si/no): ")
else:
    print("No hay mano")