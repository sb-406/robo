#!/usr/bin/env python
import time
############Serielle Kommunikation
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
        elif ch == '\n':
            return s

ser = serial.Serial(
        port='/dev/ttyS0', #Replace ttyS0 with ttyAM0 for Pi1,Pi2,Pi0
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
############GPIO Pins
import RPi.GPIO as GPIO
 
GPIO_PIN_IR_SENSOR = 4
GPIO_PIN_IR_SENSOR_2 = 17
GPIO_PIN_AUSGANG = 12
 
#DISTANCE = 5.0 # (in cm) Anpassen, falls notwendig
#TIMEOUT = 5 # sek
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
if __name__ == '__main__':
    GPIO.setup(GPIO_PIN_IR_SENSOR, GPIO.IN)
    #GPIO.setup(GPIO_PIN_IR_SENSOR_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(GPIO_PIN_AUSGANG, GPIO.OUT)
    start_time, end_time = 0, 0

#####################################################################
##############Programm mit Roboter IO und IR Sensor##################

counter=0
print ("starting")
#time.sleep(1)
time.sleep(0.5)
ser.write('1 wherec \n')
time.sleep(2)
rcvStandort = readLine(ser)
#print ("received Standort:"), rcvStandort
time.sleep(0.5)
#print ("sending attach")
ser.write('1 attach 1\n')
time.sleep(1)
rcvattach = readLine(ser)
print ("received attach:"), rcvattach
time.sleep(0.5)
#print ("sending Profile")
ser.write('1 Profile 1\n')
time.sleep(1)
rcvProfil = readLine(ser)
print ("received Profil:"), rcvProfil
time.sleep(0.5)

while True:
    ser.write('1 Move 2 1\n')
    #ser.write('1 move %d 5\n'%(counter))
    time.sleep(1)
    rcvMovea = readLine(ser)
    print ("MoveA", rcvMovea)
    ser.write('1 waitForEom\n')
    time.sleep(1)
    rcvEoma = readLine(ser)
    print ("Eom")
    # wait for up to 5 seconds for a rising edge (timeout is in milliseconds)
    print ("Lichtschranke triggern (in 5 Sekunden)")
    channel = GPIO.wait_for_edge(GPIO_PIN_IR_SENSOR_2, GPIO.RISING, timeout=5000)
    if channel is None:
       print('Timeout occurred')
    else:
       print('Edge detected on channel')

    if GPIO.input(GPIO_PIN_IR_SENSOR ) == GPIO.HIGH:
        time.sleep(0.001)

        GPIO.output(GPIO_PIN_AUSGANG, GPIO.HIGH)

        ser.write('1 Move 3 1\n')
        time.sleep(1)
        rcvMoveb = readLine(ser)
        print ("MoveB", rcvMoveb)
        ser.write('1 waitForEom\n')
        time.sleep(1)
        rcvEomb = readLine(ser)
        print ("Eom")
    else:
        ser.write('1 Move 4 1\n')
        time.sleep(1)
        rcvMovec = readLine(ser)
        print ("MoveC", rcvMovec)
        ser.write('1 waitForEom\n')
        time.sleep(1)
        rcvEomc = readLine(ser)
        print ("Eom")

    #print ("received Move:", rcvMove)
    #time.sleep(0.5)
    ser.write('1 waitForEom\n')
    time.sleep(1)
    rcvEom = readLine(ser)
    print ("received Eom:", rcvEom)
    time.sleep(0.5)
    counter += 1

#    print ("sending synch")
#    ser.write('1 move 2 5\n')
#    time.sleep(0.5)
#    rcv = readLine(ser)
#    print ("received:", rcv)

    if(counter==4):
          GPIO.output(GPIO_PIN_AUSGANG, GPIO.LOW)
          
          ser.write('1 Move 1 1\n')
          time.sleep(1)
          rcvMoved = readLine(ser)
          print ("MoveD", rcvMoved)
          ser.write('1 waitForEom\n')
          time.sleep(1)
          rcvEomd = readLine(ser)
          
          break

#while True:
#        ser.write('Write counter: %d \n'%(counter))
#	#Testen
#	print('print Write counter: %d \n'%(counter))
#        time.sleep(1)
#        counter += 1

#	x=ser.readline()
#        print('serialread',x)
	
#	if(counter==10):
#          break

