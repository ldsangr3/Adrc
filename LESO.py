from math import *
from Integration import Runge_Kutta

class LESO:
    def __init__(self, k1=30, k2=200, k3=800, x1_init=0, x2_init=0, x3_init=0):
        self.x1 = x1_init  # State x1 initial value
        self.x2 = x2_init  # State x2 initial value
        self.x3 = x3_init  # State x3 initial value (representing the disturbance)
        self.k1 = k1       # Observer gain for x1
        self.k2 = k2       # Observer gain for x2
        self.k3 = k3       # Observer gain for x3
        
        self.inte_x1 = Runge_Kutta() # Is the estimation of the output
        self.inte_x2 = Runge_Kutta()
        self.inte_x3 = Runge_Kutta()

    def update_observer(self, y, v, dt):
        """
        Update the observer with the output y and control input u, with time step dt.
        :param y: plant output.
        :param v: is the auxiliary control law.
        :param alpha: controller parameter.
        :param lambda: observer parameter.
        :return: control input u, state estimates x1, and x2.
        """
        
        e = y - self.x1
        x1_dot = v + self.x2 + self.k1 * e
        x2_dot = self.x3 + self.k2 * e
        x3_dot = self.k3 * e

        self.x1 = self.inte_x1.update_integrated_signal(signal=x1_dot, dt=dt)
        self.x2 = self.inte_x2.update_integrated_signal(signal=x2_dot, dt=dt)
        self.x3 = self.inte_x3.update_integrated_signal(signal=x3_dot, dt=dt)
        
        # updating variables names
        xi=self.x2
        
        return xi

    def get_estimates(self):
        return self.x1, self.x2, self.x3
    
    def reset_LESO(self):
        self.x1=0
        self.x2=0
        self.x3=0

