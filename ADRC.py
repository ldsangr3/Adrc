#ADRC
# This class implemented the ADRC controller 
# u is the control signal
# y is the output
# L1 and L2 are the gains of the observer


from collections import deque
from math import *

class ADRC():
    def __init__(self, disturbance, plant_output, x_stimation, Control_singal, integral_): 
        #Condiciones iniciales 
        self.disturbance = disturbance # Inicial disturbance
        self.Control_singal = Control_singal # Inicial control signal
        self.plant_output = plant_output # Inicial output
        self.x_stimation = x_stimation #State stimation 
        self.integral_ = integral_ #State stimation

    def reset_controller (self):
        self.disturbance = 0 # Inicial disturbance
        self.Control_singal = 0 # Inicial control signal
        self.plant_output = 0 # Inicial output
        self.x_stimation = 0 #State stimation 
        self.integral_ = 0 #State stimation
    
    #x_p is the state to integrate
    def integral(self, integral_previous, x_p, x_pp):
        h=0.1 # Fixed time for now t(n)-t(n-1) elapsed time
        integral_Gain=1
        integral = self.integral_previous + integral_Gain*h*(self.x_p+self.x_pp)/2 #Trapezoidal method
        return integral    
    

    def observer(self, y, u):
        L1=1
        e=1
        disturbance_p = u + L1*e
        return disturbance_p
