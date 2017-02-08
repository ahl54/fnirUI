import serial



class ICP(object):

    def __init__(self):
        
        self.portAddress = '/dev/ttyUSB0'
        self.timeout = 1 # seconds
        self.buadrate = 9600
        self.port = 'COM2'
        self.ser = serial.Serial()
        self.ser.buadrate = self.buadrate;
        self.ser.port = self.port;
        self.ser.timeout = self.timeout;
        self.serCon = 0

        try:
            self.ser.open()
            self.serCon = 1
        except serial.SerialException as e:
            print('Error connecting to serial')
    
    def packetSend(self, command, commandBody):
    	#sends a packet containing input command with command body
    
        self.ser.write(bytes([170]))
        self.ser.write(bytes([command]))
        if ((commandBody is None)==0):
            self.ser.write(bytes(commandBody))
        chksum = self.calcChksum(command,commandBody)
        self.ser.write(chksum)
        self.ser.write(bytes([81]))
    	
    def packetReceive(self, numBytes):
        commandBody = []
    	#receive a packet from sensor
        if(self.ser.read()!=bytes([170])):
            self.ser.reset_input_buffer()
            self.resend()
        else:
            command = self.ser.read()
            s = self.ser.read(numBytes-2)
            if (s(-1)==bytes([81])):
                del s[-1]
                chksum = s(-1)
                del s[-1]
                if(self.chkChksum(s,chksum)==0):
                    self.ser.reset_input_buffer()
                    self.resend()
                    return self.packetReceive(numBytes)
                else:
                    if(range(s)>2):
                        commandBody = s[0:range(s)-2]
                    else:
                        comandBody = None
                    return (command, commandBody)
            else:
                self.ser.reset_input_buffer()
                self.resend()
                return self.packetReceive(numBytes)
    
    
    def sayHello(self):
        
        self.packetSend(11,[0])
        (com,comBod) = self.packetReceive(11)
        if(com!=bytes([12])):
            return false
        self.sensorID = int(comBod[0:1])
        self.sensorVer = long(comBod[2:3])
        self.tc = int(comBod[4:5])
        self.channels = int(comBod[6]) 
        return true;
    
    def measSettings(self,LP,ADG,FDG,PN):
        settings = [LP,ADG,FDG,PN]
        self.packetSend(bytes([15]),bytes(settings))
        tmp = self.packetReceive(4)
        if (tmp==18):
            print('Settings not initialized')
            return
        else:
            print('Settings initialized')
            return
    
    def pollData(self,numChannels):
    
        self.packetSend(21,None)
        (com,comBod) = self.packetReceive(8+channels*12)
        data = list();
        while(com!=bytes([26])):
            self.ser.reset_input_buffer()
            self.resend()
            (com,comBod) = self.packetReceive(8+channels*12)
        for i in range(comBod,2):
            data.append(unpack('h',comBod[i:i+1]))
        return data
    
    
    def queryBattery(self):
        # receives battery status
        self.packetSend(65,None)
        (com,comBod) = self.packetReceive(5)
        while(com!=bytes([66])):
            self.ser.reset_input_buffer()
            self.resend(self)
            (com,comBod) = self.packetReceive(5)
        return unpack('b',comBod)
    
    
    def sayBye(self):
    	# sends a bye, whoever received a bye ends session and replies with bye
    	# to acknowledge
        self.packetSend(42,None)
        
    
    def calcChksum(self,com,comBod):
     # sum = cmdbyte + cmdbody1 + cmdbody2 + cmdbody3 + cmdbody4
     # checksum = LSB(sum) -> binary -> decimal
        
        total = 0
        if((comBod is None)==0):
            for num in comBod:
                total += num
        total += com
        if(total>255):
            a= bin(total)
            b= a[-8:]
            return int(b,2)
        else:
            return bytes([total])
        
    
    
    def chkChksum(self,s,chksumi):
    
        total = 0
        for c in s:
            total += c
        if(total>255):
            a= bin(total)
            b= a[-8:]
            chksum = int(b,2)
        else:
            chksum = bytes([total])
        return chksumi==chksum
    
    def resend(self):
        self.packetSend(36,None)
    
    
    
    
    
    
    
    















































