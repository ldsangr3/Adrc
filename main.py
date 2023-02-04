#CÓDIGO FOTOBIORREACTORES CONTINUOS VERSIÓN ACTUALIZADA 3:59PM 09/12/2021
#Álvaro Pulido Aponte
#Nota: ante cualquier modificación del código por favor generar bakup previo sin modificaciones, cambiar fecha, hora y nombre del editor


#IMPORTAR LIBRERÍAS
#from cProfile import label
#from distutils.cmd import Command
#from msilib.schema import SelfReg
import tkinter as tk #TKINTER ES PARA INTERFAZ GRÁFICA
from tkinter import * #IMPORTAR TODOS LOS MÓDULOS
from tkinter import ttk #PAQUETE TTK
import time
from typing_extensions import Self #RETARDOS
import numpy as np #LIBRERÍA FUNCIONES MATEMÁTICAS
from numpy import interp #FUNCIÓN INTERPOLACIÓN ANÁLOGA A MAP EN ARDUINO
import matplotlib.pyplot as plt #LIBRERÍA GRÁFICAS 
plt.style.use('ggplot') #ESTILO DEL PLOT
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #GUI CANVAS
from drawnow import * #GRÁFICAR EN TIEMPO REAL
import atexit #GESTOR DE SALIDA
from collections import deque #LIBRERÍA COLLECTIONS, PAQUETE DEQUE PARA GESTIONAR COLAS
from datetime import datetime #FORMATO TIEMPO REAL
from matplotlib.animation import FuncAnimation #MOVIMIENTO DE LAS GRÁFICAS
from matplotlib import pyplot
from random import randrange #NÚMEROS ALEATORIOS
import multiprocessing #EJECUTA VARIAS RUTINAS DE FORMA PARALELA
from threading import Thread #EVITAN EL ENCLAVAMIENTO DE LOS BOTONES
import pandas #PARA GENERAR FORMATOS CSV
import openpyxl #LEER Y ESCRIBIR TABLAS EXCEL
from ljm1 import Ljm  #LIBRERÍA LabJack1
from ljm2 import Ljm2 #LIBRERIA LabJack2



tarjeta1=Ljm() #CREAR UN OBJETO LLAMADO TARJETA1 DE LA CLASE LJM
tarjeta2 = Ljm2() #LO MISMO PERO CON LJM2
comunicacion = Ljm() #CREA UN OBJETO ESPECÍFICO DE LA MISMA CLASE PARA LA COMUNICACIÓN
comunicacion2 = Ljm2() #LO MISMO PERO CON LJM2

        
class Principal(): #CLASE PRINCIPAL DE ESTE SCRIPT
    def __init__(self): #MÉTODO INIT INICIALIZA LAS VARIABLES Y PARÁMETROS DE OPERACIÓN
        ventana=Tk() #CREAR VENTANA DEL GUI
        notebook=ttk.Notebook(ventana) #CREAR OBJETO PARA GESTIONAR LAS PESTAnhAS
        notebook.pack(fill='both',expand='yes') #CONFIGURACIÓN PESTAnhAS
        pestanha1=tk.Frame(notebook,bg='white') #CREAR UN FRAME DE COLOR BLANCO PARA LA PESTAnhA 1
        pestanha2=tk.Frame(notebook,bg='white') #IGUAL PERO PARA LA PESTAnhA 2
        pestanha3=tk.Frame(notebook,bg='white') #LO MISMO PARA LA PESTAnhA 3
        notebook.add(pestanha1,text='FBR1') #ASIGNACIÓN PESTAnhAS FBR1,FBR2 Y FBR3
        notebook.add(pestanha2,text='FBR2') #""
        notebook.add(pestanha3,text='FBR3') #""
#1
#CREACIÓN, CONFIGURACIÓN Y ASIGNACIÓN DE SUBPESTAnhAS QUE CONTIENEN LAS GRÁFICAS DE CADA VARIABLE MEDIDA EN PESTAnhA FBR1
        right_frame = tk.Frame(pestanha1, bg='#C0C0C0', bd=1.5) #bg=color; bd=tamanho del borde en pixeles
        right_frame.place(relx=0.3, rely=0.055, relwidth=0.65, relheight=0.8) #posicionamiento de elementos horizontal,vertical,ancho,largo
        notebook1=ttk.Notebook(right_frame)
        notebook1.pack(fill='both',expand='yes')
        pestanha4=ttk.Frame(notebook1)
        pestanha5=ttk.Frame(notebook1)
        pestanha6=ttk.Frame(notebook1)
        pestanha7=ttk.Frame(notebook1)
        pestanha8=ttk.Frame(notebook1)
        pestanha9=ttk.Frame(notebook1)
        notebook1.add(pestanha4,text=' Temperatura ')
        notebook1.add(pestanha5,text='     Luz     ')
        notebook1.add(pestanha6,text='  Nivel  ')       
        notebook1.add(pestanha7,text='  pH  ')
        notebook1.add(pestanha8,text='  OD  ')
        notebook1.add(pestanha9,text='  Biomasa  ')
#2
#CREACIÓN, CONFIGURACIÓN Y ASIGNACIÓN DE SUBPESTAnhAS QUE CONTIENEN LAS GRÁFICAS DE CADA VARIABLE MEDIDA EN PESTAnhA FBR2
        right_frame2 = tk.Frame(pestanha2, bg='#C0C0C0', bd=1.5)
        right_frame2.place(relx=0.3, rely=0.055, relwidth=0.65, relheight=0.8)
        notebook2=ttk.Notebook(right_frame2)
        notebook2.pack(fill='both',expand='yes')
        pestanha10=ttk.Frame(notebook2)
        pestanha11=ttk.Frame(notebook2)
        pestanha12=ttk.Frame(notebook2)
        pestanha13=ttk.Frame(notebook2)
        pestanha14=ttk.Frame(notebook2)
        pestanha15=ttk.Frame(notebook2)
        notebook2.add(pestanha10,text=' Temperatura ')
        notebook2.add(pestanha11,text='     Luz     ')
        notebook2.add(pestanha12,text='  Nivel  ')       
        notebook2.add(pestanha13,text='  pH  ')
        notebook2.add(pestanha14,text='  OD  ')
        notebook2.add(pestanha15,text='  Biomasa  ')
#3
#CREACIÓN, CONFIGURACIÓN Y ASIGNACIÓN DE SUBPESTAnhAS QUE CONTIENEN LAS GRÁFICAS DE CADA VARIABLE MEDIDA EN PESTAnhA FBR3
        right_frame3 = tk.Frame(pestanha3, bg='#C0C0C0', bd=1.5)
        right_frame3.place(relx=0.3, rely=0.055, relwidth=0.65, relheight=0.8)
        notebook3=ttk.Notebook(right_frame3)
        notebook3.pack(fill='both',expand='yes')
        pestanha16=ttk.Frame(notebook3)
        pestanha17=ttk.Frame(notebook3)
        pestanha18=ttk.Frame(notebook3)
        pestanha19=ttk.Frame(notebook3)
        pestanha20=ttk.Frame(notebook3)
        pestanha21=ttk.Frame(notebook3)
        notebook3.add(pestanha16,text=' Temperatura ')
        notebook3.add(pestanha17,text='     Luz     ')
        notebook3.add(pestanha18,text='  Nivel  ')       
        notebook3.add(pestanha19,text='  pH  ')
        notebook3.add(pestanha20,text='  OD  ')
        notebook3.add(pestanha21,text='  Biomasa  ')
        
