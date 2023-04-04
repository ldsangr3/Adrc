import numpy as np
from Integration import Runge_Kutta

class Model_Microalgae:
    def __init__(self, D=0, X=0, Q=0, S=0):
        self.D = D
        self.X = X
        self.Q = Q
        self.S = S
        self.rk_instance_X = Runge_Kutta(X)
        self.rk_instance_Q = Runge_Kutta(Q)
        self.rk_instance_S = Runge_Kutta(S)
    
    def update_tertiolecta(self, D, dt):
        # Parameters [Bennatia, Tebbani, Dumur]
        mu_ = 2          # maximal growth rate (day−1)
        rho_m = 9.2      # maximal specific uptake rate
        K_q = 1.8        # minimal cell quota allowing growth
        K_s = 0.105      # Half substrate constant (g N me^-3)
        K_sI = 150       # Light saturation
        K_iI = 2000      # Inhibition coefficient (mol m^-2 se1)
        S_in = 100       # % 120   %he input substrate concentration (μmol L−1) 80-120% Experiment selection for the discrimination of semi-quantitative models of dynamical systems 

        I_opt = np.sqrt(K_sI * K_iI)  # The optimal light intensity
        mu_I = I_opt / (I_opt + K_sI + (I_opt**2) / K_iI)

        mu = mu_ * (1 - K_q / self.Q) * mu_I
        rho = rho_m * self.S / (self.S + K_s)

        dX = mu * self.X - D * self.X
        dQ = rho - mu * self.Q
        dS = (S_in - self.S) * D - rho * self.X

        # Update X using the Runge-Kutta integration method
        self.X = max(self.rk_instance_X.update_integrated_signal(dX, dt), 0)
        self.Q = max(self.rk_instance_Q.update_integrated_signal(dQ, dt), 0)
        self.S = max(self.rk_instance_S.update_integrated_signal(dS, dt), 0)


        return self.X, self.Q, self.S






