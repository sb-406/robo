#!/usr/bin/env python
import time
import serial
#port = "/dev/ttyAMA0"  # Raspberry Pi 2
#port = "/dev/ttyS0"    # Raspberry Pi 3

def readLine(port):
    s = ""
    while True:
        ch = port.read()
        s += ch
        if ch == '\r':
            return s
        if ch == '\n':
            return s

ser = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
###################################################
print ("starting")
time.sleep(1)
#Positionsnummer = 4
NumStr= input("Manuell verfahren")
Positionsnummer = int(NumStr)
rcvPos = readLine(ser)
ser.write('1 HereC %d\n' %Positionsnummer)
time.sleep(0.5)
rcvPos = readLine(ser)
print ("received Pos:", rcvPos)
ser.write('1 locXyz %d\n' %Positionsnummer)
time.sleep(0.5)
rcvaktuell = readLine(ser)
print ("received aktuelle Position%d:"%Positionsnummer, rcvaktuell)


