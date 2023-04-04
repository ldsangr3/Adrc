#ADRC
# This class implemented the ADRC controller 
# u is the control signal
# y is the output
# L1 and L2 are the gains of the observer

from math import *
from Integration import Runge_Kutta
from LESO import LESO

class ADRC:
    def __init__(self, mu_max=2, plant_output=0, y_stimation=0, Control_singal_U=0, estimated_disturbance=0):
        
        # Initial conditions
        
        self.e_xi = estimated_disturbance  # Initial disturbance
        self.Control_singal = Control_singal_U  # Initial control signal
        self.plant_output = plant_output  # Initial output
        self.y_stimation = y_stimation  # State estimation
        self.mu_max=mu_max # maximal dilution rate
        self.integral = 0  # State estimation

 

    def reset_controller(self):
        # Reset the controller's state
        self.e_xi = 0  # Initial disturbance
        self.Control_singal = 0  # Initial control signal
        self.plant_output = 0  # Initial output
        self.y_stimation = 0  # State estimation
        self.integral = 0  # State estimation
        
        # Create the observer instance
        self.Observer = LESO()

    def ComputeADRC(self, setpoint, y, K, dt):
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
        e = K*(y - y_ast) 
        # Compute de auxiliary Control law
        v = - e - self.e_xi
        restricted_v = min(v, 0)  # Restricts the signal to be 0 or negative
        
        
        # Call the observer 
        self.e_xi=self.Observer.update_observer(y=y,v=restricted_v, dt=dt)
        
        D = - v / y
        self.restricted_D = max(min(D, self.mu_max), 0)
        return self.restricted_D 

    def get_D(self):
        return self.restricted_D