#VENTANA GENERAL        
        ventana.title('Interfaz de control FotoBioReactores continuos')
        ventana.geometry('1100x720') #TAMAnhO DE LA VENTANA EN PIXELES
        ventana.configure(background='white') #COLOR DE FONDO
        menubar = Menu(ventana) #CREACIÓN BARRA DE MENU
        ventana.config(menu=menubar) 
        menu_archivo = Menu(menubar, tearoff=0)  #ELEMENTOS BARRA DE MENU
        menu_archivo.add_command(label="New")
        menu_archivo.add_command(label="Open")
        menu_archivo.add_command(label="Save")
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=ventana.destroy)

        # Aqui se llama la ventana
        menu_edicion = Menu(menubar, tearoff=0)
        menu_ayuda = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=menu_archivo)
        menubar.add_cascade(label="Edit", menu=menu_edicion)
        menubar.add_cascade(label="Help", menu=menu_ayuda)

        # Menu ayuda
        
        menu_ayuda.add_command(label="About", command=self.f_acerca) #f.acerca=MÉTODO CON LA FIGURA AGRADECIMIENTO
        menu_ayuda.add_command(label="Thanks", command=self.f_about) # Metodo de los agradecimientos
        #menu_ayuda.add_command(Label="Acerca", menu=menu_archivo)

#PARÁMETROS CONTROLADORES
#1
        self.error_anterior_luz1 = 0
        self.integral_anterior_luz1 = 0
        self.kp_luz1 = 3
        self.ki_luz1 = 2
        self.kd_luz1 = 0
        self.bias_luz1 = 0
        self.error_anterior_temp1 = 0
        self.integral_anterior_temp1 = 0
        self.kp_temp1 = 32.4
        self.ki_temp1 = 22.9
        self.kd_temp1 = 0.9
        self.bias_temp1 = 0
#2
        self.error_anterior_luz2 = 0
        self.integral_anterior_luz2 = 0
        self.kp_luz2 = 3
        self.ki_luz2 = 2
        self.kd_luz2 = 0
        self.bias_luz2 = 0
        self.error_anterior_temp2 = 0
        self.integral_anterior_temp2 = 0
        self.kp_temp2 = 32.4
        self.ki_temp2 = 22.9
        self.kd_temp2 = 0.9
        self.bias_temp2 = 0
#3
        self.error_anterior_luz3 = 0
        self.integral_anterior_luz3 = 0
        self.kp_luz3 = 3
        self.ki_luz3 = 2
        self.kd_luz3 = 0
        self.bias_luz3 = 0
        self.error_anterior_temp3 = 0
        self.integral_anterior_temp3 = 0
        self.kp_temp3 = 32.4
        self.ki_temp3 = 22.9
        self.kd_temp3 = 0.9
        self.bias_temp3 = 0
#-o-
#TABLAS
        self.lista_temp1=list()
        self.lista_temp2=list()
        self.lista_temp3=list()
        self.lista_luz1=list()
        self.lista_luz2=list()
        self.lista_luz3=list()
        self.lista_nivel1=list()
        self.lista_nivel2=list()
        self.lista_nivel3=list()
        self.lista_pH1=list()
        self.lista_pH2=list()
        self.lista_pH3=list()
        self.lista_DO1=list()
        self.lista_DO2=list()
        self.lista_DO3=list()
#-o-
#EJES DE ABSCISAS Y ORDENADAS PARA CADA UNA DE LAS GRÁFICAS
#fbr1
        self.x = []
        self.y = []
        self.x1 = []
        self.y1 = []
        self.x2 = []
        self.y2 = []
        self.x3 = []
        self.y3 = []
        self.x4 = []
        self.y4 = []
        self.x5 = []
        self.y5 = []
#fbr2
        self.x_2 = []
        self.y_2 = []
        self.x1_2 = []
        self.y1_2 = []
        self.x2_2 = []
        self.y2_2 = []
        self.x3_2 = []
        self.y3_2 = []
        self.x4_2 = []
        self.y4_2 = []
        self.x5_2 = []
        self.y5_2 = []
#fbr3
        self.x_3 = []
        self.y_3 = []
        self.x1_3 = []
        self.y1_3 = []
        self.x2_3 = []
        self.y2_3 = []
        self.x3_3 = []
        self.y3_3 = []
        self.x4_3 = []
        self.y4_3 = []
        self.x5_3 = []
        self.y5_3 = []
#-o-
#CREACIÓN DE CADA UNO DE LOS ENTORNOS WIDGETS Y SU RESPECTIVA CONFIGURACIÓN
#######################################################################################################################
### FOTOBIORREACTOR 1##################################################################################################
#######################################################################################################################
        etiqueta2=Label(pestanha1,text="Luz",font=("arial",15),bg=('white')).place(x=10,y=10)
        etiqueta3=Label(pestanha1,text="Color",font=("arial",14),bg=('white')).place(x=10,y=40)
        rcolor1=IntVar()
        R1 = Radiobutton(pestanha1, text="Rojo",
                                      variable=rcolor1, value=1,command=self.color_rojo1,font=("arial",10),bg=('white')).place(x=10,y=70)
        R2 = Radiobutton(pestanha1, text="Verde",
                                        variable=rcolor1, value=2, command=self.color_verde1,font=("arial",10),bg=('white')).place(x=10,y=90)
        R3 = Radiobutton(pestanha1, text="Azul",
                                        variable=rcolor1, value=3, command=self.color_azul1,font=("arial",10),bg=('white')).place(x=10,y=110)
        R4 = Radiobutton(pestanha1, text="Blanco",
                         variable=rcolor1, value=3, command=self.color_rojo1,font=("arial",10),bg=('white')).place(x=10,y=130)
        self.luz1=DoubleVar()
        escala_intensidad_luz=Scale(pestanha1,variable=self.luz1,
                                                 from_ = 1, to = 900, orient = HORIZONTAL,length=216,bg=('#BDBDBD')).place(x=80,y=70)
        entrada1 = ttk.Entry(pestanha1, width=30, textvariable=self.luz1,font=("arial",10)).place(x=80,y=110)
        etiqueta4=Label(pestanha1,text="Intensidad del color",font=("arial",12),bg=('white')).place(x=140,y=40)
        etiqueta5=Label(pestanha1,text="Temperatura",font=("arial",15),bg=('white')).place(x=10,y=165)
        etiqueta6 = Label(pestanha1, text="Ref:",font=("arial",12),bg=('white')).place(x=10,y=195)
        self.temperatura1=DoubleVar()
        escala_ref_temperatura1=Scale(pestanha1,variable=self.temperatura1,
                                                 from_ = 1, to = 92, orient = HORIZONTAL,length=216,bg=('#BDBDBD')).place(x=80,y=195)
        entrada2 = ttk.Entry(pestanha1, width=30, textvariable=self.temperatura1,font=("arial",10)).place(x=80,y=235)
        etiqueta5=Label(pestanha1,text="Nivel",font=("arial",15),bg=('white')).place(x=10,y=265)
        etiqueta6 = Label(pestanha1, text="Ref:",font=("arial",12),bg=('white')).place(x=10,y=295)
        self.nivel1=DoubleVar()
        escala_ref_nivel1=Scale(pestanha1,variable=self.nivel1,
                                                 from_ = 1, to = 25, orient = HORIZONTAL,length=216,bg=('#BDBDBD')).place(x=80,y=295)
        entrada3 = ttk.Entry(pestanha1, width=30, textvariable=self.nivel1,font=("arial",10)).place(x=80,y=335)
        boton1=Button(pestanha1,text="Iniciar",command=self.accion_boton,width=30).place(x=80,y=365)
        boton2=Button(pestanha1,text="Detener",command=self.accion_boton4,width=30).place(x=80,y=400)

