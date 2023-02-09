# Release ADRC 
# Stils Bugs at vector of DO of PBR3
import numpy as np #Numpy
from ADRC import *
import tkinter as tk #TKINTER ES PARA INTERFAZ GRÁFICA
from tkinter import ttk # TTK


import matplotlib.pyplot as plt #GRAHP LIBRARY
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #GUI CANVAS

# Image loading library
from PIL import ImageTk, Image

from ljm1 import Ljm1 #LabJack1
from ljm2 import Ljm2 #LabJack2

import continuous_threading
import time
import datetime

from PID import PID_Event_Based

# Intances for the Labjacks, and starting the comunication
Labjack1 = Ljm1() #LIB
Labjack2 = Ljm2() #LIB

# Library to export data
from openpyxl import load_workbook as load_excel_file
from openpyxl import Workbook






class Window_FBR:
    def __init__(self,tab):
        """
        New Widows 
        """
        right_frame = tk.Frame(master=tab, bg='#00205B', bd=1.5) #bg=color; bd=tamaño del borde en pixeles # Care master add
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
        tk.Label(tab,text="Light",font=("Helvetica",15), fg='white', bg=('#00205B')).place(x=10,y=10)
        tk.Label(tab,text="Color",font=("Helvetica",14), fg='white', bg=('#00205B')).place(x=10,y=40)
        
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
        self.xLvl.grid(True),self.xLvl.set_xlabel('$Time$'),self.xLvl.set_ylabel('$cm$')
        
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
        
        self.rcolor = tk.IntVar(master=tab,value=4)
        tab.rcolor = tk.Radiobutton(tab, text="Red", variable=self.rcolor, value=1, command=self.color_rojo,font=("Helvetica",10), bg=('#00205B'), fg=('white'), activebackground='#0E62A6', activeforeground='white', selectcolor='black', foreground='white').place(x=10,y=70)
        tab.rcolor = tk.Radiobutton(tab, text="Green", variable=self.rcolor, value=2, command=self.color_verde,font=("Helvetica",10), bg=('#00205B'), fg=('white'), activebackground='#0E62A6', activeforeground='white', selectcolor='black', foreground='white').place(x=10,y=95)
        tab.rcolor = tk.Radiobutton(tab, text="Blue", variable=self.rcolor, value=3, command=self.color_azul,font=("Helvetica",10), bg=('#00205B'), fg=('white'), activebackground='#0E62A6', activeforeground='white', selectcolor='black', foreground='white').place(x=10,y=120)
        tab.rcolor = tk.Radiobutton(tab, text="White", variable=self.rcolor, value=4, command=self.color_white,font=("Helvetica",10), bg=('#00205B'), fg=('black'), activebackground='#0E62A6', activeforeground='white', selectcolor='black', foreground='white').place(x=10,y=145)
        
        #activebackground=common_bg, activeforeground=common_fg, selectcolor=common_bg
               
                            
        self.Ref_luz=tk.DoubleVar(master=tab)
        tk.Scale(tab,variable=self.Ref_luz, from_ = 1, to = 900, orient = "horizontal",length=217,bg=('#BDBDBD')).place(x=80,y=70)
        ttk.Entry(tab, width=31, textvariable=self.Ref_luz,font=("Helvetica",10)).place(x=80,y=110)
        tk.Label(tab,text="Color Intensity",font=("Helvetica",15), fg='white', bg=('#00205B')).place(x=140,y=40)
        tk.Label(tab,text="Temperature",font=("Helvetica",15), fg='white', bg=('#00205B')).place(x=10,y=175)
        tk.Label(tab, text="Ref:",font=("Helvetica",12), fg='white', bg=('#00205B')).place(x=10,y=205)
        
        self.Ref_tmp=tk.DoubleVar(master=tab)
        tk.Scale(tab,variable=self.Ref_tmp, from_ = 1, to = 92, orient = "horizontal",length=217,bg=('#BDBDBD')).place(x=80,y=205)
        ttk.Entry(tab, width=31, textvariable=self.Ref_tmp, font=("Helvetica",10)).place(x=80,y=245)
        tk.Label(tab,text="PBR Level",font=("Helvetica",15), fg='white',bg=('#00205B')).place(x=10,y=275)
        tk.Label(tab, text="Ref:",font=("Helvetica",12),fg='white', bg=('#00205B')).place(x=10,y=305)
        
        self.Ref_lvl=tk.DoubleVar(master=tab)
        tk.Scale(tab,variable=self.Ref_lvl, from_ = 1, to = 25, orient = "horizontal",length=217,bg=('#BDBDBD')).place(x=80,y=305)
        ttk.Entry(tab, width=31, textvariable=self.Ref_lvl,font=("Helvetica",10)).place(x=80,y=345)
        
            
        
        
     
   

            
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
    pass

