import os
import tkinter
from tkinter import Tk 
from tkinter import filedialog
import io
from io import*


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
            print("Data cargada")
            Ventana_CargarVentas()
            print("")
        elif opcion == "2" :
            print("")
            print("Instrucciones Cargadas")
            Ventana_CargarInstrucciones()
            print("")
        elif opcion == "3" :
           #analizar()
            print("")
            print("Analisis hecho")
            print("")
        elif opcion == "4" :
            #reportes()
            print("")
            print("Reportes hechos")
            print("")
        elif opcion == "5" :
            print("Gracias, vuelve pronto :)")
            opcion = False
            
        else:
            input("Ingrese una opción válida :)")
            print("")

def Ventana_CargarVentas():
    root = Tk()
    archivo =  filedialog.askopenfilename(initialdir = "/") 
    ventas_upload = open(archivo ,'r',encoding ="utf8")
    read = ventas_upload.read()
    ventas_upload.close()
    print(read)
    root = destroyer()

def Ventana_CargarInstrucciones():
    root=Tk()
    archivo =  filedialog.askopenfilename(initialdir = "/")
    instrucciones_upload = open(archivo, 'r',encoding = "utf8")
    read = instrucciones_upload.read()
    instrucciones_upload.close()
    print(read)
    root = destroyer()

if __name__ == "__main__":
    Menu()



    











