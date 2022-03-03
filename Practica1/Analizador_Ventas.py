import re
import locale
from Mes import *
from Producto import *

class Analizador_Ventas:

    # Variables Golobales en las que se guardará los paramétros del objeto producto
    month_name = ''
    year_name = ''
    product_name = ''
    product_price =''
    product_quantity = ''
     # En esta lista se agregaran los productos analizados por mes
    Productos = []
    # En está lista se agregan el mes  
    Meses=[]
    
    def __init__(self):
        pass
    
    # Método encargado de hacer el análisis léxico del archivo .data que se carga.
    def analizador_ventas(self, entrada):
        
        state = 1
        contador = 0
        lexema = ""
       
      
        while contador < len(entrada):
           
             #State 1 se encarga de realizar la verificación de los caráteres del archivo cargado.

            if state == 1:

                #Verifica si el caracter es una letra y analiza hasta que termine de leer el nombre.
                
                if re.search(r"[a-zA-Z]", entrada[contador]):
                     #print(lexema)
                     lexema += entrada[contador]
                     contador += 1
                     state = 1

                # Al encontrar ":" salta al State 2 para analizar el año 

                elif re.search(r"[:]" , entrada[contador]):

                    #Guarda los caracteres del nombre del mes 

                    namemonth = lexema
                    #print(lexema)

                    #Se agrea el nombre a la variable global y se convierte todo a mayúsculas

                    global month_name
                    month_name = lexema.upper()

                    #Imprime el nombre del mes y envía al State 2 para analizar el año

                    print("---------------Nuevo Mes---------------")
                    print("Nombre del Mes: ", month_name)
                    state = 2
                    lexema = ''

                    #Al econtrar un parentésis de apertura salta al State 3 para analizar el producto

                elif re.search(r"[(]", entrada[contador]):
                     state = 3
                     contador += 1

                    # Al encontrar un salto de línea regresa al estado uno para verificar la sintaxis de nuevo.

                elif re.search(r"[\n]", entrada[contador]):
                     state = 1
                     contador += 1
                
                #Si no encuentra el caracter sigue verificando

                else:
                     lexema += entrada[contador]
                     state = 1 
                     contador += 1

            # Al llegar al State 2 comienza el análisis del año

            if state == 2:

                # Sí lee números significa que está leyendo el año 

                if re.search(r"[0-9]", entrada[contador]):
                    lexema += entrada[contador]
                    contador +=1
                    state = 2

                #elif re.search(r"[:]", entrada[contador]):
                    #state = 2
                    #contador+=1

                # Al econtrar el igual termina con el año
                	
                elif re.search(r"[=]", entrada[contador]):
                    nameyear=lexema
                    #print(lexema)

                    #Agre el año a la variable global y la imprime

                    global year_name
                    year_name = lexema.upper()
                    print("Año del Mes: ",year_name)
                    contador += 1
                    state = 1
                    lexema =''

                else:
                    #Si no encuentra el caracter sigue verificando
                    lexema += entrada[contador]
                    contador += 1
                    state = 2 
                   
            
            # En State 3 se analizan los productos    
             
            if state == 3:

                if re.search(r"[\[]", entrada[contador]):
                    contador += 1
                    state = 4 
                
                elif re.search(r"[ ]", entrada[contador]):
                    state=3
                    contador += 1
                
                # Al llegar a un ; el contenido del producto termina y continua con el siguiente

                elif re.search(r"[;]", entrada[contador]):
                    contador += 1
                    state = 3
                    lexema = ''

                elif re.search(r"[\n]", entrada[contador]):
                    contador += 1
                    state = 3

                # Cuando llega a un ) significa que el mes ha terminado

                elif re.search(r"[)]", entrada[contador]):

                    # Aquí va agregando cada mes analizado a la lista Meses

                    self.CreateMonth()

                    # Limpia las variables para regresar al State 1 
                    mes_name =''
                    año_name =''
                    contador +=1
                    state = 1
                
                else :
                    #Si no encuentra el caracter sigue verificando
                    lexema += entrada[contador]
                    contador += 1
                    state = 3

            #En State 4 analiza el nombre del producto

            if state == 4 :     

                if re.search(r"[a-zA-Z]", entrada[contador]):
                    lexema += entrada[contador]
                    contador += 1
                    state = 4

                elif re.search(r"[0-9]", entrada[contador]):
                    lexema += entrada[contador]
                    contador += 1
                    state = 4

                elif re.search(r"[ ]", entrada[contador]):
                    lexema += entrada[contador]
                    contador += 1
                    state = 4
                
                elif re.search(r"[\"]", entrada[contador]):
                    contador +=1
                    state = 4

                    # Al encontrar una "," significa que el nombre de producto termina e inicia el precio del producto por eso salta a State 5 

                elif re.search(r"[,]", entrada[contador]):

                    #Imprime el nombre del producto nuevo

                    print("----------Nuevo Producto-------------")
                    #print(lexema)
                    global product_name
                    product_name = lexema.upper()
                    #product_name = product_name.upper()
                    print("Nombre del Producto: ", product_name)
                    contador += 1
                    state = 5 
                    lexema = ''
                
                elif re.search(r"[\“]", entrada[contador]):
                    contador += 1
                    state = 4

                elif re.search(r"[\”]", entrada[contador]):
                    contador += 1
                    state = 4

                else : 
                    contador +=1
                    state = 3

            # El state 5 se encarga de verificar el precio de cada producto

            if state == 5:

                if re.search(r"[0-9]", entrada[contador]):
                    lexema += entrada[contador]
                    state = 5
                    contador += 1

                elif re.search(r"[\.]", entrada[contador]):
                    lexema += entrada[contador]
                    state = 5
                    contador += 1

                elif re.search(r"[ ]", entrada[contador]):
                    contador += 1
                    state = 5

                   # Al encontrar una "," significa que el precio de producto termina e inicia la cantidad del producto por eso salta a State 6

                elif re.search(r"[,]", entrada[contador]):
                    contador += 1
                    state = 6
                    #print(lexema)

                    #Imprime el precio del producto

                    global product_price
                    product_price = lexema
                    print("Precio del Producto: ", product_price)
                    lexema = ''

                else :
                    state = 4
                    contador +=1


            # Al llegar a State 6 analiza la cantidad de cada producto

            if state ==6:

                    if re.search(r"[0-9]", entrada[contador]):
                        lexema += entrada[contador]
                        state = 6
                        contador +=1
 
                    elif re.search(r"[]]", entrada[contador]):
                        contador += 1
                        #print(lexema)

                        #Imprime la cantidad del producto

                        global product_quantity
                        product_quantity = lexema
                        print("Cantidad del Producto: ", product_quantity)
                        state= 5
                        lexema = ''
                        self.CreatingProduct()
                           
                    elif re.search(r"[ ]", entrada[contador]):
                        contador += 1
                        state = 6
                    
                    else :
                        print ("regresa por ", entrada[contador])
                        state = 5
                        contador +=1
        
            if state == 0:
                break
    
            
            
    def hola(self):
        print("asdfasdfasdfasdf")
    
   

    # Se Crea el objeto del producto que recibirá los argumentos de los productos 

    def CreatingProduct(self):
        global product_price
        global product_quantity
        global product_name

        """print("-------"product_name)
        print("-------"product_price)
        print("-------"product_quantity)"""

        #Objeto del producto nuevo 

        Create_Product = Producto(product_name,product_price,product_quantity)

        #Se agrega la lista         
          
        self.Productos.append(Create_Product)     
                    
    

    # Se Crea el objeto del mes que recibirá los argumentos del mes y la lista de productos
     
    def CreateMonth(self):
            global month_name
            global year_name
            nuevo = Mes(month_name, year_name,self.Productos)
            self.Meses.append(nuevo)
            self.Productos=[]

    # Este método calcula las ganancias totales

    def Gains(self,price,quantity):
        a = price
        b = quantity

        # Se combia el signo de los decimales del "." a "," para que lo tome en cuenta como float

        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
        gain = locale.atof(a) * locale.atof(b)
        return gain

    #Los métodos search sirven para buscar el precio y la cantidad de los productos
    
    def search_price(self,nameproduct):
        price = ''
        for i in range(len(self.Meses)):
            for j in range(len(self.Meses[i].getProducto())):
                if nameproduct == self.Meses[i].getProducto()[j].getNombre():
                    price = self.Meses[i].getProducto()[j].getPrecio()
        return price

    def search_quantity(self,nameproduct):
        quantity =''
        for i in range(len(self.Meses)):
            for j in range(len(self.Meses[i].getProducto())):
                if nameproduct == self.Meses[i].getProducto()[j].getNombre():
                    quantity = self.Meses[i].getProducto()[j].getCantidad()
        return quantity

    # En este método se utiliza el ordenamiento burbuja para manejar los datos de los productos

    def Bubble_Sort(self,ordenando_lista):
        count = len(ordenando_lista)

        for i in range(count-1):
            for j in range(0, count-i-1):
                if ordenando_lista[j] > ordenando_lista[j + 1] :
                   ordenando_lista[j], ordenando_lista[j + 1] = ordenando_lista[j + 1], ordenando_lista[j] 
        return ordenando_lista
       

    

    



