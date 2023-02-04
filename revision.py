import tkinter as tk
from tkinter import *
from tkinter import ttk
import time
import numpy as np
from numpy import interp
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from drawnow import *
import atexit
from collections import deque
from datetime import datetime
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot
from random import randrange
import multiprocessing
from threading import Thread
import pandas
import openpyxl
from ljm1 import Ljm
from ljm2 import Ljm2



tarjeta1=Ljm()
tarjeta2 = Ljm2()
comunicacion = Ljm()
comunicacion2 = Ljm2()

        
class Principal():
    def __init__(self):
        ventana=Tk()
        notebook=ttk.Notebook(ventana)
        notebook.pack(fill='both',expand='yes')
        pestaña1=tk.Frame(notebook,bg='white')
        pestaña2=tk.Frame(notebook,bg='white')
        pestaña3=tk.Frame(notebook,bg='white')
        notebook.add(pestaña1,text='FBR1')
        notebook.add(pestaña2,text='FBR2')
        notebook.add(pestaña3,text='FBR3')
#1
        right_frame = tk.Frame(pestaña1, bg='#C0C0C0', bd=1.5)
        right_frame.place(relx=0.3, rely=0.055, relwidth=0.65, relheight=0.8)
        notebook1=ttk.Notebook(right_frame)
        notebook1.pack(fill='both',expand='yes')
        pestaña4=ttk.Frame(notebook1)
        pestaña5=ttk.Frame(notebook1)
        pestaña6=ttk.Frame(notebook1)
        pestaña7=ttk.Frame(notebook1)
        pestaña8=ttk.Frame(notebook1)
        pestaña9=ttk.Frame(notebook1)
        notebook1.add(pestaña4,text=' Temperatura ')
        notebook1.add(pestaña5,text='     Luz     ')
        notebook1.add(pestaña6,text='  Nivel  ')       
        notebook1.add(pestaña7,text='  pH  ')
        notebook1.add(pestaña8,text='  OD  ')
        notebook1.add(pestaña9,text='  Biomasa  ')
#2
        right_frame2 = tk.Frame(pestaña2, bg='#C0C0C0', bd=1.5)
        right_frame2.place(relx=0.3, rely=0.055, relwidth=0.65, relheight=0.8)
        notebook2=ttk.Notebook(right_frame2)
        notebook2.pack(fill='both',expand='yes')
        pestaña10=ttk.Frame(notebook2)
        pestaña11=ttk.Frame(notebook2)
        pestaña12=ttk.Frame(notebook2)
        pestaña13=ttk.Frame(notebook2)
        pestaña14=ttk.Frame(notebook2)
        pestaña15=ttk.Frame(notebook2)
        notebook2.add(pestaña10,text=' Temperatura ')
        notebook2.add(pestaña11,text='     Luz     ')
        notebook2.add(pestaña12,text='  Nivel  ')       
        notebook2.add(pestaña13,text='  pH  ')
        notebook2.add(pestaña14,text='  OD  ')
        notebook2.add(pestaña15,text='  Biomasa  ')
#3
        right_frame3 = tk.Frame(pestaña3, bg='#C0C0C0', bd=1.5)
        right_frame3.place(relx=0.3, rely=0.055, relwidth=0.65, relheight=0.8)
        notebook3=ttk.Notebook(right_frame3)
        notebook3.pack(fill='both',expand='yes')
        pestaña16=ttk.Frame(notebook3)
        pestaña17=ttk.Frame(notebook3)
        pestaña18=ttk.Frame(notebook3)
        pestaña19=ttk.Frame(notebook3)
        pestaña20=ttk.Frame(notebook3)
        pestaña21=ttk.Frame(notebook3)
        notebook3.add(pestaña16,text=' Temperatura ')
        notebook3.add(pestaña17,text='     Luz     ')
        notebook3.add(pestaña18,text='  Nivel  ')       
        notebook3.add(pestaña19,text='  pH  ')
        notebook3.add(pestaña20,text='  OD  ')
        notebook3.add(pestaña21,text='  Biomasa  ')
        
        
