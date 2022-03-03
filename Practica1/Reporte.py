from Analizador_Ventas import *
import webbrowser
ventas = Analizador_Ventas()

def Reporte():

    datos = ''
    File = open( "Reporte"+ ".html", "w")

    File.write("""<!DOCTYPE HTML PUBLIC"

    <html>

    <head>
        <title>Reporte</title>
     <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" ></script>
    </head>
    <body class = "fst-italic">
      <h2 style = "background-color:#6c757d">  Leonel Antonio González García</h2> 
      <h2 style = "background-color:#6c757d">  201709088</h2>
     <table class="table table-dark table-borderless">
    
    <thead>
      <tr>
       
        <th><p class="fst-italic">Producto.</p></th>
        <th><p class="fst-italic">Precio.</p></th>
        <th><p class="fst-italic">Cantidad.</p></th>
        <th><p class="fst-italic">Ganancia.</p></th>
        
      </tr>
    </thead>

    """)    
    ordenando_lista =[]
    lista_ordenada = []
    lista = []
    for i in range(len(ventas.Meses)):
      for j in range(len(ventas.Meses[i].getProducto())):
        price = ventas.Meses[i].getProducto()[j].getPrecio()
        quantity = ventas.Meses[i].getProducto()[j].getCantidad()
        gain = ventas.Gains(price,quantity)
        product = ventas.Meses[i].getProducto()[j].getNombre()
        lista.append([product,gain])
        ordenando_lista.append(gain)   

      

    Product = ''
    Price = ''
    Quantity = ''
    Gain = ''

    lista_ordenada = ventas.Bubble_Sort(ordenando_lista)
    size = len(lista_ordenada)
    print(ordenando_lista)

    for i in range(size-1, -1, -1):
      for l in range(len(lista)):
         if lista_ordenada[i] == lista[l][1]:
            Product = lista[l][0]
            Price = ventas.search_price(Product)
            Quantity = ventas.search_quantity(Product)
            Gain =    lista_ordenada[i]
            datos += "<tbody>"
            print("----Productos:  ",Product," ",Price," ",Quantity," ",Gain)
            datos += "<td>"+str(Product)+"</td>"
                           
            datos += "<td>"+str(Price)+"</td>"
            datos += "<td>"+str(Quantity)+"</td>"
            datos += "<td>"+str(Gain)+"</td>"
            datos += "</tbody>"
         
    
    
                  
    
    datos += best_seller()
    File.write(datos)
    
    File.write("""
      </table>
    </div>
        </body>
        </html>""")
    webbrowser.open("Reporte.html")
    File.close

def best_seller():
   
    actual = ''
    actual = int(ventas.Meses[0].getProducto()[0].getCantidad())
    nombre = ''
    for i in range(len(ventas.Meses)):
        
        for j in range(len(ventas.Meses[i].getProducto())):
          
            if actual <= int(ventas.Meses[i].getProducto()[j].getCantidad()):
                actual = int(ventas.Meses[i].getProducto()[j].getCantidad())
                nombre = ventas.Meses[i].getProducto()[j].getNombre()
    
    datos = """
    <div>
    <table class="table table-dark table-borderless">
    <thead>
      <tr>
       
        <p  style = "background-color:#6c757d",class="fst-italic">Producto más vendido.</p>
        <th><p class="fst-italic">Producto.</p></th>
        <th><p class="fst-italic">Cantidad.</p></th>
        
        
      </tr>
      </thead>
      """

    datos+="<tbody>"
    datos += "<td>"+str(nombre)+"</td>"
    datos += "<td>"+str(actual)+"</td>"  
    datos+= "</tbody>"
    datos += """
    
       </table>
    
    """
    ac = ''
    ac = int(ventas.Meses[0].getProducto()[0].getCantidad())
    name = ''
    for i in range(len(ventas.Meses)):
        
        for j in range(len(ventas.Meses[i].getProducto())):
            
            if ac >= int(ventas.Meses[i].getProducto()[j].getCantidad()):
                ac = int(ventas.Meses[i].getProducto()[j].getCantidad())
                name = ventas.Meses[i].getProducto()[j].getNombre()
    datos += """
   
    <table class="table table-dark table-borderless">
    <thead>
      <tr>

        <p style = "background-color:#6c757d",class="fst-italic">Producto menos Vendido.</p>
        <th><p class="fst-italic">Producto.</p></th>
        <th><p class="fst-italic">Cantidad.</p></th>
        
        
      </tr>
     
      </thead>
      """
    datos +="<tbody>"
    datos += "<td>"+str(name)+"</td>"
    datos += "<td>"+str(ac)+"</td>"  
    datos += "</tbody>"
    datos += """
        </table>
    </div>
        """
    
    return datos

def least_sold():
    ac = ''
    ac = int(ventas.Meses[0].getProducto()[0].getCantidad())
    nm = ''
    for i in range(len(ventas.Meses)):
        
        for j in range(len(ventas.Meses[i].getProducto())):
            
            if actual > int(ventas.Meses[i].getProducto()[j].getCantidad()):
                ac = int(ventas.Meses[i].getProducto()[j].getCantidad())
                nm = ventas.Meses[i].getProducto()[j].getNombre()
    
    datos = """
   
    <thead>
      <tr>
       
        <p class="fst-italic">Producto menos Vendido.</p>
        <th><p class="fst-italic">Producto.</p></th>
        <th><p class="fst-italic">Cantidad.</p></th>
        
        
      </tr>
      </thead>
      """
    datos+=  "<tbody>"
    datos += "<td>"+str(nm)+"</td>"
    datos += "<td>"+str(ac)+"</td>"  
    datos += "</tbody>"
    datos += """
    </table>
    </div>
        
    """
    return datos




