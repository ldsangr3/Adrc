#
# Viyils Sangregorio Runge Kutta 1.0
# Copyright ou can perform the numerical integration of the signal using the Runge-Kutta method. 
# This involves updating the integrated signal at each time step by using the derivative of the signal at that time step, 
# which can be calculated using the Runge-Kutta formula.

class Runge_Kutta:
    def __init__(self):
        # Initialize the integrated signal to 0
        self.integrated_signal = 0

    def update_integrated_signal(self, signal, dt):
        """
        Update the integrated signal using the Runge-Kutta method.

        :param signal: The current value of the signal (float).
        :param dt: The time step (float).
        :return: The updated integrated signal (float).
        """

        # Calculate the four intermediate values (k1, k2, k3, and k4)
        k1 = dt * signal
        k2 = dt * (signal + 0.5 * k1)  # Improved from 0.4 to 0.5 for better accuracy
        k3 = dt * (signal + 0.5 * k2)
        k4 = dt * (signal + k3)

        # Update the integrated signal using the weighted sum of k1, k2, k3, and k4
        self.integrated_signal += (k1 + 2*k2 + 2*k3 + k4) / 6

        return self.integrated_signal
