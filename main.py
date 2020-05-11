from modules.states import state_machine, StateMachine
from modules.communication import WnR, ComRobo
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
    
def readLine(port):
    s = ""
    while True:
        ch = port.read()
        s += ch.decode()
        #if ch == '\r':
        #    return s
        if ch == '\n':
            return s

def WnRx(self):
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

#It's easier than it is thought:

#my_str = "hello world"
#my_str_as_bytes = str.encode(my_str)
#print(type(my_str_as_bytes)) # ensure it is byte representation
#my_decoded_str = my_str_as_bytes.decode()
#print(type(my_decoded_str)) # ensure it is string representation
        

###main   
Command= input("Kommando eingeben:")
arg1= input("Argument 1 eingeben:")
arg2_n= input("Argument 2 bis n eingeben:")
Robosaid= WnR(Command, arg1, arg2_n)
print("erhalten: "+Robosaid)

"""
Positionsnummer = 0
while Positionsnummer < 8:
    NumStr= raw_input("Etwas eingeben:\n")
    #Positionsnummer = int(NumStr)
    #Positionsnummer = int(NumStr)
    ser.flushOutput()
    ser.write(str.encode(NumStr))
    print(str.encode(NumStr))
    #print("1 HereC %s\n" %NumStr)
    time.sleep(5)
    rcv = readLine(ser)
    print (rcv)
    time.sleep(5)
"""
"""
ser.flushOutput()
NumStr= input('Etwas eingeben:\n')
print(NumStr)
#Kommando = NumStr
#ser.write(Kommando)
#time.sleep(1)
#abc = readLine(ser)
#print(abc)        

print("ubergabe der Befehle testen")
s = ComRobo()
s.Command = "1 attach\n"
answer = s.WnR()
print("Der Befehl war %s und die Antwort ist %s", (s.Command, answer))
"""
"""
print("Version mit Funktionen")
state = 0
for k in range(10):
    state = state_machine(state)

print("Version mit Klasse")
s = StateMachine()
for k in range(10):
    s.propagate()
    print(s.state)
"""