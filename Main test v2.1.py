# Main test

from ADRC import *
import tkinter as tk #TKINTER ES PARA INTERFAZ GRÁFICA
from tkinter import ttk #PAQUETE TTK


import matplotlib.pyplot as plt #GRAHP LIBRARY
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #GUI CANVAS

#

from ljm1 import Ljm1 #LIBRERÍA LabJack1
from ljm2 import Ljm2 #LIBRERIA LabJack2

import continuous_threading
import time
import datetime

Labjack1 = Ljm1 #LIB
Labjack2 = Ljm2 #LIB
class Window_FBR:
    def __init__(self,tab):
        """
        New Widows 
        """
        right_frame = tk.Frame(master=tab, bg='#C0C0C0', bd=1.5) #bg=color; bd=tamaño del borde en pixeles # Care master add
        right_frame.place(relx=0.3, rely=0.055, relwidth=0.65, relheight=0.8) #posicionamiento de elementos horizontal,vertical,ancho,largo
        notebook=ttk.Notebook(right_frame)
        notebook.pack(fill='both',expand='yes')
        tab_temperature=ttk.Frame(notebook)
        tab_Light=ttk.Frame(notebook)
        tab_PBR_lvl=ttk.Frame(notebook)
        tab_DO=ttk.Frame(notebook)
        tab_pH=ttk.Frame(notebook)
        tab_Biomass=ttk.Frame(notebook)
        notebook.add(tab_temperature,text=' Temperature ')
        notebook.add(tab_Light,text=' Light Intensity ')
        notebook.add(tab_PBR_lvl,text=' PBR Level ')       
        notebook.add(tab_DO,text=' DO ')
        notebook.add(tab_pH,text=' pH ')
        notebook.add(tab_Biomass,text=' Biomass ')
        
        # Mini panels for the tab
        tk.Label(tab,text="Light",font=("arial",15),bg=('white')).place(x=10,y=10)
        tk.Label(tab,text="Color",font=("arial",14),bg=('white')).place(x=10,y=40)
        
        #   Configuration for the panels for the varaibles 
        
        frame_variable_temp= plt.Figure(figsize=(5,6), dpi=100)
        frame_variable_Iin= plt.Figure(figsize=(5,6), dpi=100)
        frame_variable_Lvl= plt.Figure(figsize=(5,6), dpi=100)
        frame_variable_pH= plt.Figure(figsize=(5,6), dpi=100)
        frame_variable_DO= plt.Figure(figsize=(5,6), dpi=100)
        frame_variable_Biomass= plt.Figure(figsize=(5,6), dpi=100)
        
        
        self.xTemp = frame_variable_temp.add_subplot(111)
        self.xIin = frame_variable_Iin.add_subplot(111)
        self.xLvl = frame_variable_Lvl.add_subplot(111)
        self.xpH = frame_variable_pH.add_subplot(111)
        self.xDO = frame_variable_DO.add_subplot(111)
        self.xBiomas = frame_variable_Biomass.add_subplot(111)
        
        #Figure Temperature
        self.xTemp.grid(True),self.xTemp.set_xlabel('$Time$'),self.xTemp.set_ylabel('$°C$')
        self.xTemp.set_ylim([0, 50])
        self.lineTemp = FigureCanvasTkAgg(frame_variable_temp, tab_temperature)
        self.lineTemp.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
        
        #Figure Ligt
        self.xIin.grid(True),self.xIin.set_xlabel('$Time$'),self.xIin.set_ylabel('$\mu mol \cdot m^{-2} \cdot s^{-1}$')
        self.xIin.set_ylim([0, 1500])
        self.lineIin = FigureCanvasTkAgg(frame_variable_Iin, tab_Light)
        self.lineIin.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
        
        # Figure level
        self.xLvl.grid(True),self.xLvl.set_xlabel('$Time$'),self.xLvl.set_ylabel('$Cm$')
        
        self.lineLvl = FigureCanvasTkAgg(frame_variable_Lvl, tab_PBR_lvl)
        self.lineLvl.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
        
        #FIGURA pH
        self.xpH.grid(True),self.xpH.set_xlabel('$Time$'),self.xpH.set_ylabel('$pH$')
        self.xpH.set_ylim([0, 14])
        self.linepH = FigureCanvasTkAgg(frame_variable_pH, tab_pH)
        self.linepH.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
        
        #FIGURA DO
        self.xDO.grid(True),self.xDO.set_xlabel('$TIme$'),self.xDO.set_ylabel('$mg \cdot L^{-1}$')
        self.xDO.set_ylim([0, 100])
        self.lineDO = FigureCanvasTkAgg(frame_variable_DO, tab_DO)
        self.lineDO.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
        
        #FIGURA Biomass
        self.xBiomas.grid(True),self.xBiomas.set_xlabel('$Time$'),self.xBiomas.set_ylabel('$Density$')
        self.xBiomas.set_ylim([0, 100])
        self.lineBiomass = FigureCanvasTkAgg(frame_variable_Biomass, tab_Biomass)
        self.lineBiomass.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
        
    
    def __main__(self, tab):
        self.tab = tab #intance of tab
        
        self.rcolor= tk.IntVar(master=tab,value=4)
        tab.rcolor = tk.Radiobutton(tab, text="Red", variable=self.rcolor, value=1, command=self.color_rojo,font=("arial",10),bg=('white')).place(x=10,y=70)
        tk.Radiobutton(tab, text="Green", variable=self.rcolor, value=2, command=self.color_verde,font=("arial",10),bg=('white')).place(x=10,y=90)
        tk.Radiobutton(tab, text="Blue", variable=self.rcolor, value=3, command=self.color_azul,font=("arial",10),bg=('white')).place(x=10,y=110)
        tk.Radiobutton(tab, text="White", variable=self.rcolor, value=4, command=self.color_white,font=("arial",10),bg=('white')).place(x=10,y=130)
        
        
        luz=tk.DoubleVar(master=tab)
        tk.Scale(tab,variable=luz, from_ = 1, to = 900, orient = "horizontal",length=216,bg=('#BDBDBD')).place(x=80,y=70)
        ttk.Entry(tab, width=30, textvariable=luz,font=("arial",10)).place(x=80,y=110)
        tk.Label(tab,text="Color Intensity",font=("arial",12),bg=('white')).place(x=140,y=40)
        tk.Label(tab,text="Temperature",font=("arial",15),bg=('white')).place(x=10,y=165)
        tk.Label(tab, text="Ref:",font=("arial",12),bg=('white')).place(x=10,y=195)
        
        temperatura=tk.DoubleVar(master=tab)
        tk.Scale(tab,variable=temperatura, from_ = 1, to = 92, orient = "horizontal",length=216,bg=('#BDBDBD')).place(x=80,y=195)
        ttk.Entry(tab, width=30, textvariable=temperatura,font=("arial",10)).place(x=80,y=235)
        tk.Label(tab,text="PBR Level",font=("arial",15),bg=('white')).place(x=10,y=265)
        tk.Label(tab, text="Ref:",font=("arial",12),bg=('white')).place(x=10,y=295)
        
        nivel=tk.DoubleVar(master=tab)
        tk.Scale(tab,variable=nivel, from_ = 1, to = 25, orient = "horizontal",length=216,bg=('#BDBDBD')).place(x=80,y=295)
        ttk.Entry(tab, width=30, textvariable=nivel,font=("arial",10)).place(x=80,y=335)
        
            
        
        
        
    #def MyThread2(self):
    #    pass
    # end def
    

            
    # Color activation    
    def color_rojo(self): 
        return
    def color_verde(self):   
        return
    def color_azul(self):
        return
    def color_white(self):
        return