#######################################################################################################################
### FOTOBIORREACTOR 2##################################################################################################
#######################################################################################################################   
        etiqueta2=Label(pestanha2,text="Luz",font=("arial",15),bg=('white')).place(x=10,y=10)
        etiqueta3=Label(pestanha2,text="Color",font=("arial",14),bg=('white')).place(x=10,y=40)
        rcolor2=IntVar()
        R1 = Radiobutton(pestanha2, text="Rojo",
                                      variable=rcolor2, value=1,command=self.color_rojo2,font=("arial",10),bg=('white')).place(x=10,y=70)
        R2 = Radiobutton(pestanha2, text="Verde",
                                        variable=rcolor2, value=2, command=self.color_verde2,font=("arial",10),bg=('white')).place(x=10,y=90)
        R3 = Radiobutton(pestanha2, text="Azul",
                                        variable=rcolor2, value=3, command=self.color_azul2,font=("arial",10),bg=('white')).place(x=10,y=110)
        R4 = Radiobutton(pestanha2, text="Blanco",
                         variable=rcolor1, value=3, command=self.color_azul2,font=("arial",10),bg=('white')).place(x=10,y=130)
        self.luz2=DoubleVar()
        escala_intensidad_luz=Scale(pestanha2,variable=self.luz2,
                                                 from_ = 1, to = 900, orient = HORIZONTAL,length=216,bg=('#BDBDBD')).place(x=80,y=70)
        entrada1 = ttk.Entry(pestanha2, width=30, textvariable=self.luz2,font=("arial",10)).place(x=80,y=110)
        etiqueta4=Label(pestanha2,text="Intensidad del color",font=("arial",12),bg=('white')).place(x=140,y=40)
        etiqueta5=Label(pestanha2,text="Temperatura",font=("arial",15),bg=('white')).place(x=10,y=165)
        etiqueta6 = Label(pestanha2, text="Ref:",font=("arial",12),bg=('white')).place(x=10,y=195)
        self.temperatura2=DoubleVar()
        escala_ref_temperatura2=Scale(pestanha2,variable=self.temperatura2,
                                                 from_ = 1, to = 92, orient = HORIZONTAL,length=216,bg=('#BDBDBD')).place(x=80,y=195)
        entrada2 = ttk.Entry(pestanha2, width=30, textvariable=self.temperatura2,font=("arial",10)).place(x=80,y=235)
        etiqueta5=Label(pestanha2,text="Nivel",font=("arial",15),bg=('white')).place(x=10,y=265)
        etiqueta6 = Label(pestanha2, text="Ref:",font=("arial",12),bg=('white')).place(x=10,y=295)
        self.nivel2=DoubleVar()
        escala_ref_nivel2=Scale(pestanha2,variable=self.nivel2,
                                                 from_ = 1, to = 25, orient = HORIZONTAL,length=216,bg=('#BDBDBD')).place(x=80,y=295)
        entrada3 = ttk.Entry(pestanha2, width=30, textvariable=self.nivel2,font=("arial",10)).place(x=80,y=335)
        boton1=Button(pestanha2,text="Iniciar",command=self.accion_boton2,width=30).place(x=80,y=365)
        boton2=Button(pestanha2,text="Detener",command=self.accion_boton5,width=30).place(x=80,y=400)

#######################################################################################################################
### FOTOBIORREACTOR 3##################################################################################################
#######################################################################################################################   
        etiqueta2=Label(pestanha3,text="Luz",font=("arial",15),bg=('white')).place(x=10,y=10)
        etiqueta3=Label(pestanha3,text="Color",font=("arial",14),bg=('white')).place(x=10,y=40)
        rcolor3=IntVar()
        R1 = Radiobutton(pestanha3, text="Rojo",
                                      variable=rcolor3, value=1,command=self.color_rojo3,font=("arial",10),bg=('white')).place(x=10,y=70)
        R2 = Radiobutton(pestanha3, text="Verde",
                                        variable=rcolor3, value=2, command=self.color_verde3,font=("arial",10),bg=('white')).place(x=10,y=90)
        R3 = Radiobutton(pestanha3, text="Azul",
                                        variable=rcolor3, value=3, command=self.color_azul3,font=("arial",10),bg=('white')).place(x=10,y=110)
        R4 = Radiobutton(pestanha3, text="Blanco",
                         variable=rcolor1, value=3, command=self.color_rojo3,font=("arial",10),bg=('white')).place(x=10,y=130)
        self.luz3=DoubleVar()
        escala_intensidad_luz=Scale(pestanha3,variable=self.luz3,
                                                 from_ = 1, to = 900, orient = HORIZONTAL,length=216,bg=('#BDBDBD')).place(x=80,y=70)
        entrada1 = ttk.Entry(pestanha3, width=30, textvariable=self.luz3,font=("arial",10)).place(x=80,y=110)
        etiqueta4=Label(pestanha3,text="Intensidad del color",font=("arial",12),bg=('white')).place(x=140,y=40)
        etiqueta5=Label(pestanha3,text="Temperatura",font=("arial",15),bg=('white')).place(x=10,y=165)
        etiqueta6 = Label(pestanha3, text="Ref:",font=("arial",12),bg=('white')).place(x=10,y=195)
        self.temperatura3=DoubleVar()
        escala_ref_temperatura3=Scale(pestanha3,variable=self.temperatura3,
                                                 from_ = 1, to = 92, orient = HORIZONTAL,length=216,bg=('#BDBDBD')).place(x=80,y=195)
        entrada2 = ttk.Entry(pestanha3, width=30, textvariable=self.temperatura3,font=("arial",10)).place(x=80,y=235)
        etiqueta5=Label(pestanha3,text="Nivel",font=("arial",15),bg=('white')).place(x=10,y=265)
        etiqueta6 = Label(pestanha3, text="Ref:",font=("arial",12),bg=('white')).place(x=10,y=295)
        self.nivel3=DoubleVar()
        escala_ref_nivel3=Scale(pestanha3,variable=self.nivel3,
                                                 from_ = 1, to = 25, orient = HORIZONTAL,length=216,bg=('#BDBDBD')).place(x=80,y=295)
        entrada3 = ttk.Entry(pestanha3, width=30, textvariable=self.nivel3,font=("arial",10)).place(x=80,y=335)
        boton1=Button(pestanha3,text="Iniciar",command=self.accion_boton3,width=30).place(x=80,y=365)
        boton2=Button(pestanha3,text="Detener",command=self.accion_boton6,width=30).place(x=80,y=400)
