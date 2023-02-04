# Main test

from ADRC import *
import tkinter as tk #TKINTER ES PARA INTERFAZ GRÁFICA
from tkinter import ttk #PAQUETE TTK
import time


class main():
    def __init__(self):
        self.root = tk.Tk()
        notebook=ttk.Notebook(self.root) #CREAR OBJETO PARA GESTIONAR LAS PESTAÑAS
        notebook.pack(fill='both',expand='yes') # COnfiguration para que las pestañas tengan el mismo tamaño de la pant
        
        # Crear Frames blancos
        tab_FBR1=tk.Frame(notebook,bg='white')  #
        tab_FBR2=tk.Frame(notebook,bg='white')  #
        tab_FBR3=tk.Frame(notebook,bg='white')  #
        
        #ASIGNACIÓN PESTAÑAS FBR1,FBR2 Y FBR3
        
        notebook.add(tab_FBR1,text='FBR1') #
        notebook.add(tab_FBR2,text='FBR2') #
        notebook.add(tab_FBR3,text='FBR3') #
        
        # Configurations FBR1, FBR2 y FBR3
        self.window_FBR(tab_FBR1)
        
        self.window_FBR(tab_FBR2)
        
        self.window_FBR(tab_FBR3)
        
        
        
    def main(self):
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
       
    def window_FBR(self, tab):
        right_frame = tk.Frame(tab, bg='#C0C0C0', bd=1.5) #bg=color; bd=tamaño del borde en pixeles
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
        notebook.add(tab_Light,text='  Light Intensity    ')
        notebook.add(tab_PBR_lvl,text='  PBR Level  ')       
        notebook.add(tab_DO,text='  DO  ')
        notebook.add(tab_pH,text='  pH  ')
        notebook.add(tab_Biomass,text='  Biomass  ')
        
        # Mini panels for the tab
        tk.Label(tab,text="Light",font=("arial",15),bg=('white')).place(x=10,y=10)
        tk.Label(tab,text="Color",font=("arial",14),bg=('white')).place(x=10,y=40)
        rcolor=tk.IntVar()
        rcolor.set(4)
        tk.Radiobutton(tab, text="Red", variable=rcolor, value=1, command=self.color_rojo(tab),font=("arial",10),bg=('white')).place(x=10,y=70)
        tk.Radiobutton(tab, text="Green", variable=rcolor, value=2, command=self.color_verde(tab),font=("arial",10),bg=('white')).place(x=10,y=90)
        tk.Radiobutton(tab, text="Blue", variable=rcolor, value=3, command=self.color_azul(tab),font=("arial",10),bg=('white')).place(x=10,y=110)
        tk.Radiobutton(tab, text="White", variable=rcolor, value=4, command=self.color_white(tab),font=("arial",10),bg=('white')).place(x=10,y=130)
        luz=tk.DoubleVar()
        tk.Scale(tab,variable=luz, from_ = 1, to = 900, orient = "horizontal",length=216,bg=('#BDBDBD')).place(x=80,y=70)
        ttk.Entry(tab, width=30, textvariable=luz,font=("arial",10)).place(x=80,y=110)
        tk.Label(tab,text="Color Intensity",font=("arial",12),bg=('white')).place(x=140,y=40)
        tk.Label(tab,text="Temperature",font=("arial",15),bg=('white')).place(x=10,y=165)
        tk.Label(tab, text="Ref:",font=("arial",12),bg=('white')).place(x=10,y=195)
        temperatura=tk.DoubleVar()
        tk.Scale(tab,variable=temperatura, from_ = 1, to = 92, orient = "horizontal",length=216,bg=('#BDBDBD')).place(x=80,y=195)
        ttk.Entry(tab, width=30, textvariable=temperatura,font=("arial",10)).place(x=80,y=235)
        tk.Label(tab,text="PBR Level",font=("arial",15),bg=('white')).place(x=10,y=265)
        tk.Label(tab, text="Ref:",font=("arial",12),bg=('white')).place(x=10,y=295)
        nivel=tk.DoubleVar()
        tk.Scale(tab,variable=nivel, from_ = 1, to = 25, orient = "horizontal",length=216,bg=('#BDBDBD')).place(x=80,y=295)
        ttk.Entry(tab, width=30, textvariable=nivel,font=("arial",10)).place(x=80,y=335)
        tk.Button(tab,text="Start",command=self.star_FBR(tab),width=30).place(x=80,y=365)
        tk.Button(tab,text="Stop",command=self.stop_FBR(tab),width=30).place(x=80,y=400)
        
    # Color activation    
    def color_rojo(self,PBR): 
        return
    def color_verde(self,PBR):   
        return
    def color_azul(self, PBR):
        return
    def color_white(self, PBR):
        return
    # start threads
    def star_FBR(self,PBR): 
        return
    def stop_FBR(self,PBR):   
        return

    def run(self):
        self.root.mainloop()
            
    # close the application
    def close(self):
       self.root.destroy()
       
if __name__ == "__main__":
    main = main()
    main.main()
    main.run()






