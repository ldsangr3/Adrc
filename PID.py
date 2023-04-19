### Based on A Simple Event-Based PID Controller of Årzén, Karl-Erik 1999

######	Viyils v 1.0	#########


class PID_Event_Based:
    """
    Discrete PID control
    """
    def __init__(self, P, I, D, Z):
        
        # PID parameters
        
        self.K=P
        self.Ti=I
        self.Td=D
        self.DeltaTime = Z
                

       
        # filter coefficient
        self.N = 20
        
        # Initial values
        
        self.y_ast=0.0
        self.y_old=0
        self.error=0.0
        self.up=0.0
        self.ui=0.0
        self.ud=0.0
        
        # precalculated parameters
        self.bi = (self.K*Z) / self.Ti
        self.ad = self.Td/(self.Td+self.N*Z)
        self.bd = self.K*self.Td*self.N / (self.Td+self.N*Z)
        
    def update(self, current_value):
        """
        #Calculate PID output value for given reference input and feedback
        """
        
        #calculated coefficients
        
        
        self.error = self.y_ast - current_value
        
        
        # calculate the control signal
        self.up = self.K*self.error
        self.ud = self.ad*self.ud - self.bd*(current_value - self.y_old)
   
        # Control signal
        u_PID = self.ud + self.up + self.ui
        
        # Atuator saturations
        if u_PID >= 100:
            u_PID = 100
        elif u_PID <= 0:
            u_PID = 0

            
        # Update states
        self.ui = self.ui + self.bi*self.error
        self.y_old = current_value
        
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