#FIGURA TEMPERATURA1
        figure = plt.Figure(figsize=(5,6), dpi=100)
        self.ax = figure.add_subplot(111)
        self.ax.grid(True),self.ax.set_xlabel('$x$'),self.ax.set_ylabel('$y(x)$')
        self.line = FigureCanvasTkAgg(figure, pestanha4)
        self.line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA TEMPERATURA2
        figure = plt.Figure(figsize=(5,6), dpi=100)
        self.ax_2 = figure.add_subplot(111)
        self.ax_2.grid(True),self.ax_2.set_xlabel('$x$'),self.ax_2.set_ylabel('$y(x)$')
        self.line_2 = FigureCanvasTkAgg(figure, pestanha10)
        self.line_2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA TEMPERATURA3
        figure = plt.Figure(figsize=(5,6), dpi=100)
        self.ax_3 = figure.add_subplot(111)
        self.ax_3.grid(True),self.ax_3.set_xlabel('$x$'),self.ax_3.set_ylabel('$y(x)$')
        self.line_3 = FigureCanvasTkAgg(figure, pestanha16)
        self.line_3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA LUZ1
        figure1 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax1 = figure1.add_subplot(111)
        self.ax1.grid(True),self.ax1.set_xlabel('$x$'),self.ax1.set_ylabel('$y(x)$')
        self.line1 = FigureCanvasTkAgg(figure1, pestanha5)
        self.line1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA LUZ2
        figure1 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax1_2 = figure1.add_subplot(111)
        self.ax1_2.grid(True),self.ax1_2.set_xlabel('$x$'),self.ax1_2.set_ylabel('$y(x)$')
        self.line1_2 = FigureCanvasTkAgg(figure1, pestanha11)
        self.line1_2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA LUZ3
        figure1 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax1_3 = figure1.add_subplot(111)
        self.ax1_3.grid(True),self.ax1_3.set_xlabel('$x$'),self.ax1_3.set_ylabel('$y(x)$')
        self.line1_3 = FigureCanvasTkAgg(figure1, pestanha17)
        self.line1_3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA NIVEL1
        figure2 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax2 = figure2.add_subplot(111)
        self.ax2.grid(True),self.ax2.set_xlabel('$x$'),self.ax2.set_ylabel('$y(x)$')
        self.line2 = FigureCanvasTkAgg(figure2, pestanha6)
        self.line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA NIVEL2
        figure2 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax2_2 = figure2.add_subplot(111)
        self.ax2_2.grid(True),self.ax2_2.set_xlabel('$x$'),self.ax2_2.set_ylabel('$y(x)$')
        self.line2_2 = FigureCanvasTkAgg(figure2, pestanha12)
        self.line2_2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA NIVEL3
        figure2 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax2_3 = figure2.add_subplot(111)
        self.ax2_3.grid(True),self.ax2_3.set_xlabel('$x$'),self.ax2_3.set_ylabel('$y(x)$')
        self.line2_3 = FigureCanvasTkAgg(figure2, pestanha18)
        self.line2_3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA pH1
        figure3 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax3 = figure3.add_subplot(111)
        self.ax3.grid(True),self.ax3.set_xlabel('$x$'),self.ax3.set_ylabel('$y(x)$')
        self.line3 = FigureCanvasTkAgg(figure3, pestanha7)
        self.line3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA pH2
        figure3 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax3_2 = figure3.add_subplot(111)
        self.ax3_2.grid(True),self.ax3_2.set_xlabel('$x$'),self.ax3_2.set_ylabel('$y(x)$')
        self.line3_2 = FigureCanvasTkAgg(figure3, pestanha13)
        self.line3_2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA pH3
        figure3 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax3_3 = figure3.add_subplot(111)
        self.ax3_3.grid(True),self.ax3_3.set_xlabel('$x$'),self.ax3_3.set_ylabel('$y(x)$')
        self.line3_3 = FigureCanvasTkAgg(figure3, pestanha19)
        self.line3_3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA DO1
        figure4 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax4 = figure4.add_subplot(111)
        self.ax4.grid(True),self.ax4.set_xlabel('$x$'),self.ax4.set_ylabel('$y(x)$')
        self.line4 = FigureCanvasTkAgg(figure4, pestanha8)
        self.line4.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA DO2
        figure4 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax4_2 = figure4.add_subplot(111)
        self.ax4_2.grid(True),self.ax4_2.set_xlabel('$x$'),self.ax4_2.set_ylabel('$y(x)$')
        self.line4_2 = FigureCanvasTkAgg(figure4, pestanha14)
        self.line4_2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA DO3
        figure4 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax4_3 = figure4.add_subplot(111)
        self.ax4_3.grid(True),self.ax4_3.set_xlabel('$x$'),self.ax4_3.set_ylabel('$y(x)$')
        self.line4_3 = FigureCanvasTkAgg(figure4, pestanha20)
        self.line4_3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA BIOMASA1
##            figure5 = plt.Figure(figsize=(5,6), dpi=100)
##            self.ax5 = figure5.add_subplot(111)
##            self.ax5.grid(True),self.ax5.set_xlabel('$x$'),self.ax5.set_ylabel('$y(x)$')
##            self.line5 = FigureCanvasTkAgg(figure5, pestanha9)
##            self.line5.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA BIOMASA2
##            figure5 = plt.Figure(figsize=(5,6), dpi=100)
##            self.ax5_2 = figure5.add_subplot(111)
##            self.ax5_2.grid(True),self.ax5_2.set_xlabel('$x$'),self.ax5_2.set_ylabel('$y(x)$')
##            self.line5_2 = FigureCanvasTkAgg(figure5, pestanha15)
##            self.line5_2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA BIOMASA3
##            figure5 = plt.Figure(figsize=(5,6), dpi=100)
##            self.ax5_3 = figure5.add_subplot(111)
##            self.ax5_3.grid(True),self.ax5_3.set_xlabel('$x$'),self.ax5_3.set_ylabel('$y(x)$')
##            self.line5_3 = FigureCanvasTkAgg(figure5, pestanha21)
##            self.line5_3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)


        ventana.mainloop()
#CREACIÓN DE UNA VENTANA APARTE PARA LOS CRÉDITOS Y AGRADECIMIENTOS
    def f_acerca(self):
        acerca = Toplevel()
        acerca.geometry("700x720")
        acerca.bg=('red')
        acerca.resizable(width=False, height=False)
        acerca.title("Agradecimientos a:")
        marco1 = ttk.Frame(acerca,padding=(10, 10, 10, 10),relief=RAISED)
        marco1.pack(side=TOP, fill=BOTH, expand=True)
        self.fondo=PhotoImage(file="logo.png")
        self.labelfondo=Label(marco1,image=self.fondo).place(x=0,y=30)
        boton1 = Button(marco1, text="Salir",command=acerca.destroy)
        boton1.pack(side=TOP, padx=10, pady=0)
        boton1.focus_set()
    
    # Información Adicional        
    def f_about(self):
        about = Toplevel()
        about.geometry("900x720")
        about.bg=('red')
        about.resizable(width=False, height=False)
        about.title("This software was developed by:")
        marco1 = ttk.Frame(about,padding=(10, 10, 10, 10),relief=RAISED)
        marco1.pack(side=TOP, fill=BOTH, expand=True)
        self.fondo=PhotoImage(file="logo_II.png")
        self.labelfondo=Label(marco1,image=self.fondo).place(x=0,y=30)
        boton1 = Button(marco1, text="Salir",command=about.destroy)
        boton1.pack(side=TOP, padx=10, pady=0)
        boton1.focus_set()
        