#VENTANA GENERAL        
        ventana.title('Interfaz de control FotoBioReactores continuos')
        ventana.geometry('1100x720')
        ventana.configure(background='white')
        menubar = Menu(ventana)
        ventana.config(menu=menubar)
        menu_archivo = Menu(menubar)
        menu_archivo = Menu(menubar, tearoff=0)
        menu_archivo.add_command(label="Nuevo")
        menu_archivo.add_command(label="Abrir")
        menu_archivo.add_command(label="Guardar")
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=ventana.destroy)
        menu_edicion = Menu(menubar)
        menu_ayuda = Menu(menubar)
        menu_edicion = Menu(menubar, tearoff=0)
        menu_ayuda = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)
        menubar.add_cascade(label="Editar", menu=menu_edicion)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="Agradecimientos",command=self.f_acerca)

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
#######################################################################################################################
### FOTOBIORREACTOR 1##################################################################################################
#######################################################################################################################
        etiqueta2=Label(pestaña1,text="Luz",font=("arial",15),bg=('white')).place(x=10,y=10)
        etiqueta3=Label(pestaña1,text="Color",font=("arial",14),bg=('white')).place(x=10,y=40)
        rcolor1=IntVar()
        R1 = Radiobutton(pestaña1, text="Rojo",
                                      variable=rcolor1, value=1,command=self.color_rojo1,font=("arial",10),bg=('white')).place(x=10,y=70)
        R2 = Radiobutton(pestaña1, text="Verde",
                                        variable=rcolor1, value=2, command=self.color_verde1,font=("arial",10),bg=('white')).place(x=10,y=90)
        R3 = Radiobutton(pestaña1, text="Azul",
                                        variable=rcolor1, value=3, command=self.color_azul1,font=("arial",10),bg=('white')).place(x=10,y=110)
        R4 = Radiobutton(pestaña1, text="Blanco",
                         variable=rcolor1, value=3, command=self.color_rojo1,font=("arial",10),bg=('white')).place(x=10,y=130)
        self.luz1=DoubleVar()
        escala_intensidad_luz=Scale(pestaña1,variable=self.luz1,
                                                 from_ = 1, to = 900, orient = HORIZONTAL,length=216,bg=('#BDBDBD')).place(x=80,y=70)
        entrada1 = ttk.Entry(pestaña1, width=30, textvariable=self.luz1,font=("arial",10)).place(x=80,y=110)
        etiqueta4=Label(pestaña1,text="Intensidad del color",font=("arial",12),bg=('white')).place(x=140,y=40)
        etiqueta5=Label(pestaña1,text="Temperatura",font=("arial",15),bg=('white')).place(x=10,y=165)
        etiqueta6 = Label(pestaña1, text="Ref:",font=("arial",12),bg=('white')).place(x=10,y=195)
        self.temperatura1=DoubleVar()
        escala_ref_temperatura1=Scale(pestaña1,variable=self.temperatura1,
                                                 from_ = 1, to = 92, orient = HORIZONTAL,length=216,bg=('#BDBDBD')).place(x=80,y=195)
        entrada2 = ttk.Entry(pestaña1, width=30, textvariable=self.temperatura1,font=("arial",10)).place(x=80,y=235)
        etiqueta5=Label(pestaña1,text="Nivel",font=("arial",15),bg=('white')).place(x=10,y=265)
        etiqueta6 = Label(pestaña1, text="Ref:",font=("arial",12),bg=('white')).place(x=10,y=295)
        self.nivel1=DoubleVar()
        escala_ref_nivel1=Scale(pestaña1,variable=self.nivel1,
                                                 from_ = 1, to = 25, orient = HORIZONTAL,length=216,bg=('#BDBDBD')).place(x=80,y=295)
        entrada3 = ttk.Entry(pestaña1, width=30, textvariable=self.nivel1,font=("arial",10)).place(x=80,y=335)
        boton1=Button(pestaña1,text="Iniciar",command=self.accion_boton,width=30).place(x=80,y=365)
        boton2=Button(pestaña1,text="Detener",command=self.accion_boton4,width=30).place(x=80,y=400)

