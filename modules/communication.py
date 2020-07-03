#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Communication to robot
# Purpose:
#
# Author:      Simon Bohn Bachelorarbeit 
#
# Created:     12.04.2020
# Links:       https://stackoverflow.com/questions/45411924/python3-two-way-serial-communication-reading-in-data 12.05.2020 Grundlage für WnR Funktion
#
#
# Funktionen:  WnR(), txtRnW(), WaitforEom()
#-------------------------------------------------------------------------------

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
#############################################################################################    
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
##########################################################################################################
def txtRnW (mode): # und posData
    "Auslesen und abspeichern der Positionen in txt Datei"
    ############# 1 Anzeigen welche Positionen es gibt oder 2 Übertragen der Positionsdaten an den Roboter
    mode = int(mode)
    if mode == 1 or mode == 2:
        infile = open("/home/pi/robo/txtfiles/ArchiviertePositionen.txt", "r")
        for line in infile:
            
            line.rstrip('\n')
            pre, NrPos = line.split(' 0 0 ')
            Nr, Pos = NrPos.split(' ', 1)
            if mode == 1:
                print('Position', Nr, Pos)
                #return 0
            if mode == 2:
                print('Position', Nr, Pos)
                #Command = "LocXyz"
                #arg1 = Nr
                #arg2_n = Pos
                resp = WnR ("LocXyz", Nr, Pos)
                #print(resp)
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
            WnR("locXyz", newNr, posData)#neu direkt an Roboter übertragen
            recivedPos = posData

        ############ Eine Position ändern und richtig eintragen
        #outfile = open(fname[:-4] + ".changed", 'w')
        infile = open("/home/pi/robo/txtfiles/ArchiviertePositionen.txt", "r")
        outfile = open ("/home/pi/robo/txtfiles/ArchiviertePositionen.txt", "r+")
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


########################################################################################
def WaitforEom():
        responce = ""
        while responce!= "1 0\r\n":
            responce = WnR("waitForEom", "", "")
            #print (responce)
        print (responce)
########################################################################################
def getTemp():
    import sys

    # Systempfad zum den Sensor, weitere Systempfade könnten über ein Array
    # oder weiteren Variablen hier hinzugefügt werden.
    # 28-02161f5a48ee müsst ihr durch die eures Sensors ersetzen!
    sensor = '/sys/bus/w1/devices/28-011939d24992/w1_slave'

    def readTempSensor(sensorName) :
        """Aus dem Systembus lese ich die Temperatur der DS18B20 aus."""
        f = open(sensorName, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def readTempLines(sensorName) :
        lines = readTempSensor(sensorName)
        # Solange nicht die Daten gelesen werden konnten, bin ich hier in einer Endlosschleife
        # ['54 01 4b 46 7f ff 0c 10 fd : crc=fd YES\n', '54 01 4b 46 7f ff 0c 10 fd t=21250\n']
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = readTempSensor(sensorName)
        temperaturStr = lines[1].find('t=')
        # Ich überprüfe ob die Temperatur gefunden wurde.
        if temperaturStr != -1 :
            tempData = lines[1][temperaturStr+2:]
            tempCelsius = float(tempData) / 1000.0
            tempKelvin = 273 + float(tempData) / 1000
            tempFahrenheit = float(tempData) / 1000 * 9.0 / 5.0 + 32.0
            # Rückgabe als Array - [0] tempCelsius => Celsius...
            return [tempCelsius, tempKelvin, tempFahrenheit]

    try:
        #while True :
            # Mit einem Timestamp versehe ich meine Messung und lasse mir diese in der Console ausgeben.
            #print("Temperatur um " + time.strftime('%H:%M:%S') +" drinnen: " + str(readTempLines(sensor)[0]) + " °C")
        print("Temperatur:"+ str(readTempLines(sensor)[0]))

            # Nach 10 Sekunden erfolgt die nächste Messung
            #time.sleep(10)
    except KeyboardInterrupt:
        # Programm wird beendet wenn CTRL+C gedrückt wird.
        print('Temperaturmessung wird beendet')
    except Exception as e:
        print(str(e))
        sys.exit(1)
    #finally:
        # Das Programm wird hier beendet, sodass kein Fehler in die Console geschrieben wird.
        #print('Programm wird beendet.')
        #sys.exit(0)
########################################################################################
"""
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
"""
#####################################################################
##############Programm mit Roboter IO und IR Sensor##################
"""
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