import time

### Based on A Simple Event-Based PID Controller of Årzén, Karl-Erik 1999

######	Viyils v 1.0	#########
class PID_Realtime:
    """
    Discrete PID control
    """
    def __init__(self, P, I, D, differetial_on_measurement=True):
        """
        :param proportional_on_measurement: Whether the proportional term should be calculated on
        the input directly rather than on the error (which is the traditional way). Using
        proportional-on-measurement avoids overshoot for some types of systems.
        :param differetial_on_measurement: Whether the differential term should be calculated on
        the input directly rather than on the error (which is the traditional way).
        """
        # PID parameters
        
        self.K=P
        self.Ti=1/I
        self.Td=1/D
        self.differetial_on_measurement=differetial_on_measurement


       
        # filter coefficient
        self.N = 20
        
        # Initial values
        
        self.y_ast=0.0
        self.y_old=0
        self.error=0.0
        self.up=0.0
        self.ui=0.0
        self.ud=0.0
        
        # Get monotonic time to ensure that time deltas are always positive
        self._last_time = time.monotonic()  # Initialize _last_time here
        self._last_input = 0.0
        self._last_error = 0.0

        
    def update(self, current_value):
        """
        #Calculate PID output value for given reference input and feedback
        
        Update the PID controller.

        Call the PID controller with *input_* and calculate and return a control output if
        sample_time seconds has passed since the last update. If no new output is calculated,
        return the previous output instead (or None if no value has been calculated yet).

        :param dt: If set, uses this value for timestep instead of real time. This can be used in
            simulations when simulation time is different from real time.
        """

        now = time.monotonic()
        
        dt = now - self._last_time if (now - self._last_time) != 0 else 1e-16
        
        # Compute error terms
        error = self.y_ast - current_value
        d_input = current_value - self._last_input
        d_error = error - self._last_error

      
        self.up -= self.K * d_input

        # Compute integral and derivative terms
        self.ui += self.Ti * error * dt
        

        if self.differetial_on_measurement:
            self.ud = -self.Td * d_input / dt
        else:
            self.ud = self.Td * d_error / dt

        u_PID = self.up + self.ud + self.ui
           
        # Keep track of state
        
        self._last_input = current_value
        self._last_error = error
        self._last_time = now
        
        # Atuator saturations
        if u_PID >= 100:
            u_PID = 100
        elif u_PID <= 0:
            u_PID = 0
        
        return u_PID

    def setPoint(self,y_ast):
        """
        Initilize the setpoint of PID
        """
        self.y_ast = y_ast

    def setKp(self,K):
        self.K=K

    def setKi(self,Ti):
        self.Ti=Ti

    def setKd(self,Td):
        self.Td=Td

    def getPoint(self):
        return self.y_ast

    def getError(self):
        return self.error

    def getIntegrator(self):
        return self.ui

    def getDerivator(self):
        return self.ud
    
    def getPropotional(self):
        return self.up



