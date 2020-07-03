#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        GPIO Inputs and Outputs
# Purpose:
#
# Author:      Simon Bohn Bachelorarbeit 
#
# Created:     12.04.2020
# Links:       https://stackoverflow.com/questions/45411924/python3-two-way-serial-communication-reading-in-data 12.05.2020 Grundlage für WnR Funktion
#
#
# Funktionen:  
#-------------------------------------------------------------------------------

import time

############GPIO Pins
import RPi.GPIO as GPIO
##############################################################
#GPIO_PIN:
AUSGANG_LED = 12
AUSGANG_NR2 = 13
IR_SENSOR_1 = 18
IR_SENSOR_2 = 17
ENDSCHALTER_OBEN = 20
ENDSCHALTER_UNTEN = 21
KONTAKT_STAPEL_1 = 25
KONTAKT_STAPEL_2 = 26 


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
if __name__ == '__main__':
    GPIO.setup(AUSGANG_LED, GPIO.OUT)
    GPIO.setup(AUSGANG_NR2, GPIO.OUT)
    GPIO.setup(IR_SENSOR_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(IR_SENSOR_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ENDSCHALTER_OBEN, GPIO.IN)
    GPIO.setup(ENDSCHALTER_UNTEN, GPIO.IN)
    GPIO.setup(KONTAKT_STAPEL_1, GPIO.IN)
    GPIO.setup(KONTAKT_STAPEL_2, GPIO.IN)
     
################################################################

def GPIOwaitforEdge(Pin_ID= False, Message="", Edgeset= True):
    #Pin_ID = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(Pin_ID, GPIO.IN)
    if Edgeset == True:
        Edge = GPIO.RISING
    else:
        Edge = GPIO.FALLING
    if Message != "":
        print (Message)
    #channel = GPIO.wait_for_edge(Pin_ID, GPIO.RISING, timeout=5000)
    channel = GPIO.wait_for_edge(Pin_ID, Edge)#,timeout=20000)
    if channel is None:
       print("Timeout occurred")
       return False
    else:
       print("Edge detected on channel %s"%Pin_ID)
       return True
    
def GPIOifHigh(Pin_ID= False):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(Pin_ID, GPIO.IN)
    #print (Message)
    #GPIO.setup(Pin_ID, GPIO.IN)
    if GPIO.input(Pin_ID) == GPIO.HIGH:
        print("%s is Low"%Pin_ID)
        return False
    else:
        print("%s is High"%Pin_ID)
        return True
    
def GPIOsetOutput(Pin_ID= False, endswitch = False, Message = ""):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    #GPIO.setup(AUSGANG_LED, GPIO.OUT)
    GPIO.setup(Pin_ID, GPIO.OUT)
    
    if Message != "":
        print (Message)
    GPIO.output(Pin_ID, 1)
    if GPIOwaitforEdge(endswitch) == True:
        GPIO.output(Pin_ID, 0)
    
    
##################################
    #Für den Test dieser Funktion
"""
Pin_ID = int(input("Pin_ID eingeben:\n"))
Pin_ID2 = int(input("Pin_ID2 eingeben:\n"))
edgy = GPIOwaitforEdge(Pin_ID)
print (edgy)
higs = GPIOifHigh(Pin_ID2)
print (higs)
"""
