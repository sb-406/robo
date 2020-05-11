#!/usr/bin/env python
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
    Positionsnummer = int(NumStr)
    ser.write("1 HereC %d\n" %Positionsnummer)
    print("1 HereC %d\n" %Positionsnummer)
    #time.sleep(0.5)
    rcv = readLine(ser)
    print ("received Pos:", rcv)
    ser.write('1 locXyz %d\n' %Positionsnummer)
    time.sleep(0.5)
    rcvaktuell = readLine(ser)
    print ("received aktuelle Position%d:" %Positionsnummer, rcvaktuell)
    
    file.write("Position %s : %s" % (Positionsnummer,rcvaktuell))
    #rcvaktuell2 = readLine(ser)
    #print ("received aktuelle Position4:", rcvaktuell2)
    if Positionsnummer >= 8:
        file.close()
        break