class SettingWidnows:
    def __init__(self):
        a = 1
        #hola

class threads:
    def __init__(self, tab):
        B_start = tk.Button(tab,text="Start",command=self.star_FBR(tab),width=30).place(x=80,y=365)
        B_Stop = tk.Button(tab,text="Stop",command=self.stop_FBR(tab),width=30).place(x=80,y=400)

class Main():
    def __init__(self):
        self.root = tk.Tk()
        # Icono
        self.root.tk.call('wm', 'iconphoto', self.root._w, tk.PhotoImage(file='supervision.png'))
        # Configuratin of the wimdows
        self.root.title("ADRC")
        self.root.geometry('1100x720') #Size pixels
        self.root.configure(background='red') 
        self.root.config(bg='blue') # Borders
        
        menubar = tk.Menu(self.root) # New Menu
        self.root.config(menu=menubar)  
        
        # Menu for File
        menu_archivo = tk.Menu(menubar) #ELEMENTOS BARRA DE MENU
        menu_archivo = tk.Menu(menubar, tearoff=0)    
        menu_edicion = tk.Menu(menubar)
        menu_edicion = tk.Menu(menubar, tearoff=0)
        menu_ayuda = tk.Menu(menubar)
        menu_ayuda = tk.Menu(menubar, tearoff=0)
        
        # Menus
        menubar.add_cascade(label="File", menu=menu_archivo)
        menubar.add_cascade(label="Edit", menu=menu_edicion)
        menubar.add_cascade(label="Help", menu=menu_ayuda)
                
        # Comands for menus
        menu_archivo.add_command(label="New")
        menu_archivo.add_command(label="Open")
        menu_archivo.add_command(label="Save")
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Exit", command=self.close)
        menu_ayuda.add_command(label="Thanks",command=self.f_acerca) # f.acerca = MÉTODO CON LA FIGURA AGRADECIMIENTO
        menu_ayuda.add_command(label="About",command=self.f_about)   # f.about  = About method
        
        #
        self.notebook=ttk.Notebook(self.root) #CREAR OBJETO PARA GESTIONAR LAS PESTAÑAS
        self.notebook.pack(fill='both',expand='yes') # COnfiguration para que las pestañas tengan el mismo tamaño de la pant
        
       
         # Crear Frames blancos
        self.tab_FBR1=tk.Frame(self.notebook,bg='white')  #
        self.tab_FBR2=tk.Frame(self.notebook,bg='white')  #
        self.tab_FBR3=tk.Frame(self.notebook,bg='white')  #
        
        #ASIGNACIÓN PESTAÑAS FBR1,FBR2 Y FBR3
        self.notebook.add(self.tab_FBR1,text='FBR1') #
        self.notebook.add(self.tab_FBR2,text='FBR2') #
        self.notebook.add(self.tab_FBR3,text='FBR3') #     
        # Configurations FBR1, FBR2 y FBR3
        self.wFBR1 = Window_FBR(self.tab_FBR1)     
        self.wFBR2 = Window_FBR(self.tab_FBR2)  
        self.wFBR3 = Window_FBR(self.tab_FBR3)
        
        
        # Configurations of figures for FBR1, FBR2 y FBR3
        
     
        
        
        
        # Here is the start buttons
        
        tk.Button(text="Start",command=self.star_FBR,width=30).place(x=80,y=365)
        tk.Button(text="Stop",command=self.stop_FBR,width=30).place(x=80,y=400)
        
        b=0
    def MyThread(self, a):
            # start threads
            global b
            print('Count:', a)
            print('suma')
            print('suma 2')
            #print(th.isDaemon())
            a += 1
            time.sleep(1)
    
    
    def star_FBR(self): 
        print('Starting or Resuming Threads')
        # Threads FBR
        
        self.th = continuous_threading.ContinuousThread(target=self.MyThread, args=[0] ) #Defining the thread as continuos thread in a loop
        # self.th.daemon = True # Set thread to daemon
        print(self.th.is_running)
        #if self.th.is_running == False:
        self.th.start()
        print(self.th.is_running)
        
            
    def stop_FBR(self):
        print('Pausing Threads')
        self.th.stop()
    
  
        
    def main(self):
        # call the main function of each PBR
        self.wFBR1.__main__(self.tab_FBR1)
        self.wFBR2.__main__(self.tab_FBR2)
        self.wFBR3.__main__(self.tab_FBR3)
        
    

    
    def f_acerca(self):
        acerca = tk.Toplevel()
        acerca.geometry("700x720")
        acerca.bg=('red')
        acerca.resizable(width=False, height=False)
        acerca.title("Acknowledgment:")
        marco1 = ttk.Frame(acerca,padding=(10, 10, 10, 10))
        marco1.pack(side="top", fill="both", expand=True)
        self.fondo=tk.PhotoImage(file="logo.png")
        self.labelfondo=tk.Label(marco1,image=self.fondo).place(x=0,y=30)
        boton1 = tk.Button(marco1, text="Exit",command=acerca.destroy)
        boton1.pack(side="bottom", padx=10, pady=0)
        boton1.focus_set()
    # Información Adicional        
    def f_about(self):
        about = tk.Toplevel()
        about.geometry("900x720")
        about.bg=('red')
        about.resizable(width=False, height=False)
        about.title("This software was developed by:")
        marco1 = ttk.Frame(about,padding=(10, 10, 10, 10))
        marco1.pack(side="top", fill="both", expand=True)
        self.fondo=tk.PhotoImage(file="logo_II.png")
        self.labelfondo=tk.Label(marco1,image=self.fondo).place(x=0,y=30)
        boton1 = tk.Button(marco1, text="Exit",command=about.destroy)
        boton1.pack(side="bottom", padx=10, pady=0)
        boton1.focus_set()      
  
  
    def run(self):
        self.root.mainloop()
        
            
    # close the application
    def close(self):
       self.root.destroy()