#######################################################################################################################
### FOTOBIORREACTOR 2##################################################################################################
#######################################################################################################################   
        etiqueta2=Label(pestaña2,text="Luz",font=("arial",15),bg=('white')).place(x=10,y=10)
        etiqueta3=Label(pestaña2,text="Color",font=("arial",14),bg=('white')).place(x=10,y=40)
        rcolor2=IntVar()
        R1 = Radiobutton(pestaña2, text="Rojo",
                                      variable=rcolor2, value=1,command=self.color_rojo2,font=("arial",10),bg=('white')).place(x=10,y=70)
        R2 = Radiobutton(pestaña2, text="Verde",
                                        variable=rcolor2, value=2, command=self.color_verde2,font=("arial",10),bg=('white')).place(x=10,y=90)
        R3 = Radiobutton(pestaña2, text="Azul",
                                        variable=rcolor2, value=3, command=self.color_azul2,font=("arial",10),bg=('white')).place(x=10,y=110)
        R4 = Radiobutton(pestaña2, text="Blanco",
                         variable=rcolor1, value=3, command=self.color_azul2,font=("arial",10),bg=('white')).place(x=10,y=130)
        self.luz2=DoubleVar()
        escala_intensidad_luz=Scale(pestaña2,variable=self.luz2,
                                                 from_ = 1, to = 900, orient = HORIZONTAL,length=216,bg=('#BDBDBD')).place(x=80,y=70)
        entrada1 = ttk.Entry(pestaña2, width=30, textvariable=self.luz2,font=("arial",10)).place(x=80,y=110)
        etiqueta4=Label(pestaña2,text="Intensidad del color",font=("arial",12),bg=('white')).place(x=140,y=40)
        etiqueta5=Label(pestaña2,text="Temperatura",font=("arial",15),bg=('white')).place(x=10,y=165)
        etiqueta6 = Label(pestaña2, text="Ref:",font=("arial",12),bg=('white')).place(x=10,y=195)
        self.temperatura2=DoubleVar()
        escala_ref_temperatura2=Scale(pestaña2,variable=self.temperatura2,
                                                 from_ = 1, to = 92, orient = HORIZONTAL,length=216,bg=('#BDBDBD')).place(x=80,y=195)
        entrada2 = ttk.Entry(pestaña2, width=30, textvariable=self.temperatura2,font=("arial",10)).place(x=80,y=235)
        etiqueta5=Label(pestaña2,text="Nivel",font=("arial",15),bg=('white')).place(x=10,y=265)
        etiqueta6 = Label(pestaña2, text="Ref:",font=("arial",12),bg=('white')).place(x=10,y=295)
        self.nivel2=DoubleVar()
        escala_ref_nivel2=Scale(pestaña2,variable=self.nivel2,
                                                 from_ = 1, to = 25, orient = HORIZONTAL,length=216,bg=('#BDBDBD')).place(x=80,y=295)
        entrada3 = ttk.Entry(pestaña2, width=30, textvariable=self.nivel2,font=("arial",10)).place(x=80,y=335)
        boton1=Button(pestaña2,text="Iniciar",command=self.accion_boton2,width=30).place(x=80,y=365)
        boton2=Button(pestaña2,text="Detener",command=self.accion_boton5,width=30).place(x=80,y=400)

