from ljm1 import Ljm1
import numpy as np

Labjack1=Ljm1()
Labjack1.sendValue('EIO0', False)  
#PBR2
Labjack1.sendValue('EIO4', False)  
#PBR3
Labjack1.sendValue('EIO6', False)
Labjack1.sendValue('TDAC3', np.interp(300, [0, 500], [3, 5])) # Interp
      
Labjack1.sendValue('TDAC4', np.interp(200, [0, 500], [3, 5])) # Interp
        
Labjack1.sendValue('TDAC5', np.interp(150, [0, 500], [3, 5])) # Interp
    
    
Labjack1.close()

