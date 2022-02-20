import re
from Mes import *
from Producto import *

class Analizador_Instrucciones:

    def __init__(self, entradainstruccion)

        while contador < len(entradainstruccion):
            state = 1
            contador = 0
            lexema = ""
            if state = 1:

                if re.search(r"[<]", entradainstruccion[contador]):
                    lexema += entradainstruccion[contador]
                    contador += 1
                    state = 1

                elif re.search(r"[¿]", entradainstruccion[contador]):
                    lexema += entradainstruccion[contador]
                    contador += 1
                    state = 1
                    
                elif re.search(r"[¿]", entradainstruccion[contador]):
                    lexema += entradainstruccion[contador]
                    contador += 1
                    state = 1
                    
