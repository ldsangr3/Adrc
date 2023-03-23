### Based on A Simple Event-Based PID Controller of Årzén, Karl-Erik 1999

######	Viyils v 1.0	#########


class PID_Event_Based:
    """
    Discrete PID control
    """
    def __init__(self, P, I, D, Z, Beta, Integrator_max=1000, Integrator_min=-1000):
        
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
        self.beta=Beta
        self.y_ast=0.0
        self.y_old=0
        self.error=0.0
        self.up=0.0
        self.ui=0.0
        self.ud=0.0
        
        # precalculated parameters
        self.bi = self.K*Z / self.Ti
        self.ad = self.Td/(self.Td+self.N*Z)
        self.bd = self.K*self.Td*self.N / (self.Td+self.N*Z)
        
    def update(self, current_value):
        """
        #Calculate PID output value for given reference input and feedback
        """
        
        #calculated coefficients
        
        
        self.error = self.y_ast - current_value
        
        
        # calculate the control signal
        self.up = self.K*(self.beta*self.y_ast - current_value)
        self.ud = self.ad*self.ud - self.bd*(current_value - self.y_old)
               

        # Saturations
        if self.ui > self.Integrator_max:
            self.ui = self.Integrator_max
        elif self.ui < self.Integrator_min:
            self.ui = self.Integrator_min
    
        
        # Control signal
        PID = self.ud + self.up + self.ui
        
        # Atuator saturations
        if PID>=1000:
            PID=1000
        if PID <=0:
            PID=-1000    
            
        # Update states
        self.ui = self.ui + self.bi*self.error
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
    