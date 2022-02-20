class Mes:

    def __init__(self, nombre, año, producto=[]):
        self.nombre = nombre
        self.año = año
        self.producto = producto
    
        #Métodos set
    def setNombre (self,nombre):      
        self.nombre = nombre

    def setAño (self,año):      
        self.año = año

    def setProducto (self,producto):      
        self.producto = producto

    #Métodos get
    def getNombre (self):      
        return self.nombre

    def getAño (self):    
        return self.año

    def getProducto (self):      
        return self.producto

