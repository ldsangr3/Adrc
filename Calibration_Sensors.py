from ljm1 import Ljm1
import time

Labjack1=Ljm1()

delay = 1
# Depending of the sensor to review

Response_time_pH = 0.9
Reponse_time_DO = 0.6
Response_time_Ezo = 0.3


# Adress for calibration
# pH PBR1 6
# pH PBR2 5 
# pH PBR3 4
# DO PBR1 3
# DO PBR2 2
# DO PBR3 1
# PMP PBR1 8 Din
# PMP PBR2 10 Din
# PMP PBR3 12 Din
# PMP level PBR1 7
# PMP level PBR2 9
# PMP level PBR3 11



# DO commands

# R simple read
# DO sensores
# Cal calibrate to atmospheric oxygen levels
# Cal,0 calibrate device to 0 dissolved oxygen
# Cal,clear delete calibration data
# Cal,? device calibrated?
# T,25 Temperature compensation
# P,74.66 Atmospheric pressure compensation, bogotá 74.6567Kilopasca


# pH commands
# Cal,mid,7 single point calibration at midpoint
# Cal,low,4 two point calibration at lowpoint
# Cal,high,10 three point calibration at highpoint
# Cal,clear delete calibration data
# Cal,? device calibrated?


Labjack1.initI2C(1, 0, 3) #Adress 
#comando_PBR = "Cal,low,4"
#comando_PBR = "Cal"

#Labjack1.sendValueI2C([ord(character) for character in comando_PBR], num_bytes_to_read=1, delay=Response_time_pH)




#Labjack1.sendValueI2C([ord(character) for character in comando_PBR], num_bytes_to_read=1, delay=0.9)
#time.sleep(delay) 
Flag_PMPs=False
# For PH and DO
if Flag_PMPs==False:
    comando_PBR = "R"
    Labjack1.sendValueI2C([ord(character) for character in comando_PBR], num_bytes_to_read=1, delay=0.9)
    print(Labjack1.readValueI2C())


# Calibration PMPs
if Flag_PMPs==True:
    #Labjack1.sendValueI2C([88], num_bytes_to_read=1, delay=Response_time_Ezo) # X
    Labjack1.sendValueI2C([ord(character) for character in "D," +  str(25) ], num_bytes_to_read=1, delay=Response_time_Ezo)
    #Labjack1.sendValueI2C([ord(character) for character in "Cal," +  str(39)], num_bytes_to_read=1, delay=Response_time_Ezo)
    #Cal,9.8


Labjack1.close()