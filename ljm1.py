from labjack import ljm


class Ljm1:
    def __init__(self):
        self.handle = ''
        data=[]
        try:
            #self.handle = ljm.openS('ANY', 'ANY', 'ANY')
            #self.handle = ljm.openS('ANY', 'ANY', '470019870')
            self.handle = ljm.openS('ANY', 'ANY', '470019827')
        except:
            print('Connection error')

    def readValue(self, name):
        res = ljm.eReadName(self.handle, name)
        return res

    def sendValue(self, name, value):
        res = ljm.eWriteName(self.handle, name, value=value)

    def initI2C(self, sda, scl, addr):
        ljm.eWriteName(self.handle, "I2C_SDA_DIONUM", sda)
        ljm.eWriteName(self.handle, "I2C_SCL_DIONUM", scl)
        ljm.eWriteName(self.handle, "I2C_SPEED_THROTTLE", 65516)
        ljm.eWriteName(self.handle, "I2C_OPTIONS", 0)
        ljm.eWriteName(self.handle, "I2C_SLAVE_ADDRESS", addr)

##    def sendValueI2C(self, data):
##        aBytes = [data]
##        numBytes = len(aBytes)
##        ljm.eWriteName(self.handle, "I2C_NUM_BYTES_TX", numBytes)
##        ljm.eWriteName(self.handle, "I2C_NUM_BYTES_RX", 0)
##
##        ljm.eWriteNameByteArray(self.handle, "I2C_DATA_TX", numBytes, aBytes)
##        ljm.eWriteName(self.handle, "I2C_GO", 1)

##    def sendValueI2C(self, data):
##        for ch in data:
##            valor=int(ord(ch))
##            aBytes = [68,44,valor]
##            numBytes = len(aBytes)
##            ljm.eWriteName(self.handle, "I2C_NUM_BYTES_TX", numBytes)
##            ljm.eWriteName(self.handle, "I2C_NUM_BYTES_RX", 0)
##        
##            ljm.eWriteNameByteArray(self.handle, "I2C_DATA_TX", numBytes, aBytes)
##            ljm.eWriteName(self.handle, "I2C_GO", 1)


##    def sendValueI2C(self, data):             
##        valor=int(ord(data))
##        aBytes = [68,44,valor]
##        numBytes = len(aBytes)
##        ljm.eWriteName(self.handle, "I2C_NUM_BYTES_TX", numBytes)
##        ljm.eWriteName(self.handle, "I2C_NUM_BYTES_RX", 0)
##        ljm.eWriteNameByteArray(self.handle, "I2C_DATA_TX", numBytes, aBytes)
##        ljm.eWriteName(self.handle, "I2C_GO", 1)


    def sendValueI2C(self, data):             
        aBytes = data
        numBytes = len(aBytes)
        ljm.eWriteName(self.handle, "I2C_NUM_BYTES_TX", numBytes)
        ljm.eWriteName(self.handle, "I2C_NUM_BYTES_RX", 0)
        ljm.eWriteNameByteArray(self.handle, "I2C_DATA_TX", numBytes, aBytes)
        ljm.eWriteName(self.handle, "I2C_GO", 1)
            

    def readValueI2C(self):
        numBytes = 6
        ljm.eWriteName(self.handle, "I2C_NUM_BYTES_TX", 0)
        ljm.eWriteName(self.handle, "I2C_NUM_BYTES_RX", numBytes)
        aBytes = ljm.eReadNameByteArray(self.handle, "I2C_DATA_RX", numBytes)
        ljm.eWriteName(self.handle, "I2C_GO", 1)
        resp = ''
        for i in aBytes:
            if (i > 1 and i < 255):
                resp = resp + ''.join(chr(i))
        if (resp == ''):
            return 0
        return  (resp) # float(resp)

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
