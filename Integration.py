import numpy as np

#
# Viyils Sangregorio Runge Kutta 1.0
# Copyright ou can perform the numerical integration of the signal using the Runge-Kutta method. 
# This involves updating the integrated signal at each time step by using the derivative of the signal at that time step, 
# which can be calculated using the Runge-Kutta formula.

class Runge_Kutta:
    def __init__(self):
        self.integrated_signal = 0
    def update_integrated_signal(self, signal, dt):
        k1 = dt * signal
        k2 = dt * (signal + 0.4 * k1)
        k3 = dt * (signal + 0.5 * k2)
        k4 = dt * (signal + k3)
        self.integrated_signal += (k1 + 2*k2 + 2*k3 + k4) / 6
        return self.integrated_signal

    
    
