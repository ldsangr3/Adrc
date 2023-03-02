from Integration import Runge_Kutta
import time


class Main():
    Integral = Runge_Kutta()
    i=0
    while True:
        Integrated = Integral.update_integrated_signal(signal=0.5,dt=0.1)
        i+=1
        time.sleep(0.1)
        print("The Integral is", i*0.1, Integrated)
        
