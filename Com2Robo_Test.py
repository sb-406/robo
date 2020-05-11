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
#ser.write('1 HereC 0\n')
#time.sleep(0.5)
#print ("hier")
rcvaktuell = readLine(ser)
#print ("received aktuelle Position:", rcvaktuell)

#ser.write('1 attach 1\n')
#ser.write('1 Profile 1\n')
#ser.write('1 Move 0 1\n')