#######################################################################################################################
### FOTOBIORREACTOR 3##################################################################################################
#######################################################################################################################   
        etiqueta2=Label(pestaña3,text="Luz",font=("arial",15),bg=('white')).place(x=10,y=10)
        etiqueta3=Label(pestaña3,text="Color",font=("arial",14),bg=('white')).place(x=10,y=40)
        rcolor3=IntVar()
        R1 = Radiobutton(pestaña3, text="Rojo",
                                      variable=rcolor3, value=1,command=self.color_rojo3,font=("arial",10),bg=('white')).place(x=10,y=70)
        R2 = Radiobutton(pestaña3, text="Verde",
                                        variable=rcolor3, value=2, command=self.color_verde3,font=("arial",10),bg=('white')).place(x=10,y=90)
        R3 = Radiobutton(pestaña3, text="Azul",
                                        variable=rcolor3, value=3, command=self.color_azul3,font=("arial",10),bg=('white')).place(x=10,y=110)
        R4 = Radiobutton(pestaña3, text="Blanco",
                         variable=rcolor1, value=3, command=self.color_rojo3,font=("arial",10),bg=('white')).place(x=10,y=130)
        self.luz3=DoubleVar()
        escala_intensidad_luz=Scale(pestaña3,variable=self.luz3,
                                                 from_ = 1, to = 900, orient = HORIZONTAL,length=216,bg=('#BDBDBD')).place(x=80,y=70)
        entrada1 = ttk.Entry(pestaña3, width=30, textvariable=self.luz3,font=("arial",10)).place(x=80,y=110)
        etiqueta4=Label(pestaña3,text="Intensidad del color",font=("arial",12),bg=('white')).place(x=140,y=40)
        etiqueta5=Label(pestaña3,text="Temperatura",font=("arial",15),bg=('white')).place(x=10,y=165)
        etiqueta6 = Label(pestaña3, text="Ref:",font=("arial",12),bg=('white')).place(x=10,y=195)
        self.temperatura3=DoubleVar()
        escala_ref_temperatura3=Scale(pestaña3,variable=self.temperatura3,
                                                 from_ = 1, to = 92, orient = HORIZONTAL,length=216,bg=('#BDBDBD')).place(x=80,y=195)
        entrada2 = ttk.Entry(pestaña3, width=30, textvariable=self.temperatura3,font=("arial",10)).place(x=80,y=235)
        etiqueta5=Label(pestaña3,text="Nivel",font=("arial",15),bg=('white')).place(x=10,y=265)
        etiqueta6 = Label(pestaña3, text="Ref:",font=("arial",12),bg=('white')).place(x=10,y=295)
        self.nivel3=DoubleVar()
        escala_ref_nivel3=Scale(pestaña3,variable=self.nivel3,
                                                 from_ = 1, to = 25, orient = HORIZONTAL,length=216,bg=('#BDBDBD')).place(x=80,y=295)
        entrada3 = ttk.Entry(pestaña3, width=30, textvariable=self.nivel3,font=("arial",10)).place(x=80,y=335)
        boton1=Button(pestaña3,text="Iniciar",command=self.accion_boton3,width=30).place(x=80,y=365)
        boton2=Button(pestaña3,text="Detener",command=self.accion_boton6,width=30).place(x=80,y=400)
