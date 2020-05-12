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
    
###Sende und Empfangsfunktion über die Serielle Schnittstelle
def WnR (Command, arg1, arg2_n):
    "Kommunikation mit dem Roboter. Enthält das Senden der Kommandos und Empfangen der Daten"
    #print ("Starting Up Serial Monitor")

    try:
        ser.open()
    except Exception as e:
        print ("Exception: Opening serial port: " + str(e))
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

def txtRnW (mode): # und posData
    "Auslesen und abspeichern der Positionen in txt Datei"
    ############# 1 Anzeigen welche Positionen es gibt oder 2 Übertragen der Positionsdaten an den Roboter
    mode = int(mode)
    if mode == 1 or mode == 2:
        infile = open("/home/pi/robo/Ergebnisse.txt", "r")
        for line in infile:
            
            line.rstrip('\n')
            pre, NrPos = line.split(' 0 0 ')
            Nr, Pos = NrPos.split(' ', 1)
            if mode == 1:
                print('Position', Nr, Pos)
                #return 0
            if mode == 2:
                #Command = "LocXyz"
                #arg1 = Nr
                #arg2_n = Pos
                resp = WnR ("LocXyz", Nr, Pos)
                print(resp)
                #return responce
        infile.close()
        return "fertig"
        
    if mode == 3 or mode == 4:
        ############Eingabe welche Position verändert werden soll muss später von außen kommen
        ######## 3 neue Position ist dort wo Roboter steht oder 4 Position wird fein justiert 
        
        if mode == 3:
            newNr = input("Manuell verfahren und Positionsnummer eingeben:\n")
            oneZero = WnR ("HereC", newNr, "")
            recivedStr = WnR ("locXyz", newNr, "")
            #recivedStr = ('1 0 0 %s 40 -444 228 -171 90 -180' %newNr)
            #print(recivedStr)
            #Einlesen und teilen
            pre, NrPos = recivedStr.rstrip('\n').split(' 0 0 ')
            Nr, recivedPos = NrPos.split(' ', 1)
            #print(recivedPos)
        if mode == 4:
            newNr = input("Positionsnummer eingeben:\n")
            posData = input("Position als Koordinaten eingeben (z.b. 40 -444 228 -171 90 -180): ")
            recivedPos = posData

        ############ Eine Position ändern und richtig eintragen
        #outfile = open(fname[:-4] + ".changed", 'w')
        infile = open("/home/pi/robo/Ergebnisse.txt", "r")
        outfile = open ("/home/pi/robo/Ergebnisse.txt", "r+")
        for line in infile:
            #Einlesen und teilen
            pre, NrPos = line.rstrip('\n').split(' 0 0 ')
            Nr, Pos = NrPos.split(' ', 1)
            #Aederung
            if newNr == Nr:
                Pos = recivedPos.ljust(len(Pos))
            #Ersetzen
            outfile.write('1 0 0 %s %s\n' %(Nr, Pos))
            print(Nr, Pos)

        infile.close()
        outfile.close()


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