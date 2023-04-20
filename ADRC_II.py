#ADRC
# This class implemented the ADRC controller 
# u is the control signal
# y is the output
# L1 and L2 are the gains of the observer

from math import *
from Integration import Runge_Kutta
from LESO_II import LESO

class ADRC_II:
    def __init__(self, plant_output=0, y_stimation=0, Control_singal_U=0, estimated_disturbance=0):
        
        # Initial conditions
        
        self.e_xi = estimated_disturbance  # Initial disturbance
        self.Control_singal = Control_singal_U  # Initial control signal
        self.plant_output = plant_output  # Initial output
        self.y_stimation = y_stimation  # State estimation
        self.integral = 0  # State estimation
        
        
        # Create the observer instance
        self.Observer = LESO()
        self.Z1 = 0 
        self.Z2 = 0 
        self.Z3 = 0  
 

    def reset_controller(self):
        # Reset the controller's state
        self.Z1 = 0 
        self.Z2 = 0 
        self.Z3 = 0  
        self.Control_singal = 0  # Initial control signal
        self.plant_output = 0  # Initial output
        
        
        
     

    def ComputeADRC(self, setpoint, y, Kp, Kd, dt):
        """
        Define the function for the ADRC controller.

        :param y: plant output.
        :param u: control input.
        :param alpha: controller parameter.
        :param lambda_: observer parameter.
        :param beta: controller parameter.
        :return: control input u, state estimates x1, and x2.
        """
        y_ast = setpoint
        # Calculate the error
        e = Kp*(y_ast - self.Z1) 
        # Compute de auxiliary Control law
        Control_U = e - Kd*self.Z2 - self.Z3
        
        
        # Call the observer 
        self.Z1, self.Z2, self.Z3 =self.Observer.update_observer(y=y,v=Control_U, dt=dt)
        

        return Control_U