#FIGURA TEMPERATURA1
        figure = plt.Figure(figsize=(5,6), dpi=100)
        self.ax = figure.add_subplot(111)
        self.ax.grid(True),self.ax.set_xlabel('$x$'),self.ax.set_ylabel('$y(x)$')
        self.line = FigureCanvasTkAgg(figure, pestaña4)
        self.line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA TEMPERATURA2
        figure = plt.Figure(figsize=(5,6), dpi=100)
        self.ax_2 = figure.add_subplot(111)
        self.ax_2.grid(True),self.ax_2.set_xlabel('$x$'),self.ax_2.set_ylabel('$y(x)$')
        self.line_2 = FigureCanvasTkAgg(figure, pestaña10)
        self.line_2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA TEMPERATURA3
        figure = plt.Figure(figsize=(5,6), dpi=100)
        self.ax_3 = figure.add_subplot(111)
        self.ax_3.grid(True),self.ax_3.set_xlabel('$x$'),self.ax_3.set_ylabel('$y(x)$')
        self.line_3 = FigureCanvasTkAgg(figure, pestaña16)
        self.line_3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA LUZ1
        figure1 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax1 = figure1.add_subplot(111)
        self.ax1.grid(True),self.ax1.set_xlabel('$x$'),self.ax1.set_ylabel('$y(x)$')
        self.line1 = FigureCanvasTkAgg(figure1, pestaña5)
        self.line1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA LUZ2
        figure1 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax1_2 = figure1.add_subplot(111)
        self.ax1_2.grid(True),self.ax1_2.set_xlabel('$x$'),self.ax1_2.set_ylabel('$y(x)$')
        self.line1_2 = FigureCanvasTkAgg(figure1, pestaña11)
        self.line1_2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA LUZ3
        figure1 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax1_3 = figure1.add_subplot(111)
        self.ax1_3.grid(True),self.ax1_3.set_xlabel('$x$'),self.ax1_3.set_ylabel('$y(x)$')
        self.line1_3 = FigureCanvasTkAgg(figure1, pestaña17)
        self.line1_3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA NIVEL1
        figure2 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax2 = figure2.add_subplot(111)
        self.ax2.grid(True),self.ax2.set_xlabel('$x$'),self.ax2.set_ylabel('$y(x)$')
        self.line2 = FigureCanvasTkAgg(figure2, pestaña6)
        self.line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA NIVEL2
        figure2 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax2_2 = figure2.add_subplot(111)
        self.ax2_2.grid(True),self.ax2_2.set_xlabel('$x$'),self.ax2_2.set_ylabel('$y(x)$')
        self.line2_2 = FigureCanvasTkAgg(figure2, pestaña12)
        self.line2_2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA NIVEL3
        figure2 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax2_3 = figure2.add_subplot(111)
        self.ax2_3.grid(True),self.ax2_3.set_xlabel('$x$'),self.ax2_3.set_ylabel('$y(x)$')
        self.line2_3 = FigureCanvasTkAgg(figure2, pestaña18)
        self.line2_3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA pH1
        figure3 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax3 = figure3.add_subplot(111)
        self.ax3.grid(True),self.ax3.set_xlabel('$x$'),self.ax3.set_ylabel('$y(x)$')
        self.line3 = FigureCanvasTkAgg(figure3, pestaña7)
        self.line3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA pH2
        figure3 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax3_2 = figure3.add_subplot(111)
        self.ax3_2.grid(True),self.ax3_2.set_xlabel('$x$'),self.ax3_2.set_ylabel('$y(x)$')
        self.line3_2 = FigureCanvasTkAgg(figure3, pestaña13)
        self.line3_2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA pH3
        figure3 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax3_3 = figure3.add_subplot(111)
        self.ax3_3.grid(True),self.ax3_3.set_xlabel('$x$'),self.ax3_3.set_ylabel('$y(x)$')
        self.line3_3 = FigureCanvasTkAgg(figure3, pestaña19)
        self.line3_3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA DO1
        figure4 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax4 = figure4.add_subplot(111)
        self.ax4.grid(True),self.ax4.set_xlabel('$x$'),self.ax4.set_ylabel('$y(x)$')
        self.line4 = FigureCanvasTkAgg(figure4, pestaña8)
        self.line4.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA DO2
        figure4 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax4_2 = figure4.add_subplot(111)
        self.ax4_2.grid(True),self.ax4_2.set_xlabel('$x$'),self.ax4_2.set_ylabel('$y(x)$')
        self.line4_2 = FigureCanvasTkAgg(figure4, pestaña14)
        self.line4_2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA DO3
        figure4 = plt.Figure(figsize=(5,6), dpi=100)
        self.ax4_3 = figure4.add_subplot(111)
        self.ax4_3.grid(True),self.ax4_3.set_xlabel('$x$'),self.ax4_3.set_ylabel('$y(x)$')
        self.line4_3 = FigureCanvasTkAgg(figure4, pestaña20)
        self.line4_3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA BIOMASA1
