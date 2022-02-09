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
            #cargardata()
            print("Data cargada")
            print("")
        elif opcion == "2" :
            #cargarinstrucciones()
            print("")
            print("Instrucciones Cargadas")
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
   

Menu()











