from collections import deque
from math import *
from Integration import Runge_Kutta

class ADRC:
    def __init__(self, disturbance, plant_output, x_stimation, Control_singal): 
        #Condiciones iniciales 
        self.disturbance = disturbance # Inicial disturbance
        self.Control_singal = Control_singal # Inicial control signal
        self.plant_output = plant_output # Inicial output
        self.x_stimation = x_stimation # State stimation 
        self.integral_ = 0 # State stimation
        
        # Define a integrator
        self.inte_x1 = Runge_Kutta()
        self.inte_x2 = Runge_Kutta()
        self.inte_x2 = Runge_Kutta()
        

    def reset_controller (self):
        self.disturbance = 0 # Inicial disturbance
        self.Control_singal = 0 # Inicial control signal
        self.plant_output = 0 # Inicial output
        self.x_stimation = 0 # State stimation 
        self.integral_ = 0 # State stimation
    


    def observer(self, y, u):
        # Define the function for the ADRC controller
        
        # Calculate the control input
        u = alpha * error + x2
        # Update the state variables
        x1_dot = error - y
        x2_dot = -lambda_ * y + beta * u
        x1 = self.inte_x1.update_integrated_signal(signal=x1_dot, dt=1)
        x2 = self.inte_x2.update_integrated_signal(signal=x2_dot, dt=1)
        return u, x1, x2
        
    def get_x1(self):
        return self.y_ast

    def get_x2(self):
        return self.error

    def get_(self):
        return self.ui