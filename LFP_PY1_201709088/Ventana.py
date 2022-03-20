from tkinter import Tk
from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from Analizador_lexico import Analizador_lexico
from ErrorReporte import reporterror
from TokenReporte import reportoken
import webbrowser

Data = ""
def ventana_carga():
    #Abre Ventana para Buscar el archivo .lfp 
    archivo =  filedialog.askopenfilename(initialdir = "/") 
    #Abre el achivo 
    archivo = open(archivo ,'r')
    read = archivo.read()
    archivo.close()
    global Data
    Data = read
    Data = textfield.insert(INSERT, Data)
    Data = textfield.get("1.0","end-1c")
    print("===================================================")
    print(Data)
    
def Analizando():
    global Data 
    Data = textfield.get("1.0","end-1c")
    print(Data)
    entry = Analizador_lexico()
    entry.analizador(Data)
    f = open ("Analizador.txt","w")
    f.write(Data)
    f.close()
    

def Reportando():
    reportes = combo.get()
    global Data

    Data = textfield.get("1.0","end-1c")
    lexema = Analizador_lexico()
    lexema.analizador(Data)

    if reportes == "Reporte de Tokens":
        lexema.ErrorToken()
    elif reportes == "Reporte de Errores":
        lexema.ErrorReporte()
    elif reportes == "Manual de Usuario":
        webbrowser.open("Manual de Usuario.pdf")
    elif reportes == "Manual Técnico":
        webbrowser.open("Manual Tecnico.pdf")

ventana = Tk()
ventana.title("PROYECTO")
ventana.geometry("%dx%d+%d+%d" % (900,500,350,100))
ventana.resizable(0,0)

panel_Frame = Frame(ventana)
panel_Frame.pack(side = "top")
panel_Frame.place(width = "900", height = "500")
panel_Frame.config(background = "gray")


textfield = Text(panel_Frame)
textfield.pack()
textfield.place(x= "165", y = "20",width = "720", height = "470")
scrollbar = Scrollbar(ventana, command = textfield.yview)
scrollbar.pack()
scrollbar.place(x = "880", y = "20", width = "20", height = "470")
textfield.config(yscrollcommand = scrollbar)


button = Button(panel_Frame, text="Cargar", command = ventana_carga,  foreground = "white")
button.pack()
button.config(bg = "black")
button.place(x = 10,y = 20,width= 150, height  = 40)

button = Button(panel_Frame, text="Analizar", command = Analizando,  foreground = "white")
button.pack()
button.config(bg = "black")
button.place(x = 10,y = 65,width= 150, height  = 40)

combo = ttk.Combobox (panel_Frame, values = ["Reporte de Tokens","Reporte de Errores","Manual de Usuario","Manual Técnico"])
combo.pack()
combo.config(background = "black")
combo.current(0)
combo.place(x=10, y = 115, width = "150", height = "40")

buttonabrir = Button(panel_Frame, text="Seleccionar Reporte",command = Reportando, foreground = "white")
buttonabrir.pack()
buttonabrir.config(bg = "black")
buttonabrir.place(x= 10, y=140, width = "150", height = "40")



ventana.mainloop()








    