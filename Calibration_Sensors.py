from ljm1 import Ljm1
import time

Labjack1=Ljm1()

delay = 1
# Depending of the sensor to review

Response_time_pH = 0.9
Reponse_time_DO = 0.6


# Adress for calibration
# pH PBR1 6
# pH PBR2 5 
# pH PBR3 4
# DO PBR1 3
# DO PBR2 2
# DI PBR3 1

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
#comando_PBR = "Cal,high,10"
#comando_PBR = "Cal"

#Labjack1.sendValueI2C([ord(character) for character in comando_PBR], num_bytes_to_read=1, delay=Response_time_pH)

# This is in case of a error in the comunication


#Labjack1.sendValueI2C([ord(character) for character in comando_PBR], num_bytes_to_read=1, delay=0.9)
#time.sleep(delay) 

comando_PBR = "R"
Labjack1.sendValueI2C([ord(character) for character in comando_PBR], num_bytes_to_read=1, delay=0.9)
print(Labjack1.readValueI2C())

Labjack1.close()