#ACTIVACIÓN COLORES
    #CADA COLOR SE ACTIVA MEDIANTE PINES DIGITALES INDEPENDIENTES EN LA LabJack
    #DEPENDIENDO DEL ESTADO DE LOS RADIOBUTTON R1,R2 Y R3 PARA CADA FOTOBIORREACTOR
#1
    def color_rojo1(self): #ASOCIAR AL RADIOBUTTON R1
        respuesta_pin_rojo1=True 
        tarjeta1.sendValue('EIO0', True)
        tarjeta1.sendValue('EIO1', False)
        tarjeta1.sendValue('EIO2', False)        
    def color_verde1(self): ##ASOCIAR AL RADIOBUTTON R2
        respuesta_pin_verde1=True
        tarjeta1.sendValue('EIO0', False)
        tarjeta1.sendValue('EIO1', True)
        tarjeta1.sendValue('EIO2', False)        
    def color_azul1(self): ##ASOCIAR AL RADIOBUTTON R3
        respuesta_pin_azul1=True
        tarjeta1.sendValue('EIO0', False)
        tarjeta1.sendValue('EIO1', False)
        tarjeta1.sendValue('EIO2', True)

#2
    def color_rojo2(self):
        respuesta_pin_rojo2=True
        tarjeta1.sendValue('EIO3', True)
        tarjeta1.sendValue('EIO4', False)
        tarjeta1.sendValue('EIO5', False)
        
    def color_verde2(self):
        respuesta_pin_verde2=True
        tarjeta1.sendValue('EIO3', False)
        tarjeta1.sendValue('EIO4', True)
        tarjeta1.sendValue('EIO5', False)
        
    def color_azul2(self):
        respuesta_pin_azul2=True
        tarjeta1.sendValue('EIO3', False)
        tarjeta1.sendValue('EIO4', False)
        tarjeta1.sendValue('EIO5', True)
#3
    def color_rojo3(self):
        respuesta_pin_rojo3=True
        tarjeta1.sendValue('EIO6', True)
        tarjeta1.sendValue('EIO7', False)
        tarjeta1.sendValue('CIO0', False)
        
    def color_verde3(self):
        respuesta_pin_verde3=True
        tarjeta1.sendValue('EIO6', False)
        tarjeta1.sendValue('EIO7', True)
        tarjeta1.sendValue('CIO0', False)
        
    def color_azul3(self):
        respuesta_pin_azul3=True
        tarjeta1.sendValue('EIO6', False)
        tarjeta1.sendValue('EIO7', False)
        tarjeta1.sendValue('CIO0', True)

#MÉTODO FBR1        
    def fbr1(self):
        while True:
    #LUZ 1
            self.referencia_luz1=float(self.luz1.get()) #ASOCIAR AL WIDGET escala_intensidad_luz Y A LA entrada1 SE CREA LA REFERENCIA DEL CONTROLADOR
            self.valor_luz1 = tarjeta1.readValue('AIN3') #LEER ENTRADA ANÁLOGA AIN3
            self.luz_real1 = (100000 * round(self.valor_luz1,3)) #CALIBRACIÓN Y AJUSTE DEL SENSOR
            self.error_luz1 = self.referencia_luz1 - self.luz_real1 #SE GENERA EL ERROR
            self.integral_luz1 = self.integral_anterior_luz1 + self.error_luz1 * 5 #PARTE INTEGRAL DEL CONTROLADOR
            self.derivativo_luz1 = (self.error_luz1 - self.error_anterior_luz1) / 5 #PARTE DERIVATIVA DEL CONTROLADOR
            self.salida_luz1 = (self.kp_luz1 * self.error_luz1 + self.ki_luz1 * self.integral_luz1 +
                                self.kd_luz1 * self.derivativo_luz1 + self.bias_luz1) / 5 #SALIDA DEL CONTROLADOR HASTA ESTA LINEA PUEDE TOMAR VALORES MAYORES A 100
            self.error_prior_luz1 = self.error_luz1 #ERROR ANTERIOR, DEFINIDO=0 EN EL MÉTODO INIT
            self.integral_prior_luz1 = self.integral_luz1 #INTEGRAL ANTERIOR
            self.ax1.set_xlabel('$x$'),self.ax1.set_ylabel('$y(x)$') 
            self.ax1.clear()
            self.ax1.plot(self.x1,self.y1), self.ax1.grid(True) #CUADRICULA EN EL GRÁFICO
            self.x1.append(datetime.now()) #SE CREA UNA LISTA CON EL FORMATO DE TIEMPO REAL
            self.y1.append(self.luz_real1) #SE CREA UNA LISTA CON LOS VALORES DEL SENSOR
            self.line1.draw()
            if self.salida_luz1 >= 100: #EN ESTE CONDICIONAL SE ACOTAN LOS VALORES EN 0-100
                self.salida_luz1 = 100
            if self.salida_luz1 <= 0:
                self.salida_luz1 = 0
            tarjeta1.sendValue('TDAC3', interp(self.salida_luz1, [0, 100], [0, 5])) #SE INTERPOLA LA SALIDA DEL CONTROLADOR CON EL RANGO DEL ACTUADOR
            time.sleep(1) #RETARDO DE 1 SEGUNDO
    #TEMPERATURA 1
            referencia_temperatura1 = float(self.temperatura1.get()) #ASOCIAR AL WIDGET escala_ref_temperatura1 Y A LA entrada2 SE CREA LA REFERENCIA DEL CONTROLADOR
            valor_temp1 = tarjeta1.readValue('AIN0') #LECTURA DEL CANAL ANÁLOGO DIGITAL CORRESPONDIENTE AL TERMOPAR 1
            temperatura_real1 = (55.56 * valor_temp1) + 255.37 - 273.15 #CALIBRACIÓN Y AJUSTE DEL TERMOPAR
            self.error_temp1=referencia_temperatura1-temperatura_real1 #ERROR
            self.integral_temp1=self.integral_anterior_temp1+self.error_temp1*5 #PARTE INTEGRAL
            self.derivativo_temp1=(self.error_temp1-self.error_anterior_temp1)/5 #PARTE DERIVATIVA
            self.salida_temp1=(self.kp_temp1*self.error_temp1+self.ki_temp1*self.integral_temp1+self.kd_temp1*self.derivativo_temp1+self.bias_temp1)/5 #SALIDA
            self.error_anterior1=self.error_temp1 #ERROR ANTERIOR=0 EN LA PRIMERA ITERACIÓN (VER MÉTODO INIT)
            self.integral_anterior1=self.integral_temp1 #INTEGRAL ANTERIOR
            self.ax.set_xlabel('$x$'),self.ax.set_ylabel('$y(x)$')
            self.ax.clear()
            self.ax.plot(self.x,self.y), self.ax.grid(True)
            self.x.append(datetime.now())
            self.y.append(temperatura_real1)
            self.line.draw()
            
    #-o-

            if self.salida_temp1>=100:
                self.salida_temp1=100
            if self.salida_temp1 <=0:
                self.salida_temp1=0
            tarjeta1.sendValue('DAC0', interp(self.salida_temp1, [0, 100], [0, 5])) #INTERPOLA LA SALIDA DEL CONTROLADOR CON LA POTENCIA DEL CALEFACTOR
            if temperatura_real1 > referencia_temperatura1: #VENTILADOR ACTIVACIÓN DIGITAL
                tarjeta1.sendValue('CIO1',5)
            else:
                tarjeta1.sendValue('CIO1',0)
    #NIVEL1
            self.referencia_nivel1 = float(self.nivel1.get())
            self.voltaje1 = float(tarjeta2.readValue('AIN0'))
            self.nivel_real1 = float(5.8953 * self.voltaje1 + 2.5354)
            self.ax2.set_xlabel('$x$'),self.ax2.set_ylabel('$y(x)$')
            self.ax2.clear()
            self.ax2.plot(self.x2,self.y2), self.ax2.grid(True)
            self.x2.append(datetime.now())
            self.y2.append(self.nivel_real1)
            self.line2.draw()
            if self.nivel_real1 < self.referencia_nivel1:
                tarjeta2.sendValue('DAC0', 5)  # RECOMENDACIÓN: Ajustar el accionamiento de las
                tarjeta2.sendValue('DAC1', 0)  # bombas a la menor resolución de llenado
            elif self.nivel_real1 > self.referencia_nivel1:  # posible ya que el proceso se puede desbocar.
                tarjeta2.sendValue('DAC0', 0)
                tarjeta2.sendValue('DAC1', 5)
            elif self.nivel_real1 == self.referencia_nivel1:
                tarjeta2.sendValue('DAC0', 0)
                tarjeta2.sendValue('DAC1', 0)
    #pH1
            comunicacion.initI2C(1, 0, 6) #EL OBJETO comunicación LLAMA AL MÉTODO initI2C (TX,RX,DIRECCIÓN)
            comunicacion.sendValueI2C([82]) #EL OBJETO comunicación LLAMA AL MÉTODO sendValueI2C ([COMANDO ASCII]) EN CASO DE NECESITAR OTRA UTILIDAD VER MANUAL DEL SENSOR
            time.sleep(0.9) #POR NADA DEL MUNDO SE PUEDE CAMBIAR ESTE RETARDO (VER MANUAL DEL SENSOR)
            self.pH1_real=comunicacion.readValueI2C() #LEER SENSOR
            self.ax3.set_xlabel('$x$'),self.ax3.set_ylabel('$y(x)$')
            self.ax3.clear()
            self.ax3.plot(self.x3,self.y3), self.ax3.grid(True)
            self.x3.append(datetime.now())
            self.y3.append(self.pH1_real)
            self.line3.draw()
    #DO1
            comunicacion.initI2C(1, 0, 3)
            comunicacion.sendValueI2C([82])#114
            time.sleep(0.6) #POR NADA DEL MUNDO SE PUEDE CAMBIAR ESTE RETARDO (VER MANUAL DEL SENSOR)
            self.DO_real1=comunicacion.readValueI2C()
            self.ax4.set_xlabel('$x$'),self.ax4.set_ylabel('$y(x)$')
            self.ax4.clear()
            self.ax4.plot(self.x4,self.y4), self.ax4.grid(True)
            self.x4.append(datetime.now())
            self.y4.append(self.DO_real1)
            self.line4.draw()
    #Biomasa1
