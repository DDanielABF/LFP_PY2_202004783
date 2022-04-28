from tkinter import *
from tkinter import Text
from tkinter import filedialog
from tkinter import Canvas
from tkinter import scrolledtext
from tkinter.tix import ComboBox
from turtle import width
from tkinter import ttk
import csv
from objetoBOT import BOT
#from AnalizadorLexico import AnalizadorLexico
#from Token import Token
#from Error import Error
form =Tk()
form.title('LIGA BOT')#titulo de ventana
#form.iconbitmap("icono.ico")
form.config(bg='black' ) # color de fondo 
form.config(cursor="man")
ventanaP = Frame() # crear ventana
ventanaP.pack(fill="both",expand="True") # agarralo a la raiz
ventanaP.config(bg="light blue")
ventanaP.pack(fill="both", expand=True)
ventanaP.config(width="1300", height="1300")

ventanaP.config(bd="15")
ventanaP.config(relief="raised")
ventanaP.config(cursor="iron_cross")
textt = Text(ventanaP)
data = []
with open('LaLigaBot-LFP.csv') as a:
    reader = csv.reader(a)
    for i in reader:
        data.append(BOT(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    print(repr(data))
def data():
  
    data = []
    with open('LaLigaBot-LFP.csv') as a:
        reader = csv.reader(a)
        for i in reader:
            data.append(BOT(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        print(repr(data))
#textt["font"] = fuente
textt.place(x=75,y=75,width= 550, height=440)

textt.insert(INSERT, "Bienvenido a la Liga Bot, Ingrese un comando\n")

textt1 = Text(ventanaP)
#textt1["font"] = fuente
textt1.place(x=75,y=525,width= 550, height=40)
limpiar_tok=Button(ventanaP)

limpiar_tok["justify"] = "center"
limpiar_tok["text"] = "Reporte Tokens"
limpiar_tok.place(x=640,y=310,width=140,height=50)
#limpiar_tok["command"] = guardar_Archivo 

reporte_t=Button(ventanaP)
reporte_t["justify"] = "center"
reporte_t["text"] = "Limpiar log tokens"
reporte_t.place(x=640,y=240,width=140,height=50)
#reporte_t["command"] = guardar_Archivo 

limpiar_err=Button(ventanaP)

limpiar_err["justify"] = "center"
limpiar_err["text"] = "Reporte Errores"
limpiar_err.place(x=640,y=170,width=140,height=50)
#limpiar_err["command"] = guardar_Archivo 

reporte_e=Button(ventanaP)

reporte_e["justify"] = "center"
reporte_e["text"] = "Limpiar Log errores"
reporte_e.place(x=640,y=100,width=140,height=50)
#reporte_e["command"] = guardar_Archivo 

enviar=Button(ventanaP)
enviar["justify"] = "center"
enviar["text"] = "Enviar"
enviar.place(x=640,y=520,width=140,height=50)
enviar["command"] = data

form.mainloop()