##            figure5 = plt.Figure(figsize=(5,6), dpi=100)
##            self.ax5 = figure5.add_subplot(111)
##            self.ax5.grid(True),self.ax5.set_xlabel('$x$'),self.ax5.set_ylabel('$y(x)$')
##            self.line5 = FigureCanvasTkAgg(figure5, pestaña9)
##            self.line5.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA BIOMASA2
##            figure5 = plt.Figure(figsize=(5,6), dpi=100)
##            self.ax5_2 = figure5.add_subplot(111)
##            self.ax5_2.grid(True),self.ax5_2.set_xlabel('$x$'),self.ax5_2.set_ylabel('$y(x)$')
##            self.line5_2 = FigureCanvasTkAgg(figure5, pestaña15)
##            self.line5_2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
#FIGURA BIOMASA3
##            figure5 = plt.Figure(figsize=(5,6), dpi=100)
##            self.ax5_3 = figure5.add_subplot(111)
##            self.ax5_3.grid(True),self.ax5_3.set_xlabel('$x$'),self.ax5_3.set_ylabel('$y(x)$')
##            self.line5_3 = FigureCanvasTkAgg(figure5, pestaña21)
##            self.line5_3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)


        ventana.mainloop()

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

#ACTIVACIÓN COLOR
#1
    def color_rojo1(self):
        respuesta_pin_rojo1=True
        tarjeta1.sendValue('EIO0', True)
        tarjeta1.sendValue('EIO1', False)
        tarjeta1.sendValue('EIO2', False)
        #print('Respuesta del pin Rojo 1: ',respuesta_pin_rojo1)
        
    def color_verde1(self):
        respuesta_pin_verde1=True
        tarjeta1.sendValue('EIO0', False)
        tarjeta1.sendValue('EIO1', True)
        tarjeta1.sendValue('EIO2', False)
        #print('Respuesta del pin Verde 1: ',respuesta_pin_verde1)
        
    def color_azul1(self):
        respuesta_pin_azul1=True
        tarjeta1.sendValue('EIO0', False)
        tarjeta1.sendValue('EIO1', False)
        tarjeta1.sendValue('EIO2', True)
        #print('Respuesta del pin Azul 1: ',respuesta_pin_azul1)

#2
    def color_rojo2(self):
        respuesta_pin_rojo2=True
        tarjeta1.sendValue('EIO3', True)
        tarjeta1.sendValue('EIO4', False)
        tarjeta1.sendValue('EIO5', False)
        #print('Respuesta del pin Rojo 2: ',respuesta_pin_rojo2)
        
    def color_verde2(self):
        respuesta_pin_verde2=True
        tarjeta1.sendValue('EIO3', False)
        tarjeta1.sendValue('EIO4', True)
        tarjeta1.sendValue('EIO5', False)
        #print('Respuesta del pin Verde 2: ',respuesta_pin_verde2)
        
    def color_azul2(self):
        respuesta_pin_azul2=True
        tarjeta1.sendValue('EIO3', False)
        tarjeta1.sendValue('EIO4', False)
        tarjeta1.sendValue('EIO5', True)
        #print('Respuesta del pin Azul 2: ',respuesta_pin_azul2)
#3
    def color_rojo3(self):
        respuesta_pin_rojo3=True
        tarjeta1.sendValue('EIO6', True)
        tarjeta1.sendValue('EIO7', False)
        tarjeta1.sendValue('CIO0', False)
        #print('Respuesta del pin Rojo 3: ',respuesta_pin_rojo3)
        
    def color_verde3(self):
        respuesta_pin_verde3=True
        tarjeta1.sendValue('EIO6', False)
        tarjeta1.sendValue('EIO7', True)
        tarjeta1.sendValue('CIO0', False)
        #print('Respuesta del pin Verde 3: ',respuesta_pin_verde3)
        
    def color_azul3(self):
        respuesta_pin_azul3=True
        tarjeta1.sendValue('EIO6', False)
        tarjeta1.sendValue('EIO7', False)
        tarjeta1.sendValue('CIO0', True)
        #print('Respuesta del pin Azul 3: ',respuesta_pin_azul3)

