#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:31:14 2020

@author: usuario
"""
# Let's import tkinter 
from tkinter import *
import pandas as pd
#import tkinter as tk

# Get and store data from users 
nueva_fecha = str()
nueva_venta = int()
nueva_publicidad = int()

nueva_fecha_info = str(nueva_fecha.get())
nueva_venta_info = int(nueva_venta.get())
nueva_publicacion_info = int(nueva_publicidad.get())

# Manipulate data from registration fields 
def send_data():
    nueva_fecha_info
    nueva_venta_info
    nueva_publicacion_info
#  Open and write data to a file
excel = pd.read_excel('ingresos.xlsx', index_col=0)
excel = excel.append(
        {'Fecha': nueva_fecha_info, 
         'Venta': nueva_venta_info, 
         'Publicidad': nueva_publicidad_info}, 
         ignore_index=True)
#  Delete data from previous event
nueva_fecha.delete(0, END)
nueva_venta.delete(0, END)
nueva_publicidad.delete(0, END)

# Create new instance - Class Tk()  
mywindow = Tk()
mywindow.geometry("500x400")
mywindow.title("Registros Haru Creaciones")
mywindow.resizable(False,False)
mywindow.config(background = "#213141")
main_title = Label(text = "REGISTROS DE LUCAS", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()

# Define Label Fields 
username_label = Label(text = "Fecha", bg = "#FFEEDD")
username_label.place(x = 22, y = 70)
password_label = Label(text = "Nueva Venta", bg = "#FFEEDD")
password_label.place(x = 22, y = 130)
fullname_label = Label(text = "Nueva Publicación", bg = "#FFEEDD")
fullname_label.place(x = 22, y = 190)
 

 
nueva_fecha_entry = Entry(textvariable = nueva_fecha, width = "40")
nueva_venta_entry = Entry(textvariable = nueva_venta, width = "40")
nueva_publicidad_entry = Entry(textvariable = nueva_publicidad, width = "40")
 
nueva_fecha_entry.place(x = 22, y = 100)
nueva_venta_entry.place(x = 22, y = 160)
nueva_publicidad_entry.place(x = 22, y = 220)
 
# Submit Button
submit_btn = Button(mywindow,text = "Agregar Datos", width = "30", height = "2", command = send_data, bg = "#00CD63")
submit_btn.place(x = 22, y = 320)

excel.to_excel("ingresos.xlsx")
mywindow.mainloop()