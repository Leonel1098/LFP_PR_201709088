import os
import tkinter
from tkinter import Tk 
from tkinter import filedialog
import io
from io import*
from Analizador_Ventas import *
from Mes import *
from Producto import *
from Reporte import *
ventas = Analizador_Ventas()
Datos = ""

def Menu():
    opcion = True  
    
    while opcion :
        
        print("**** Funciones del Sistema ****")
        print("** Elija una opción **")
        print("1. Cargar Datos")
        print("2. Cargar Instrucciones")
        print("3. Analizar")
        print("4. Reportes")
        print("5. Salir")
        opcion = input ("")
        if opcion == "1" :
            print("")
            print("---------- Data Cargada -----------")
            Ventana_CargarVentas()
            
            print("")

        elif opcion == "2" :
            print("")
            print("--------- Instrucciones Cargadas ----------")
            Ventana_CargarInstrucciones()
            print("")

        elif opcion == "3" :
            print("")
            print("---------- Análisis Hecho ----------")
            global Datos
            #print(Datos)
            ventas.analizador_ventas(Datos)
            print("")

        elif opcion == "4" :
            print("")
            print("Reportes hechos")
            Reporte()
            print("")

        elif opcion == "5" :
            print("Gracias, vuelve pronto :)")
            opcion = False
            
        else:
            input("Ingrese una opción válida :)")
            print("")

def Ventana_CargarVentas():
    archivo =  filedialog.askopenfilename(initialdir = "/") 
    ventas_upload = open(archivo ,'r',encoding ="utf8")
    read = ventas_upload.read()
    ventas_upload.close()
    global Datos
    Datos = read
    print(Datos)
    

def Ventana_CargarInstrucciones():
    archivo =  filedialog.askopenfilename(initialdir = "/")
    instrucciones_upload = open(archivo, 'r',encoding = "utf8")
    read = instrucciones_upload.read()
    instrucciones_upload.close()
    print(read)


if __name__ == "__main__":
    Menu()



    











