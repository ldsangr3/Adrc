### Based on A Simple Event-Based PID Controller of Årzén, Karl-Erik 1999

######	Example	#########

#
#p=PID(3.0,0.4,1.2)
#p.setPoint(5.0)
#while True:
#     pid = p.update(measurement_value)
#
#
class PID_Event_Based:
    """
    Discrete PID control
    """
    def __init__(self, P, I, D, Z, Integrator_max=500, Integrator_min=-500):
        
        # PID parameters
        
        self.K=P
        self.Ti=I
        self.Td=D
        self.DeltaTime = Z
                

        self.Integrator_max=Integrator_max
        self.Integrator_min=Integrator_min
       
        # filter coefficient
        self.N = 20
        
        # Initial values
        self.beta=1
        self.y_ast=0.0
        self.y_old=0
        self.error=0.0
        self.up=0.0
        self.ui=0.0
        self.ud=0.0
        
        # precalculated parameters
        self.bi = self.K / self.Ti
        
    def update(self, current_value):
        """
        Calculate PID output value for given reference input and feedback
        """
        self.error = self.y_ast - current_value
        self.ad = self.Td / (self.Td + self.N*self.DeltaTime)
        
        # calculate the control signal
        self.up = self.K*(self.beta*self.y_ast - current_value)
        self.ud = self.ad*self.ud -self.ad*self.K*self.N*(current_value - self.y_old)
               

        # Saturations
        if self.ui > self.Integrator_max:
            self.ui = self.Integrator_max
        elif self.ui < self.Integrator_min:
            self.ui = self.Integrator_min

        PID = self.ud + self.up + self.ui
        
        # Update states
        self.ui = self.ui + self.bi*self.DeltaTime*self.error
        self.y_old = current_value
        
        return PID

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
        return self.K