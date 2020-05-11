#!/usr/bin/env python
## Communication to robot
import time
import serial
ser = serial.Serial(
    port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
    baudrate = 115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
    )
    
###Funktion
def WnR (Command, arg1, arg2_n):
    "Kommunikation mit dem Roboter. Enthält das Senden der Kommandos und Empfangen der Daten"
    #print ("Starting Up Serial Monitor")

    try:
        ser.open()
    except Exception as e:
        #print ("Exception: Opening serial port: " + str(e))

    if ser.isOpen():
        try:
            ser.flushInput()
            ser.flushOutput()
            #Command= input("Kommando eingeben:")
            #arg1= input("Argument 1 eingeben:")
            #arg2_n= input("Argument 2 bis n eingeben:")
            string = ("1 %s %s %s\n" % (Command, arg1, arg2_n))
            ser.write(string.encode('ascii'))
            #print(string)
            time.sleep(0.5)
            numberOfLine = 0
            while True:
                response = ser.readline().decode('ascii')
                #print("read data: " + response)
                numberOfLine = numberOfLine + 1
                if (numberOfLine >= 1):
                    break
            ser.close()
        except Exception as e:
            print ("Error communicating...: " + str(e))
    else:
        print ("Cannot open serial port.")
    return response



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