class Main():
    def __init__(self):
        self.root = tk.Tk()
        # Icono
        self.root.tk.call('wm', 'iconphoto', self.root._w, tk.PhotoImage(file='supervision.png'))
        # Configuratin of the wimdows
        self.root.title("ADRC")
        self.root.geometry('1280x960') #Size pixels
        
        
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
        
              
        # Create a photoimage object of the image in the path
        icono_sabana = ImageTk.PhotoImage(Image.open("MONOCROMATICA-HRZL.png").resize((176, 67)))
        
        
        
        # Create a label object to display the image   


        label_Sabana = ttk.Label(image= icono_sabana)
        label_Sabana.image =  icono_sabana
        # Position imagex
        label_Sabana.place(x=700, y=790)

        # Blue Frames
        self.tab_FBR1=tk.Frame(self.notebook,bg='#00205B')  #
        self.tab_FBR2=tk.Frame(self.notebook,bg='#00205B')  #
        self.tab_FBR3=tk.Frame(self.notebook,bg='#00205B')  #
        
        
        
        # Tabs FBR1,FBR2 Y FBR3
        self.notebook.add(self.tab_FBR1,text='FBR1') #
        self.notebook.add(self.tab_FBR2,text='FBR2') #
        self.notebook.add(self.tab_FBR3,text='FBR3') #     
        
        # Configuration of FBR1, FBR2 and FBR3
        self.wFBR1 = Window_FBR(self.tab_FBR1)     
        self.wFBR2 = Window_FBR(self.tab_FBR2)  
        self.wFBR3 = Window_FBR(self.tab_FBR3)
        
        
        # Instances ofs PIDs
        self.PID_temp_PBR1 = PID_Event_Based (P=1.5, I=0.5, D=0.01, Z=0)
        self.PID_temp_PBR2 = PID_Event_Based (P=2, I=0.2, D=0.02, Z=0)
        self.PID_temp_PBR3 = PID_Event_Based (P=3, I=0.5, D=0.1, Z=0)         
        

        #Start storage variables
        # Global variables 
        self.Time_PBR1=[] 
        self.Time_PBR2=[]
        self.Time_PBR3=[]
        
        self.pH_PBR1=[]
        self.pH_PBR2=[]
        self.pH_PBR3=[]
        
        self.DO_PBR1=[]
        self.DO_PBR2=[]
        self.DO_PBR3=[]
        
        self.lvl_PBR1=[]
        self.lvl_PBR2=[]
        self.lvl_PBR3=[]
        self.Timelvl_PBR1=[]
        self.Timelvl_PBR2=[]
        self.Timelvl_PBR3=[]
        
        self.Iin_PBR1=[]
        self.Iin_PBR2=[]
        self.Iin_PBR3=[]
        self.TimeIin=[]
        
        
        self.TimeTemperature=[]
        self.Tmp_PBR1=[]
        self.Tmp_PBR2=[]
        self.Tmp_PBR3=[]
        
        # Create  aExcel Boot to save data
        wb = load_excel_file("Data_Excel")
        
        

        # Here is the start buttons
        
        tk.Button(text="Start",command=self.star_FBR,width=30).place(x=80,y=435)
        tk.Button(text="Stop",command=self.stop_FBR,width=30).place(x=80,y=465)
        
    
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
        pid_temperature_executiontime=1
        self.th = continuous_threading.ContinuousThread(target=self.MyThread, args=[0] ) #Defining the thread as continuos thread in a loop
        self.th2 = continuous_threading.ContinuousThread(target=self.monitoring) #Defining the thread as continuos thread in a loop
        self.th3 = continuous_threading.PeriodicThread(1,target=self.nivel_monitoring) #Defining the thread as periodic thread in a loop
        self.th4 = continuous_threading.PeriodicThread(1,target=self.Light_control) #Defining the thread as periodic thread in a loop
        self.th5 = continuous_threading.PeriodicThread(pid_temperature_executiontime,target=self.temperature_control, args=[pid_temperature_executiontime]) #Defining the thread as periodic thread in a loop
        # self.th.daemon = True # Set thread to daemon
        #print(self.th.is_running)
        #if self.th.is_running == False:
        self.th.start()
        self.th2.start()
        self.th3.start()
        self.th4.start()
        self.th5.start()
        #
            
    def stop_FBR(self):
        print('Pausing Threads')
        self.th.stop()
        print('Pausing My Thread')
        self.th2.stop()
        print('Pausing IC2 Network')
        self.th3.stop()
        print('Pausing Level Monitoring')
        self.th4.stop()
        print('Pausing Light Monitoring')
        self.th5.stop()
        print('Pausing temperature control')
  
        
    def main(self):
        # call the main function of each PBR
        self.wFBR1.__main__(self.tab_FBR1)
        self.wFBR2.__main__(self.tab_FBR2)
        self.wFBR3.__main__(self.tab_FBR3)
        
         
    def nivel_monitoring(self):
        # Nivel PBR1
        voltaje_Nivel_PBR1 = float(Labjack2.readValue('AIN0'))
        nivel_real_PBR1 = float(5.8953 * voltaje_Nivel_PBR1 + 2.5354)
        self.wFBR1.xLvl.clear()
        self.wFBR1.xLvl.set_xlabel('$Time$'), self.wFBR1.xLvl.set_ylabel('$cm$')
        self.lvl_PBR1.append(nivel_real_PBR1)
        self.Timelvl_PBR1.append(datetime.datetime.now())
        self.lvl_PBR1=self.lvl_PBR1[-20:]        
        self.Timelvl_PBR1=self.Timelvl_PBR1[-20:]
        self.wFBR1.xLvl.plot(self.Timelvl_PBR1,self.lvl_PBR1), self.wFBR1.xLvl.grid(True)
        self.wFBR1.lineLvl.draw()    
        
        # Nivel PBR2
        voltaje_Nivel_PBR2 = float(Labjack2.readValue('AIN1'))
        nivel_real_PBR2 = float(5.8953 * voltaje_Nivel_PBR2 + 2.5354)
        self.wFBR2.xLvl.clear()
        self.wFBR2.xLvl.set_xlabel('$Time$'), self.wFBR2.xLvl.set_ylabel('$cm$')
        self.lvl_PBR2.append(nivel_real_PBR2)
        self.Timelvl_PBR2.append(datetime.datetime.now())
        self.lvl_PBR2=self.lvl_PBR2[-20:]   
        self.Timelvl_PBR2=self.Timelvl_PBR2[-20:]  
        self.wFBR2.xLvl.plot(self.Timelvl_PBR2,self.lvl_PBR2), self.wFBR2.xLvl.grid(True)   
        self.wFBR2.lineLvl.draw()  
        
        # Nivel PBR3
        voltaje_Nivel_PBR3 = float(Labjack2.readValue('AIN2'))
        nivel_real_PBR3 = float(5.8953 * voltaje_Nivel_PBR3 + 2.5354)
        self.wFBR3.xLvl.clear()
        self.wFBR3.xLvl.set_xlabel('$Time$'), self.wFBR3.xLvl.set_ylabel('$cm$')
        self.lvl_PBR3.append(nivel_real_PBR3)
        self.Timelvl_PBR3.append(datetime.datetime.now())
        self.lvl_PBR3=self.lvl_PBR3[-20:]    
        self.Timelvl_PBR3=self.Timelvl_PBR3[-20:]  
        self.wFBR3.xLvl.plot(self.Timelvl_PBR3,self.lvl_PBR3), self.wFBR3.xLvl.grid(True)  
        self.wFBR3.lineLvl.draw()  
        
        
    
    def temperature_control(self, z):
        #z is the time of execution of the thread

        print("z = ", z)
        
        # append time temperature 
        self.TimeTemperature.append(datetime.datetime.now())
        self.TimeTemperature = self.TimeTemperature[-20:]
        
        
        # Temperature PBR1
        Temp_PBR1 = 55.56*Labjack1.readValue('AIN0') + 255.37 - 273.15 
        self.wFBR1.xTemp.clear()
        self.wFBR1.xTemp.set_xlabel('$Time$'), self.wFBR1.xTemp.set_ylabel('$°C$')
        self.Tmp_PBR1.append(Temp_PBR1)
        self.Tmp_PBR1=self.Tmp_PBR1[-20:]        
        self.wFBR1.xTemp.plot(self.TimeTemperature,self.Tmp_PBR1), self.wFBR1.xTemp.grid(True)
        self.wFBR1.lineTemp.draw()
        
        # Control temp PBR1
        
        # Setpoint
        self.PID_temp_PBR1.setPoint(self.wFBR1.Ref_tmp.get())
        print("the setpoint is", self.PID_temp_PBR1.getPoint())
        # Call update function of the PID and send the value of the actual temperature
        UPID_Temp_PBR1 = self.PID_temp_PBR1.update(Temp_PBR1)
        
        # Write the temperature computed value in the labjack
        Labjack1.sendValue('DAC0', np.interp(UPID_Temp_PBR1, [0, 100], [0, 5])) # Interp
        
        # Turn on Cooler
        if Temp_PBR1 > self.wFBR1.Ref_tmp.get(): #VENTILADOR ACTIVACIÓN DIGITAL
                Labjack1.sendValue('CIO1',5)
        else:
                Labjack1.sendValue('CIO1',0)
        
        
        
        
        
        
        
        
                
                
        # Temperature PBR1
        Temp_PBR2 = 55.56*Labjack1.readValue('AIN1') + 255.37 - 273.15 
        self.wFBR2.xTemp.clear()
        self.wFBR2.xTemp.set_xlabel('$Time$'), self.wFBR2.xTemp.set_ylabel('$°C$')
        self.Tmp_PBR2.append(Temp_PBR2)
        self.Tmp_PBR2=self.Tmp_PBR2[-20:]        
        self.wFBR2.xTemp.plot(self.TimeTemperature,self.Tmp_PBR2), self.wFBR2.xTemp.grid(True)
        self.wFBR2.lineTemp.draw()   
        
        # Temperature PBR1
        Temp_PBR3 = 55.56*Labjack1.readValue('AIN3') + 255.37 - 273.15 
        self.wFBR3.xTemp.clear()
        self.wFBR3.xTemp.set_xlabel('$Time$'), self.wFBR3.xTemp.set_ylabel('$°C$')
        self.Tmp_PBR3.append(Temp_PBR3)
        self.Tmp_PBR3=self.Tmp_PBR3[-20:]        
        self.wFBR3.xTemp.plot(self.TimeTemperature,self.Tmp_PBR3), self.wFBR3.xTemp.grid(True)
        self.wFBR3.lineTemp.draw()   
        
        
    
    def Light_control(self):
         # Append time vector
        self.TimeIin.append(datetime.datetime.now())
        self.TimeIin=self.TimeIin[-20:]
        
        # PBR1
        self.Intensity_PBR1 = (Labjack1.readValue('AIN5')-0.39)*100000 #Read analoge input
        self.wFBR1.xIin.clear()
        self.wFBR1.xIin.grid(True),self.wFBR1.xIin.set_xlabel('$Time$'),self.wFBR1.xIin.set_ylabel('$\mu mol \cdot m^{-2} \cdot s^{-1}$')
        # Append Light vector
        self.Iin_PBR1.append(self.Intensity_PBR1)
        # Limits vector to have 20 elements
        self.Iin_PBR1=self.Iin_PBR1[-20:] 
        self.wFBR1.xIin.plot(self.TimeIin,self.Iin_PBR1)
        self.wFBR1.xIin.set_ylim([0, 1500])
        self.wFBR1.lineIin.draw()
        
        # PBR2
        self.Intensity_PBR2 = (Labjack1.readValue('AIN13')-0.39)*100000 #Read analoge input
        self.wFBR2.xIin.clear()
        self.wFBR2.xIin.grid(True),self.wFBR2.xIin.set_xlabel('$Time$'),self.wFBR2.xIin.set_ylabel('$\mu mol \cdot m^{-2} \cdot s^{-1}$')
        # Append Light vector
        self.Iin_PBR2.append(self.Intensity_PBR2)
        # Limits vector to have 20 elements
        self.Iin_PBR2=self.Iin_PBR2[-20:] 
        self.wFBR2.xIin.plot(self.TimeIin,self.Iin_PBR2)
        self.wFBR2.xIin.set_ylim([0, 1500])
        self.wFBR2.lineIin.draw()
        
        
        # PBR3
        self.Intensity_PBR3 = (Labjack1.readValue('AIN9')-0.39)*100000 #Read analoge input
        self.wFBR3.xIin.clear()
        self.wFBR3.xIin.grid(True),self.wFBR1.xIin.set_xlabel('$Time$'),self.wFBR1.xIin.set_ylabel('$\mu mol \cdot m^{-2} \cdot s^{-1}$')
        # Append Light vector
        self.Iin_PBR3.append(self.Intensity_PBR3)
        # Limits vector to have 20 elements
        self.Iin_PBR3=self.Iin_PBR3[-20:] 
        self.wFBR3.xIin.plot(self.TimeIin,self.Iin_PBR3)
        self.wFBR3.xIin.set_ylim([0, 1500])
        self.wFBR3.lineIin.draw()
        
    
        
 
    
    
    def monitoring(self):
   
        delay = 0
        # start monitoring 
        
        # DO PBR1
        Labjack1.initI2C(1, 0, 6) #EL OBJETO comunicación LLAMA AL MÉTODO initI2C (TX,RX,DIRECCIÓN)
        Labjack1.sendValueI2C([82]) #EL OBJETO comunicación LLAMA AL MÉTODO sendValueI2C ([COMANDO ASCII]) EN CASO DE NECESITAR OTRA UTILIDAD VER MANUAL DEL SENSOR
        time.sleep(0.9 + delay) #POR NADA DEL MUNDO SE PUEDE CAMBIAR ESTE RETARDO (VER MANUAL DEL SENSOR)
        
        # This is in case of a error in the comunication
        try:
            DO_real_PBR1=float(Labjack1.readValueI2C()) #L read the sensor
        except:
            DO_real_PBR1=self.DO_PBR1.pop() #las value
            print("Error de lectura DO PBR1")
        
        print('DO1',DO_real_PBR1)
        self.wFBR1.xDO.clear()
        self.wFBR1.xDO.set_xlabel('$Time$'),self.wFBR1.xDO.set_ylabel('$mg \cdot L^{-1}$')
        # Appendings dataset
        self.Time_PBR1.append(datetime.datetime.now())
        self.DO_PBR1.append(DO_real_PBR1)
        # Limiting the list to be 20
        self.Time_PBR1=self.Time_PBR1[-20:]
        self.DO_PBR1=self.DO_PBR1[-20:]
        self.wFBR1.xDO.plot(self.Time_PBR1,self.DO_PBR1), self.wFBR1.xDO.grid(True)
        self.wFBR1.xDO.set_ylim(0, 50)
        self.wFBR1.lineDO.draw()
    
                
        # pH PBR1
        Labjack1.initI2C(1, 0, 3)
        Labjack1.sendValueI2C([82])#114
        time.sleep(0.6 + delay) #POR NADA DEL MUNDO SE PUEDE CAMBIAR ESTE RETARDO (VER MANUAL DEL SENSOR)
        
        # This is in case of a error in the comunication
        try:
            pH_real_PBR1=float(Labjack1.readValueI2C())
        except:
            pH_real_PBR1=self.pH_PBR1.pop() # Last value
            print("Error de lectura PH PBR1")
                
        print('pH1',pH_real_PBR1)
        self.wFBR1.xpH.clear()
        self.wFBR1.xpH.set_xlabel('$Time$'),self.wFBR1.xpH.set_ylabel('$pH$')
        # appendings dataset
        self.pH_PBR1.append(pH_real_PBR1) 
        # Limiting the list to be 20
        self.pH_PBR1=self.pH_PBR1[-20:]
        self.wFBR1.xpH.plot(self.Time_PBR1,self.pH_PBR1), self.wFBR1.xpH.grid(True)
        self.wFBR1.xpH.set_ylim(0, 14)
        self.wFBR1.linepH.draw()

        # DO PBR2
        Labjack1.initI2C(1, 0, 5)
        Labjack1.sendValueI2C([82])
        time.sleep(0.9 + delay)
        # This is in case of a error in the comunication
        try:
            DO_real_PBR2=float(Labjack1.readValueI2C())
        except:
            DO_real_PBR2=self.DO_PBR2.pop() # Last value 
            print("Error de lectura DO PBR2")
        
        self.wFBR2.xDO.clear()
        self.wFBR2.xDO.set_xlabel('$Time$'),self.wFBR2.xDO.set_ylabel('$mg/L$')
        # Appending dataset
        self.Time_PBR2.append(datetime.datetime.now())
        self.DO_PBR2.append(DO_real_PBR2)        
        # Limiting the list to be 20
        self.Time_PBR2=self.Time_PBR2[-20:]
        self.DO_PBR2=self.DO_PBR2[-20:]
        print('DO2',DO_real_PBR2)
        self.wFBR2.xDO.plot(self.Time_PBR2,self.DO_PBR2), self.wFBR2.xDO.grid(True)
        self.wFBR2.xDO.set_ylim(0, 50)
        self.wFBR2.lineDO.draw()
  
  
        
        # pH PBR2
        Labjack1.initI2C(1, 0, 2)
        Labjack1.sendValueI2C([82])#114
        time.sleep(0.6 + delay)
        
        # This is in case of a error in the comunication
        try:
            pH_real_PBR2=float(Labjack1.readValueI2C())
        except:
            pH_real_PBR2=self.pH_PBR2.pop() # last value
            print("Error de lectura pH PBR2")
        
        print('pH2', pH_real_PBR2)
        self.wFBR2.xpH.clear()
        self.wFBR2.xpH.set_xlabel('$Time$'),self.wFBR2.xpH.set_ylabel('$pH$')
        # Appending data
        self.pH_PBR2.append(pH_real_PBR2)
        # Limiting the list to be 20
        self.pH_PBR2=self.pH_PBR2[-20:]
        self.wFBR2.xpH.plot(self.Time_PBR2,self.pH_PBR2), self.wFBR2.xpH.grid(True)
        self.wFBR2.xpH.set_ylim(0, 14)
        self.wFBR2.linepH.draw()
        
    
        # DO PBR3
        Labjack1.initI2C( 1, 0, 4)
        Labjack1.sendValueI2C([82])
        time.sleep(0.9 + delay)
        
        # This is in case of a error in the comunication
        try:
            DO_real_PBR3=float(Labjack1.readValueI2C())
        except:
            DO_real_PBR3=self.DO_PBR3.pop() # last value
            print("Error de lectura DO PBR3")
        
        print('DO3',DO_real_PBR3)
        self.wFBR3.xDO.clear()
        self.wFBR3.xDO.set_xlabel('$Time$'),self.wFBR3.xDO.set_ylabel('$mg/L$')
        # Apending dataset
        self.Time_PBR3.append(datetime.datetime.now())
        self.DO_PBR3.append(DO_real_PBR3)
        # Limiting the list to be 20
        self.Time_PBR3=self.Time_PBR3[-20:]
        self.DO_PBR3=self.DO_PBR3[-20:]
        self.wFBR3.xDO.plot(self.Time_PBR3,self.DO_PBR3), self.wFBR3.xDO.grid(True)
        self.wFBR3.xDO.set_ylim(0, 50)
        self.wFBR3.lineDO.draw()
        
        # pH PBR3
        Labjack1.initI2C(1, 0, 1)
        Labjack1.sendValueI2C([82])#114
        time.sleep(0.6 + delay)
        # This is in case of a error in the comunication
        try:
            pH_real_PBR3=float(Labjack1.readValueI2C())
        except:
            pH_real_PBR3=self.pH_PBR3.pop() #last value
            print("Error de lectura pH PBR3")
            
            
        self.wFBR3.xpH.clear()
        self.wFBR3.xpH.set_xlabel('$Time$'),self.wFBR3.xpH.set_ylabel('$pH$')
        print('pH3', pH_real_PBR3)
        # Apending data
        self.pH_PBR3.append(pH_real_PBR3)
        # Limiting the list to be 20
        self.pH_PBR3=self.pH_PBR3[-20:]
        self.wFBR3.xpH.plot(self.Time_PBR3,self.pH_PBR3), self.wFBR3.xpH.grid(True)

        self.wFBR3.xpH.set_ylim(0, 14)
        self.wFBR3.linepH.draw()
        
    
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



if __name__ == "__main__":
    main = Main()  # intance of main
    main.main()    # call method main of main class
    main.run()     # call mainloop of the wimdows
    

    


