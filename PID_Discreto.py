### Based on A Simple Event-Based PID Controller of Årzén, Karl-Erik 1999

######	Viyils v 1.0	#########


class PID_Discreto:
    """
    Discrete PID control
    """
    def __init__(self, P=0.588442472894726, I=0.00582245726162423, D=-313.988863983634, Z=120):
        
        # PID parameters
        
        self.K=P
        self.Ti=1/I
        self.Td=1/D
        self.DeltaTime = Z
                

       
        # filter coefficient
        self.N = 0.00187408707885066
        
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
        if u_PID >= 1000:
            u_PID = 1000
        elif u_PID <= 0:
            u_PID = 0

            
        # Update states
        self.ui = self.ui + self.bi*self.error
        self.y_old = current_value
        
        return u_PID
    
    def reset(self):
        self.up=0.0
        self.ui=0.0
        self.ud=0.0
        print("Controller resetted")

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