##                comunicacion2.initUART(8,9)#tx,rx
##                self.biomasa1=comunicacion2.readValueUART()
##                print("Biomasa fbr1: ",self.biomasa1)
##                self.ax5.set_xlabel('$x$'),self.ax5.set_ylabel('$y(x)$')
##                self.ax5.clear()
##                self.ax5.plot(self.x5,self.y5), self.ax5.grid(True)
##                self.x5.append(datetime.now())
##                self.y5.append(self.biomasa1)
##                self.line5.draw()

#TABLA 1
            
            self.lista_temp1.append(temperatura_real1) #CREAR LISTA E INCORPORAR LOS DATOS DEL TERMOPAR
            frame_data1_1 = {'temperatura fbr1': self.lista_temp1} #TÍTULO DE LA COLUMNA : REGISTRO DE DATOS
            df = pandas.DataFrame(frame_data1_1) #ESCRIBIR TABLA
            df.to_excel("Temperatura_fbr1.xlsx", "Sheet1") #GUARDAR EN FORMÁTO DE EXCEL

            self.lista_luz1.append(luz_real1)
            frame_data1_2 = {'luz fbr1': self.lista_luz1}
            df = pandas.DataFrame(frame_data1_2)
            df.to_excel("Luz_fbr1.xlsx", "Sheet1")

            self.lista_nivel1.append(nivel_real1)
            frame_data1_3 = {'nivel fbr1': self.lista_nivel1}
            df = pandas.DataFrame(frame_data1_3)
            df.to_excel("Nivel_fbr1.xlsx", "Sheet1")

            self.lista_DO1.append(DO_real1)
            frame_data1_4 = {'DO fbr1': self.lista_DO1}
            df = pandas.DataFrame(frame_data1_4)
            df.to_excel("DO_fbr1.xlsx", "Sheet1")

            self.lista_pH1.append(pH_real1)
            frame_data1_5 = {'pH fbr1': self.lista_pH1}
            df = pandas.DataFrame(frame_data1_5)
            df.to_excel("pH_fbr1.xlsx", "Sheet1")