def monitoring():
    Labjack1.initI2C(1, 0, 6) #EL OBJETO comunicación LLAMA AL MÉTODO initI2C (TX,RX,DIRECCIÓN)
    Labjack1.sendValueI2C([82]) #EL OBJETO comunicación LLAMA AL MÉTODO sendValueI2C ([COMANDO ASCII]) EN CASO DE NECESITAR OTRA UTILIDAD VER MANUAL DEL SENSOR
    time.sleep(0.9) #POR NADA DEL MUNDO SE PUEDE CAMBIAR ESTE RETARDO (VER MANUAL DEL SENSOR)
    DO_real=float(Labjack1.readValueI2C()) #LEER SENSOR
    print('DO1',DO_real)
    self.ax3_1.clear()
    self.ax3_1.set_xlabel('$Time$'),self.ax3_1.set_ylabel('$mg/L$')
    # Limiting the list to be 20
    Time_PBR1=self.x3[-20:]
    DO_PBR1=self.y3[-20:]
    self.ax3_1.plot(Time_PBR1,DO_PBR1), self.ax3_1.grid(True)
    self.ax3_1.set_ylim(0, 50)
    self.x3.append(datetime.now())
    self.y3.append(DO_real)
    self.line3.draw()
    # Limiting the storage vectors
    self.x3=self.x3[-20:]
    self.y3=self.y3[-20:]
    
    #pH1
    Labjack1.initI2C(1, 0, 3)
    Labjack1.sendValueI2C([82])#114
    time.sleep(0.6) #POR NADA DEL MUNDO SE PUEDE CAMBIAR ESTE RETARDO (VER MANUAL DEL SENSOR)
    pH_real1=float(Labjack1.readValueI2C())
    print('pH1',pH_real1)
    self.ax4_1.clear()
    self.ax4_1.set_xlabel('$Time$'),self.ax4_1.set_ylabel('$pH$')
            # Limiting the list to be 20
    pH_PBR1=self.y4[-20:]
    self.ax4_1.plot(Time_PBR1,pH_PBR1), self.ax4_1.grid(True)
    self.ax4_1.set_ylim(0, 14)
    self.x4.append(datetime.now())
    self.y4.append(pH_real1)
    self.line4.draw()
    # Limiting the storage vectors
    self.x4=self.x4[-20:]
    self.y4=self.y4[-20:]

    #DO2
    Labjack1.initI2C(1, 0, 5)
    Labjack1.sendValueI2C([82])
    time.sleep(0.9)
    DO2_real=float(Labjack1.readValueI2C())
    self.ax3_2.clear()
    self.ax3_2.set_xlabel('$Time$'),self.ax3_2.set_ylabel('$mg/L$')
    # Limiting the list to be 20
    Time_PBR2=self.x3_2[-20:]
    OD_PBR2=self.y3_2[-20:]
    print('DO2',DO2_real)
    self.ax3_2.plot(Time_PBR2,OD_PBR2), self.ax3_2.grid(True)
    self.ax3_2.set_ylim(0, 50)
    self.x3_2.append(datetime.now())
    self.y3_2.append(DO2_real)
    self.line3_2.draw()
    # Limiting the storage vectors
    self.x3_2=self.x3_2[-20:]
    self.y3_2=self.y3_2[-20:]
    
    #pH2
    Labjack1.initI2C(1, 0, 2)
    Labjack1.sendValueI2C([82])#114
    time.sleep(0.6)
    pH_real2=float(comunicacion.readValueI2C())
    print('pH2',pH_real2)
    self.ax4_2.clear()
    self.ax4_2.set_xlabel('$Time$'),self.ax4_2.set_ylabel('$pH$')
    # Limiting the list to be 20
    pH_PBR2=self.y4_2[-20:]
    self.ax4_2.plot(Time_PBR2,pH_PBR2), self.ax4_2.grid(True)
    self.ax4_2.set_ylim(0, 14)
    self.x4_2.append(datetime.now())
    self.y4_2.append(pH_real2)
    self.line4_2.draw()
    # Limiting the storage vectors
    self.x4_2=self.x4_2[-20:]
    self.y4_2=self.y4_2[-20:]
    
    #DO3
    Labjack1.initI2C(1, 0, 4)
    Labjack1.sendValueI2C([82])
    time.sleep(0.9)
    DO3_real=float(Labjack1.readValueI2C())
    self.ax3_3.clear()
    self.ax3_3.set_xlabel('$Time$'),self.ax3_3.set_ylabel('$mg/L$')
    print('DO3',DO3_real)
    # Limiting the list to be 20
    Time_PBR3=self.x3_3[-20:]
    OD_PBR3=self.y3_3[-20:]
    self.ax3_3.plot(Time_PBR3,OD_PBR3), self.ax3_3.grid(True)
    self.ax3_3.set_ylim(0, 50)
    self.x3_3.append(datetime.now())
    self.y3_3.append(DO3_real)
    self.line3_3.draw()
    # Limiting the storage vectors
    self.x3_3=self.x3_3[-20:]
    self.y3_3=self.y3_3[-20:]
    
    #pH3
    Labjack1.initI2C(1, 0, 1)
    Labjack1.sendValueI2C([82])#114
    time.sleep(0.6)
    pH_real3=float(Labjack1.readValueI2C())
    self.ax4_3.clear()
    self.ax4_3.set_xlabel('$Time$'),self.ax4_3.set_ylabel('$pH$')
    print('pH3', pH_real3)
    # Limiting the list to be 20
    pH_PBR3=self.y4_3[-20:]
    self.ax4_3.plot(Time_PBR3,pH_PBR3), self.ax4_3.grid(True)
    self.ax4_3.set_ylim(0, 14)
    self.x4_3.append(datetime.now())
    self.y4_3.append(pH_real3)
    self.line4_3.draw()
    # Limiting the storage vectors
    self.x4_3=self.x4_3[-20:]
    self.y4_3=self.y4_3[-20:]




if __name__ == "__main__":
    main = Main()  # intance of main
    main.main()    # call method main of main class
    main.run()     # call mainloop of the wimdows
    

    


