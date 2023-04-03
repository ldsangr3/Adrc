from labjack import ljm
import time


class Ljm1:
    def __init__(self):
        self.handle = ''
        try:
            self.handle = ljm.openS('ANY', 'ANY', '470019827')
        except:
            print('Connection error')

    def readValue(self, name):
        res = ljm.eReadName(self.handle, name)
        return res

    def sendValue(self, name, value):
        res = ljm.eWriteName(self.handle, name, value=value)

    def initI2C(self, sda, scl, addr, speed=65516):
        # Set the digital I/O line number for the I2C data line (SDA) on the LabJack device
        ljm.eWriteName(self.handle, "I2C_SDA_DIONUM", sda)

        # Set the digital I/O line number for the I2C clock line (SCL) on the LabJack device
        ljm.eWriteName(self.handle, "I2C_SCL_DIONUM", scl)

        # Set the I2C communication speed by configuring the speed throttle value
        # The value 65516 corresponds to a speed of approximately 100 kHz (standard I2C speed)
        ljm.eWriteName(self.handle, "I2C_SPEED_THROTTLE", speed)

        # Set the I2C options for the LabJack device
        # The value 0 means that no special options are selected
        ljm.eWriteName(self.handle, "I2C_OPTIONS", 0)

        # Set the I2C slave address for the device you want to communicate with
        # The variable addr should contain the 7-bit or 10-bit I2C address of the target device
        ljm.eWriteName(self.handle, "I2C_SLAVE_ADDRESS", addr)

          
    def sendValueI2C(self, data, num_bytes_to_read=0, delay=0):
        aBytes = data
        numBytes = len(aBytes)
    
        # Write the number of bytes to transmit
        ljm.eWriteName(self.handle, "I2C_NUM_BYTES_TX", numBytes)
    
        # Set the number of bytes to receive
        ljm.eWriteName(self.handle, "I2C_NUM_BYTES_RX", num_bytes_to_read)
    
        # Write the data to be transmitted
        ljm.eWriteNameByteArray(self.handle, "I2C_DATA_TX", numBytes, aBytes)
    
        # Start the I2C communication
        ljm.eWriteName(self.handle, "I2C_GO", 1)

        # Introduce a delay if specified
        if delay > 0:
            time.sleep(delay)
        
                   
        # Read the received data if there is any
        if num_bytes_to_read > 0:
            # Read the received data (ACK)
            numAcks = ljm.eReadNameByteArray(self.handle, "I2C_ACKS", num_bytes_to_read)
            return numAcks
        else:
            return None


    def readValueI2C(self):
        # Do a read only transaction to obtain the readings
        numBytes = 6
        ljm.eWriteName(self.handle, "I2C_NUM_BYTES_TX", 0) # Set the number of bytes to transmit
        ljm.eWriteName(self.handle, "I2C_NUM_BYTES_RX", numBytes) # Set the number of bytes to receive
        ljm.eWriteName(self.handle, "I2C_GO", 1)  # Do the I2C communications.
        

        aBytes = ljm.eReadNameByteArray(self.handle, "I2C_DATA_RX", numBytes)
        resp = ''
        for i in aBytes:
            if (i > 1 and i < 255):
                resp = resp + ''.join(chr(i))
        if (resp == ''):
            return 0
        return (resp)
    
    def readMaxI2CEZO(self):
        # Do a read only transaction to obtain the readings
        numBytes = 18
        ljm.eWriteName(self.handle, "I2C_NUM_BYTES_TX", 0) # Set the number of bytes to transmit
        ljm.eWriteName(self.handle, "I2C_NUM_BYTES_RX", numBytes) # Set the number of bytes to receive
        ljm.eWriteName(self.handle, "I2C_GO", 1)  # Do the I2C communications.
        

        aBytes = ljm.eReadNameByteArray(self.handle, "I2C_DATA_RX", numBytes)
        resp = ''
        for i in aBytes:
            if (i > 1 and i < 255):
                resp = resp + ''.join(chr(i))
        if (resp == ''):
            return 0
        return (resp)


    def initUART(self, tx, rx):
        ljm.eWriteName(self.handle, "ASYNCH_ENABLE", 0)
        ljm.eWriteName(self.handle, "ASYNCH_TX_DIONUM", tx)
        ljm.eWriteName(self.handle, "ASYNCH_RX_DIONUM", rx)
        ljm.eWriteName(self.handle, "ASYNCH_BAUD", 9600)
        ljm.eWriteName(self.handle, "ASYNCH_RX_BUFFER_SIZE_BYTES", 10)
        ljm.eWriteName(self.handle, "ASYNCH_NUM_DATA_BITS", 8)
        ljm.eWriteName(self.handle, "ASYNCH_NUM_STOP_BITS", 1)
        ljm.eWriteName(self.handle, "ASYNCH_PARITY", 0)
        ljm.eWriteName(self.handle, "ASYNCH_ENABLE", 1)

    def sendValueUART(self, data):
        for i in data:
            print(i)
            ljm.eWriteName(self.handle, "ASYNCH_TX_GO", 0)
            ljm.eWriteName(self.handle, "ASYNCH_NUM_BYTES_TX", 1)
            ljm.eWriteName(self.handle, "ASYNCH_DATA_TX", i)
            ljm.eWriteName(self.handle, "ASYNCH_TX_GO", 1)

    def readValueUART(self):
        # Remember to put the time.sleep to call this method until the rx buffer is full
        rxBytes = ljm.eReadName(self.handle, "ASYNCH_NUM_BYTES_RX")
        data = []
        cont = 0
        if (rxBytes > 0):
            while cont < int(rxBytes):
                bt = ljm.eReadName(self.handle, "ASYNCH_DATA_RX")
                data.append(chr(int(bt)))
                cont = cont + 1
        return data
    
    def close(self):
        self.handle = ljm.close(self.handle)
        
