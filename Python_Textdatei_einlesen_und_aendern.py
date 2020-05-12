
#!/usr/bin/env python
"""
import time
import serial

def readLine(port):
    s = ""
    while True:
        ch = port.read()
        s += ch
        #if ch == '\r':
        #    return s
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
print('Positionsnummer = 0')
#rcv0 = readLine(ser)
file = open("/home/pi/robo/txtfiles/Positionen-kartesisch.txt", "a")
file.write("\n--------------------------------\n")
zeit = time.time()
file.write(time.strftime('%Y-%m-%d %H:%M:%S\n', time.localtime(zeit)))

Positionsnummer = 0
while Positionsnummer < 8:
    NumStr= input("Manuell verfahren und Positionsnummer eingeben:\n")
    #Positionsnummer = int(NumStr)
    Positionsnummer = NumStr
    ser.write("1 HereC %d\n" %Positionsnummer)
    print("1 HereC %d\n" %Positionsnummer)
    #time.sleep(0.5)
    rcv = readLine(ser)
    print ("received Pos:", rcv)
    ser.write('1 locXyz %d\n' %Positionsnummer)
    time.sleep(0.5)
    rcvaktuell = readLine(ser)
    print ("received aktuelle Position%d:" %Positionsnummer, rcvaktuell)
    
"""

"""
import time
file = open("F:/Hauptordner/Simon\Hochschule Aalen/7_Semester_WS19/Versuche Python/Python_Textdatei_einlesen_und_aendern/Positionen-kartesisch.txt", "a")
file.write("\n--------------------------------\n")
zeit = time.time()
file.write(time.strftime('%Y-%m-%d %H:%M:%S\n', time.localtime(zeit)))
Positionsnummer = 21
rcvaktuell = 2345
file.write("Position %s : %s" % (Positionsnummer,rcvaktuell))
"""


#import os
#import re

############# Anzeigen welche Positionen es gibt oder auch Übertragen der Positionsdaten an den Roboter
infile = open("/home/pi/robo/Ergebnisse.txt", "r")
for line in infile:
    
    line.rstrip('\n')
    pre, NrPos = line.split(' 0 0 ')
    Nr, Pos = NrPos.split(' ', 1)

    #print(posNr, '\n')
    print('Position', Nr, Pos)
    #print(Pos)
infile.close()

############Eingabe welche Position verändert werden soll muss später von außen kommen
newNr = input("Manuell verfahren und Positionsnummer eingeben:\n")
recivedStr = ('1 0 0 %s 40 -444 228 -171 90 -180' %newNr)
print(recivedStr)
#Einlesen und teilen
pre, NrPos = recivedStr.rstrip('\n').split(' 0 0 ')
Nr, recivedPos = NrPos.split(' ', 1)
#print(recivedPos)  #recivedPos = '40 -444 228 -171 90 -180'

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

"""
for line in infile:
    if line == '*INCLUDE,INPUT=') :
        # modifizierte Zeile schreiben
    else:
        outfile.write(line) # kopie der eingelesenen Zeile
"""
#outfile.close()
#print(file.readline())
#k2 = re.findall(r"^\w", file, re.U)
#print(k2)