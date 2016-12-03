# Anna Lu
# December 3, 2016
# protocol type: polling

import serial

portAddress = '/dev/ttyUSB0'
timeout = 1 # seconds
baudrate = 19200
port = 'COM1'

def hello(ser, baudrate, timeout):
	# receives helloandInfo input from sensor
	# exchanges only at startup
	# helloandInfo has cmd body of 4 bytes long

    with serial.Serial(portAddress, baudrate, timeout) as ser: # open serial port
        if (ser.isopen):
            print('connected to serial' + ser.name)
            ser.write(b'hello') # write a hello over serial port
            s = ser.read(8) # read up to 8 bytes: start cmd cmd1 cmd2 cmd3 cmd4 checksum end
        else:
            print('error connecting to serial port')
 
# first two bytes: sensor ID number (unique) # next two are version number
# (major and minor) eg. version 1.5, major = 1, minor = 5, limited to 255 or
# 2^8

	# byte 5 and 6 time counter no RTC? time value in two bytes stores
	# unsigned short = 5 bits day, 5 bits hour, 6 bits minute (shift and mask
	# to get values) 
        # verify if we want hour, min, seconds instead
	
	unsigned short timestamp = <some value>; // Bits: DDDDDHHHHHMMMMMM

	int day = (timestamp >> 11) & 0x1F;
	int hour = (timestamp >> 6) & 0x1F;
	int minute = (timestamp) & 0x3F;

def measurementSettings():
    # receives settingsInitialized signal from the sensor
    # parameters initialized to be used throughout

def queryBattery(ser):
    # receives battery status
    

def doMeasurement(ser):
    # receives measurement data, continuous reading
    while (data != None):
        line = ser.readline() # reads a '\n' terminated line         

def Bye():
	# sends a bye, whoever received a bye ends session and replies with bye
	# to acknowledge

## packet body starts with command byte and ends with checksum byte
# label - decimal value - binary value - body length - body byte labels
# hello - 11 - 00001011 - 1 - Byte 1: sender, 0 PDA, 1 Sensor


# checksum
def checksum():
 # sum = cmdbyte + cmdbody1 + cmdbody2 + cmdbody3 + cmdbody4
 # checksum = LSB(sum) -> binary -> decimal