#MÉTODO FBR1        
    def fbr1(self):
        while True:
            self.referencia_luz1=float(self.luz1.get())
            self.valor_luz1 = tarjeta1.readValue('AIN3')
            self.luz_real1 = (100000 * round(self.valor_luz1,3))
            self.error_luz1 = self.referencia_luz1 - self.luz_real1
            self.integral_luz1 = self.integral_anterior_luz1 + self.error_luz1 * 5
            self.derivativo_luz1 = (self.error_luz1 - self.error_anterior_luz1) / 5
            self.salida_luz1 = (self.kp_luz1 * self.error_luz1 + self.ki_luz1 * self.integral_luz1 + self.kd_luz1 * self.derivativo_luz1 + self.bias_luz1) / 5
            self.error_prior_luz1 = self.error_luz1
            self.integral_prior_luz1 = self.integral_luz1
            self.ax1.set_xlabel('$x$'),self.ax1.set_ylabel('$y(x)$')
            self.ax1.clear()
            self.ax1.plot(self.x1,self.y1), self.ax1.grid(True)
            self.x1.append(datetime.now())
            self.y1.append(self.luz_real1)
            self.line1.draw()
            #print(self.luz_real1)
            #print("valor luz1", self.valor_luz1, '\n' + "luz real1", self.luz_real1)
            if self.salida_luz1 >= 100:
                self.salida_luz1 = 100
            if self.salida_luz1 <= 0:
                self.salida_luz1 = 0
            tarjeta1.sendValue('TDAC3', interp(self.salida_luz1, [0, 100], [0, 5]))
            time.sleep(1)
    #TEMPERATURA 1
            referencia_temperatura1 = float(self.temperatura1.get())
            valor_temp1 = tarjeta1.readValue('AIN0')
            temperatura_real1 = (55.56 * valor_temp1) + 255.37 - 273.15
            self.error_temp1=referencia_temperatura1-temperatura_real1
            self.integral_temp1=self.integral_anterior_temp1+self.error_temp1*5
            self.derivativo_temp1=(self.error_temp1-self.error_anterior_temp1)/5
            self.salida_temp1=(self.kp_temp1*self.error_temp1+self.ki_temp1*self.integral_temp1+self.kd_temp1*self.derivativo_temp1+self.bias_temp1)/5
            self.error_anterior1=self.error_temp1
            self.integral_anterior1=self.integral_temp1
            self.ax.set_xlabel('$x$'),self.ax.set_ylabel('$y(x)$')
            self.ax.clear()
            self.ax.plot(self.x,self.y), self.ax.grid(True)
            self.x.append(datetime.now())
            self.y.append(temperatura_real1)
            self.line.draw()
            
    #-o-

            #print("valor1",valor_temp1,'\n'+"temperatura real1",temperatura_real1)
            #print("error1",self.error_temp1,'\n'+"integral1",self.integral_temp1,'\n'+"derivativo1",self.derivativo_temp1,'\n'+"salida1",self.salida_temp1)

            if self.salida_temp1>=100:
                self.salida_temp1=100
                #print("salida1", self.salida_temp1)
            if self.salida_temp1 <=0:
                self.salida_temp1=0
                #print("salida1",self.salida_temp1)
            tarjeta1.sendValue('DAC0', interp(self.salida_temp1, [0, 100], [0, 5])) #CALEFACTOR
            if temperatura_real1 > referencia_temperatura1: #VENTILADOR
                tarjeta1.sendValue('CIO1',5)
            else:
                tarjeta1.sendValue('CIO1',0)
    #NIVEL1
            self.referencia_nivel1 = float(self.nivel1.get())
            self.voltaje1 = float(tarjeta2.readValue('AIN0'))
            self.nivel_real1 = float(5.8953 * self.voltaje1 + 2.5354)
            #print('nivel1= ', "{0:.2f}".format(self.nivel_real1))
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
            comunicacion.initI2C(1, 0, 6)
            comunicacion.sendValueI2C([82])
            time.sleep(0.9)
            self.pH1_real=comunicacion.readValueI2C()
            #print("pH1: ",self.pH1_real)
            self.ax3.set_xlabel('$x$'),self.ax3.set_ylabel('$y(x)$')
            self.ax3.clear()
            self.ax3.plot(self.x3,self.y3), self.ax3.grid(True)
            self.x3.append(datetime.now())
            self.y3.append(self.pH1_real)
            self.line3.draw()
    #DO1
            comunicacion.initI2C(1, 0, 3)
            comunicacion.sendValueI2C([82])#114
            time.sleep(0.6)
            self.DO_real1=comunicacion.readValueI2C()
            #print("DO1: ",self.DO_real1)
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
            
            self.lista_temp1.append(temperatura_real1)
            frame_data1_1 = {'temperatura fbr1': self.lista_temp1}
            df = pandas.DataFrame(frame_data1_1)
            df.to_excel("Temperatura_fbr1.xlsx", "Sheet1")

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
            #print("valor luz2", self.valor_luz2, '\n' + "luz real2", self.luz_real2)
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

            #print("valor2",valor_temp2,'\n'+"temperatura real2",temperatura_real2)
            #print("error2",self.error_temp2,'\n'+"integral2",self.integral_temp2,'\n'+"derivativo2",self.derivativo_temp2,'\n'+"salida2",self.salida_temp2)

            if self.salida_temp2>=100:
                self.salida_temp2=100
                #print("salida2", self.salida_temp2)
            if self.salida_temp2 <=0:
                self.salida_temp2=0
                #print("salida1",self.salida_temp2)
            tarjeta1.sendValue('DAC1', interp(self.salida_temp2, [0, 100], [0, 5])) #CALEFACTOR 2
            if temperatura_real2 > referencia_temperatura2: #VENTILADOR 2
                tarjeta1.sendValue('CIO2',5)
            else:
                tarjeta1.sendValue('CIO2',0)
    #NIVEL2
            self.referencia_nivel2 = float(self.nivel2.get())
            self.voltaje2 = float(tarjeta2.readValue('AIN1'))
            self.nivel_real2 = float(5.8953 * self.voltaje2 + 2.5354)
            #print('nivel2= ', "{0:.2f}".format(self.nivel_real2))
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
            #print("pH2: ",self.pH2_real)
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
            #print("DO2: ",self.DO_real2)
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
            #print("valor luz3", self.valor_luz3, '\n' + "luz real3", self.luz_real3)
            if self.salida_luz3 >= 100:
                self.salida_luz3 = 100
            if self.salida_luz3 <= 0:
                self.salida_luz3 = 0
            tarjeta1.sendValue('TDAC5', interp(self.salida_luz3, [0, 100], [0, 5]))
    #TEMPERATURA3
            referencia_temperatura3 = float(self.temperatura3.get())
            valor_temp3 = tarjeta1.readValue('AIN2')
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

            #print("valor3",valor_temp3,'\n'+"temperatura real3",temperatura_real3)
            #print("error3",self.error_temp3,'\n'+"integral3",self.integral_temp3,'\n'+"derivativo3",self.derivativo_temp3,'\n'+"salida3",self.salida_temp3)

            if self.salida_temp3>=100:
                self.salida_temp3=100
                #print("salida3", self.salida_temp3)
            if self.salida_temp3 <=0:
                self.salida_temp3=0
                #print("salida3",self.salida_temp3)
            tarjeta1.sendValue('TDAC2', interp(self.salida_temp3, [0, 100], [0, 5])) #CALEFACTOR 3
            if temperatura_real3 > referencia_temperatura3: #VENTILADOR 3
                tarjeta1.sendValue('CIO3',5)
            else:
                tarjeta1.sendValue('CIO3',0)
    #NIVEL3
            self.referencia_nivel3 = float(self.nivel3.get())
            self.voltaje3 = float(tarjeta2.readValue('AIN2'))
            self.nivel_real3 = float(5.8953 * self.voltaje3 + 2.5354)
            #print('nivel3= ', "{0:.2f}".format(self.nivel_real3))
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
            #print("pH3: ",self.pH3_real)
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
            #print("DO3: ",self.DO_real3)
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

