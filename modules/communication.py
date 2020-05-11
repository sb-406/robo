#!/usr/bin/env python
## Communication to robot

# Klasse mit Methoden (Aufruf über self.methode())
class ComRobo():
    'Communication'
    def __init__(self,state = 0, Command = "1 nop\n"):
            self.state = state
            self.Command = Command

    # import time
    

    
    def WnR(self):
        import serial
        ser = serial.Serial(
            port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
            baudrate = 115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1
            )
        # Teilen und senden
        for char in self.Command:
            ser.write(char.encode())
            #print(char, '\n')
        #ser.write(encode("\n"))
        # Empfangen
        s = ""
        while True:
            ch = ser.read().decode()
            s += ch
            #if ch == '\r':
            #    return s
            if ch == '\n':
                return s
   
"""
    def readLine(port):
        s = ""
        while True:
            ch = port.read()
            s += ch
            #if ch == '\r':
            #    return s
            if ch == '\n':
                return s

    def writeLine(Command):
        # Teilen
        for char in Command:
            ser.write(char)
            #print(char, '\n')
        return 0
"""

"""
    def propagate(self):
        if self.state == 0:
            self.f0()
            self.state = 1
        elif self.state == 1:
            self.f1()
            self.state = 2
        elif self.state == 2:
            self.f2()
            self.state = 0

    def f0(self):
        print("f0")

    def f1(self):
        print("f1")

    def f2(self):
        print("f2")



)
#####################################################################
##############Programm mit Roboter IO und IR Sensor##################

counter=0
print ("starting")
#time.sleep(1)
time.sleep(0.5)
ser.write('1 wherec \n')
time.sleep(2)
print("Hier")
rcvStandort = readLine(ser)
#print ("received Standort:"), rcvStandort
time.sleep(0.5)
#print ("sending attach")
ser.write('1 attach 1\n')
time.sleep(1)
rcvattach = readLine(ser)
print ("received attach:", rcvattach)
time.sleep(0.5)
#print ("sending Profile")
ser.write('1 Profile 1\n')
time.sleep(1)
rcvProfil = readLine(ser)
print ("received Profil:", rcvProfil)
time.sleep(0.5)
"""