#MÉTODO FBR2
    def fbr2(self):
        while True:
            self.referencia_luz2=float(self.luz2.get())
            self.valor_luz2 = tarjeta1.readValue('AIN4')
            self.luz_real2 = (100000 * round(self.valor_luz2,3))
            self.error_luz2 = self.referencia_luz2 - self.luz_real2
            self.integral_luz2 = self.integral_anterior_luz2 + self.error_luz2 * 5
            self.derivativo_luz2 = (self.error_luz2 - self.error_anterior_luz2) / 5
            self.salida_luz2 = (self.kp_luz2 * self.error_luz2 + self.ki_luz2 * self.integral_luz2 + self.kd_luz2 * self.derivativo_luz2 + self.bias_luz2) / 5
            self.error_prior_luz2 = self.error_luz2
            self.integral_prior_luz2 = self.integral_luz2
            self.ax1_2.set_xlabel('$x$'),self.ax1_2.set_ylabel('$y(x)$')
            self.ax1_2.clear()
            self.ax1_2.plot(self.x1_2,self.y1_2), self.ax1_2.grid(True)
            self.x1_2.append(datetime.now())
            self.y1_2.append(self.luz_real2)
            self.line1_2.draw()
            if self.salida_luz2 >= 100:
                self.salida_luz2 = 100
            if self.salida_luz2 <= 0:
                self.salida_luz2 = 0
            tarjeta1.sendValue('TDAC4', interp(self.salida_luz2, [0, 100], [0, 5]))
    #TEMPERATURA2
            referencia_temperatura2 = float(self.temperatura2.get())
            valor_temp2 = tarjeta1.readValue('AIN1')
            temperatura_real2 = (55.56 * valor_temp2) + 255.37 - 273.15
            self.error_temp2=referencia_temperatura2-temperatura_real2
            self.integral_temp2=self.integral_anterior_temp2+self.error_temp2*5
            self.derivativo_temp2=(self.error_temp2-self.error_anterior_temp2)/5
            self.salida_temp2=(self.kp_temp2*self.error_temp2+self.ki_temp2*self.integral_temp2+self.kd_temp2*self.derivativo_temp2+self.bias_temp2)/5
            self.error_anterior2=self.error_temp2
            self.integral_anterior2=self.integral_temp2
            self.ax_2.set_xlabel('$x$'),self.ax_2.set_ylabel('$y(x)$')
            self.ax_2.clear()
            self.ax_2.plot(self.x_2,self.y_2), self.ax_2.grid(True)
            self.x_2.append(datetime.now())
            self.y_2.append(temperatura_real2)
            self.line_2.draw()


            if self.salida_temp2>=100:
                self.salida_temp2=100
            if self.salida_temp2 <=0:
                self.salida_temp2=0
            tarjeta1.sendValue('DAC1', interp(self.salida_temp2, [0, 100], [0, 5])) #CALEFACTOR 2
            if temperatura_real2 > referencia_temperatura2: #VENTILADOR 2
                tarjeta1.sendValue('CIO2',5)
            else:
                tarjeta1.sendValue('CIO2',0)
    #NIVEL2
            self.referencia_nivel2 = float(self.nivel2.get())
            self.voltaje2 = float(tarjeta2.readValue('AIN1'))
            self.nivel_real2 = float(5.8953 * self.voltaje2 + 2.5354)
            self.ax2_2.set_xlabel('$x$'),self.ax2_2.set_ylabel('$y(x)$')
            self.ax2_2.clear()
            self.ax2_2.plot(self.x2_2,self.y2_2), self.ax2_2.grid(True)
            self.x2_2.append(datetime.now())
            self.y2_2.append(self.nivel_real2)
            self.line2_2.draw()
            #if self.nivel_real2 < self.referencia_nivel2:
                #tarjeta2.sendValue('TDAC0', 5)  
                #tarjeta2.sendValue('TDAC1', 0)  
            #elif self.nivel_real2 > self.referencia_nivel2:  
                #tarjeta2.sendValue('TDAC0', 0)
                #tarjeta2.sendValue('TDAC1', 5)
            #elif self.nivel_real2 == self.referencia_nivel2:
                #tarjeta2.sendValue('TDAC0', 0)
                #tarjeta2.sendValue('TDAC1', 0)
    #pH2
            comunicacion.initI2C(1, 0, 5)
            comunicacion.sendValueI2C([82])
            time.sleep(0.9)
            self.pH2_real=comunicacion.readValueI2C()
            self.ax3_2.set_xlabel('$x$'),self.ax3_2.set_ylabel('$y(x)$')
            self.ax3_2.clear()
            self.ax3_2.plot(self.x3_2,self.y3_2), self.ax3_2.grid(True)
            self.x3_2.append(datetime.now())
            self.y3_2.append(self.pH2_real)
            self.line3_2.draw()
    #DO2
            comunicacion.initI2C(1, 0, 2)
            comunicacion.sendValueI2C([82])#114
            time.sleep(0.6)
            self.DO_real2=comunicacion.readValueI2C()
            self.ax4_2.set_xlabel('$x$'),self.ax4_2.set_ylabel('$y(x)$')
            self.ax4_2.clear()
            self.ax4_2.plot(self.x4_2,self.y4_2), self.ax4_2.grid(True)
            self.x4_2.append(datetime.now())
            self.y4_2.append(self.DO_real2)
            self.line4_2.draw()
    #Biomasa2
##                comunicacion2.initUART(10,11)
##                self.biomasa2=comunicacion2.readValueUART()
##                print("Biomasa fbr2: ",self.biomasa2)
##                self.ax5_2.set_xlabel('$x$'),self.ax5_2.set_ylabel('$y(x)$')
##                self.ax5_2.clear()
##                self.ax5_2.plot(self.x5_2,self.y5_2), self.ax5_2.grid(True)
##                self.x5_2.append(datetime.now())
##                self.y5_2.append(self.biomasa2)
##                self.line5_2.draw()
            self.lista_temp2.append(temperatura_real2)
            frame_data2_1 = {'temperatura fbr2': self.lista_temp2}
            df = pandas.DataFrame(frame_data2_1)
            df.to_excel("Temperatura_fbr2.xlsx", "Sheet1")

            self.lista_luz2.append(luz_real2)
            frame_data2_2 = {'luz fbr1': self.lista_luz2}
            df = pandas.DataFrame(frame_data2_2)
            df.to_excel("Luz_fbr2.xlsx", "Sheet1")

            self.lista_nivel2.append(nivel_real2)
            frame_data2_3 = {'nivel fbr2': self.lista_nivel2}
            df = pandas.DataFrame(frame_data2_3)
            df.to_excel("Nivel_fbr2.xlsx", "Sheet1")

            self.lista_DO2.append(DO_real2)
            frame_data2_4 = {'DO fbr2': self.lista_DO2}
            df = pandas.DataFrame(frame_data2_4)
            df.to_excel("DO_fbr2.xlsx", "Sheet1")

            self.lista_pH2.append(pH_real2)
            frame_data2_5 = {'pH fbr2': self.lista_pH2}
            df = pandas.DataFrame(frame_data2_5)
            df.to_excel("pH_fbr2.xlsx", "Sheet1")
            

#MÉTODO FBR3
    def fbr3(self):
        while True:
            self.referencia_luz3=float(self.luz3.get())
            self.valor_luz3 = tarjeta1.readValue('AIN5')
            self.luz_real3 = (100000 * round(self.valor_luz3,3))
            self.error_luz3 = self.referencia_luz3 - self.luz_real3
            self.integral_luz3 = self.integral_anterior_luz3 + self.error_luz3 * 5
            self.derivativo_luz3 = (self.error_luz3 - self.error_anterior_luz3) / 5
            self.salida_luz3 = (self.kp_luz3 * self.error_luz3 + self.ki_luz3 * self.integral_luz3 + self.kd_luz3 * self.derivativo_luz3 + self.bias_luz3) / 5
            self.error_prior_luz3 = self.error_luz3
            self.integral_prior_luz3 = self.integral_luz3
            self.ax1_3.set_xlabel('$x$'),self.ax1_3.set_ylabel('$y(x)$')
            self.ax1_3.clear()
            self.ax1_3.plot(self.x1_3,self.y1_3), self.ax1_3.grid(True)
            self.x1_3.append(datetime.now())
            self.y1_3.append(self.luz_real3)
            self.line1_3.draw()
            if self.salida_luz3 >= 100:
                self.salida_luz3 = 100
            if self.salida_luz3 <= 0:
                self.salida_luz3 = 0
            tarjeta1.sendValue('TDAC5', interp(self.salida_luz3, [0, 100], [0, 5]))
    #TEMPERATURA3
            referencia_temperatura3 = float(self.temperatura3.get())
            valor_temp3 = tarjeta1.readValue('AIN6')
            temperatura_real3 = (55.56 * valor_temp3) + 255.37 - 273.15
            self.error_temp3=referencia_temperatura3-temperatura_real3
            self.integral_temp3=self.integral_anterior_temp3+self.error_temp3*5
            self.derivativo_temp3=(self.error_temp3-self.error_anterior_temp3)/5
            self.salida_temp3=(self.kp_temp3*self.error_temp3+self.ki_temp3*self.integral_temp3+self.kd_temp3*self.derivativo_temp3+self.bias_temp3)/5
            self.error_anterior3=self.error_temp3
            self.integral_anterior3=self.integral_temp3
            self.ax_3.set_xlabel('$x$'),self.ax_3.set_ylabel('$y(x)$')
            self.ax_3.clear()
            self.ax_3.plot(self.x_3,self.y_3), self.ax_3.grid(True)
            self.x_3.append(datetime.now())
            self.y_3.append(temperatura_real3)
            self.line_3.draw()


            if self.salida_temp3>=100:
                self.salida_temp3=100
            if self.salida_temp3 <=0:
                self.salida_temp3=0
            tarjeta1.sendValue('TDAC2', interp(self.salida_temp3, [0, 100], [0, 5])) #CALEFACTOR 3
            if temperatura_real3 > referencia_temperatura3: #VENTILADOR 3
                tarjeta1.sendValue('CIO3',5)
            else:
                tarjeta1.sendValue('CIO3',0)
    #NIVEL3
            self.referencia_nivel3 = float(self.nivel3.get())
            self.voltaje3 = float(tarjeta2.readValue('AIN2'))
            self.nivel_real3 = float(5.8953 * self.voltaje3 + 2.5354)
            self.ax2_3.set_xlabel('$x$'),self.ax2_3.set_ylabel('$y(x)$')
            self.ax2_3.clear()
            self.ax2_3.plot(self.x2_3,self.y2_3), self.ax2_3.grid(True)
            self.x2_3.append(datetime.now())
            self.y2_3.append(self.nivel_real3)
            self.line2_3.draw()
            if self.nivel_real3 < self.referencia_nivel3:
                tarjeta2.sendValue('TDAC2', 5)  
                tarjeta2.sendValue('TDAC3', 0)  
            elif self.nivel_real3 > self.referencia_nivel3:  
                tarjeta2.sendValue('TDAC2', 0)
                tarjeta2.sendValue('TDAC3', 5)
            elif self.nivel_real3 == self.referencia_nivel3:
                tarjeta2.sendValue('TDAC2', 0)
                tarjeta2.sendValue('TDAC3', 0)
    #pH3
            comunicacion.initI2C(1, 0, 4)
            comunicacion.sendValueI2C([82])
            time.sleep(0.9)
            self.pH3_real=comunicacion.readValueI2C()
            self.ax3_3.set_xlabel('$x$'),self.ax3_3.set_ylabel('$y(x)$')
            self.ax3_3.clear()
            self.ax3_3.plot(self.x3_3,self.y3_3), self.ax3_3.grid(True)
            self.x3_3.append(datetime.now())
            self.y3_3.append(self.pH3_real)
            self.line3_3.draw()
    #DO3
            comunicacion.initI2C(1, 0, 1)
            comunicacion.sendValueI2C([82])#114
            time.sleep(0.6)
            self.DO_real3=comunicacion.readValueI2C()
            self.ax4_3.set_xlabel('$x$'),self.ax4_3.set_ylabel('$y(x)$')
            self.ax4_3.clear()
            self.ax4_3.plot(self.x4_3,self.y4_3), self.ax4_3.grid(True)
            self.x4_3.append(datetime.now())
            self.y4_3.append(self.DO_real3)
            self.line4_3.draw()
    #Biomasa3
##                comunicacion2.initUART(12,13)
##                self.biomasa3=comunicacion2.readValueUART()
##                print("Biomasa fbr3: ",self.biomasa3)
##                self.ax5_3.set_xlabel('$x$'),self.ax5_3.set_ylabel('$y(x)$')
##                self.ax5_3.clear()
##                self.ax5_3.plot(self.x5_3,self.y5_3), self.ax5_3.grid(True)
##                self.x5_3.append(datetime.now())
##                self.y5_3.append(self.biomasa3)
##                self.line5_3.draw()
            
            self.lista_temp3.append(temperatura_real3)
            frame_data3 = {'temperatura fbr3': self.lista_temp3}
            df = pandas.DataFrame(frame_data3)
            df.to_excel("Temperatura_fbr3.xlsx", "Sheet1")

            self.lista_luz3.append(luz_real3)
            frame_data3_2 = {'luz fbr3': self.lista_luz3}
            df = pandas.DataFrame(frame_data3_2)
            df.to_excel("Luz_fbr3.xlsx", "Sheet1")

            self.lista_nivel3.append(nivel_real3)
            frame_data3_3 = {'nivel fbr3': self.lista_nivel3}
            df = pandas.DataFrame(frame_data3_3)
            df.to_excel("Nivel_fbr3.xlsx", "Sheet1")

            self.lista_DO3.append(DO_real3)
            frame_data3_4 = {'DO fbr3': self.lista_DO3}
            df = pandas.DataFrame(frame_data3_4)
            df.to_excel("DO_fbr3.xlsx", "Sheet1")

            self.lista_pH3.append(pH_real3)
            frame_data3_5 = {'pH fbr3': self.lista_pH3}
            df = pandas.DataFrame(frame_data3_5)
            df.to_excel("pH_fbr3.xlsx", "Sheet1")
            
    def reset1(self):
        while True:
            tarjeta1.sendValue('EIO0', False)
            tarjeta1.sendValue('EIO1', False)
            tarjeta1.sendValue('EIO2', False)        

            tarjeta1.sendValue('TDAC3',0)
            tarjeta1.sendValue('DAC0',0)
            tarjeta1.sendValue('CIO1',0)

            tarjeta2.sendValue('DAC0', 0)
            tarjeta2.sendValue('DAC1', 0)

    def reset2(self):
        while True:
            tarjeta1.sendValue('EIO3', False)
            tarjeta1.sendValue('EIO4', False)
            tarjeta1.sendValue('EIO5', False)

            tarjeta1.sendValue('TDAC4',0)
            tarjeta1.sendValue('DAC1',0)
            tarjeta1.sendValue('CIO2',0)

            tarjeta2.sendValue('TDAC0', 0)
            tarjeta2.sendValue('TDAC1', 0)

    def reset3(self):
        while True:
            tarjeta1.sendValue('EIO6', False)
            tarjeta1.sendValue('EIO7', False)
            tarjeta1.sendValue('CIO0', False)

            tarjeta1.sendValue('TDAC5',0)
            tarjeta1.sendValue('TDAC2',0)
            tarjeta1.sendValue('CIO3',0)

            tarjeta2.sendValue('TDAC2', 0)
            tarjeta2.sendValue('TDAC3', 0)

        


#DESANCLAR BOTON
    def accion_boton(self):
        Thread(target=self.fbr1).start()
    def accion_boton2(self):
        Thread(target=self.fbr2).start()
    def accion_boton3(self):
        Thread(target=self.fbr3).start()
    def accion_boton4(self):
        Thread(target=self.reset1).start()
    def accion_boton5(self):
        Thread(target=self.reset2).start()
    def accion_boton6(self):
        Thread(target=self.reset3).start()

objeto=Principal()

