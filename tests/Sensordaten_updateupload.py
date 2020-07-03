#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Sensordaten_updateupload
# Purpose:
#
# Author:      Simon Bohn Bachelorarbeit 
#
# Created:     12.04.2020
# Links:       https://community.ptc.com/t5/ThingWorx-Developers/can-someone-point-me-to-a-sample-python-script-that-sets/td-p/516106
#              https://www.programcreek.com/python/example/2253/requests.put
# Funktionen:  
#-------------------------------------------------------------------------------           

import time
import sys
import RPi.GPIO as GPIO


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

####################################################################
def _send_raw_http_request( method, url2="", data1="", value=""):
        import requests
        import json
        
        import urllib3
        urllib3.disable_warnings()
        
        url1 = "https://twxhsaalen01.inneo.cloud"
        url = url1 + url2
        
        headers = { "Content-Type": "application/json", "appKey": "6a65119c-5819-4ca2-b043-048aff006c19" }
        data = { data1 : value}
        
        if method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
            if method == 'GET': httpresp = requests.get(url, headers=headers, verify=False)
            elif method == 'POST': httpresp = requests.post(url, headers=headers, json=data, verify=False)
            elif method == 'PUT': httpresp = requests.put(url, headers=headers, json=data, verify=False)
            elif method == 'PATCH': httpresp = requests.patch(url, headers=headers, json=data, verify=False)
            elif method == 'DELETE': httpresp = requests.delete(url, headers=headers, verify=False)
            print (httpresp)
            return httpresp
        else:
            return False
        
########################################################################
        #MAIN Loop
        
try:
    Endschalter_oben=False     # 20= 
    Endschalter_unten=False      # 21=
    IR_Sensor_1=False           # 17=
    IR_Sensor_2=False           # 18=
    Kontakt_Stapel_1=False      # 25=
    Kontakt_Stapel_2=False      # 26=
    Output_Presse_runter=False  # 12=
    Output_Presse_hoch=False    # 13=
    #    Temperatur:20.00
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(20, GPIO.IN)
    GPIO.setup(21, GPIO.IN)
    GPIO.setup(17, GPIO.IN)
    GPIO.setup(18, GPIO.IN)
    GPIO.setup(25, GPIO.IN)
    GPIO.setup(26, GPIO.IN)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    
    while True :
        if GPIO.input(20) == Endschalter_oben:
            Endschalter_oben= not(GPIO.input(20))
            _send_raw_http_request( "PUT", "/Thingworx/Things/PiThingRobot/Properties/Endschalter_oben", "Endschalter_oben", Endschalter_oben)
        if GPIO.input(21) == Endschalter_unten:
            Endschalter_unten= not(GPIO.input(21))
            _send_raw_http_request( "PUT", "/Thingworx/Things/PiThingRobot/Properties/Endschalter_unten", "Endschalter_unten", Endschalter_unten)
        if GPIO.input(17) != IR_Sensor_1:
            IR_Sensor_1= GPIO.input(17)
            _send_raw_http_request( "PUT", "/Thingworx/Things/PiThingRobot/Properties/IR_Sensor_1", "IR_Sensor_1", IR_Sensor_1)
        if GPIO.input(18) != IR_Sensor_2:
            IR_Sensor_2= GPIO.input(18)
            _send_raw_http_request( "PUT", "/Thingworx/Things/PiThingRobot/Properties/IR_Sensor_2", "IR_Sensor_2", IR_Sensor_2)        
        if GPIO.input(25) == Kontakt_Stapel_1:
            Kontakt_Stapel_1= not(GPIO.input(25))
            _send_raw_http_request( "PUT", "/Thingworx/Things/PiThingRobot/Properties/Kontakt_Stapel_1", "Kontakt_Stapel_1", Kontakt_Stapel_1)
        if GPIO.input(26) == Kontakt_Stapel_2:
            Kontakt_Stapel_2= not(GPIO.input(26))
            _send_raw_http_request( "PUT", "/Thingworx/Things/PiThingRobot/Properties/Kontakt_Stapel_2", "Kontakt_Stapel_2", Kontakt_Stapel_2)
        if GPIO.input(12) != Output_Presse_runter:
            Output_Presse_runter= GPIO.input(12)
            _send_raw_http_request( "PUT", "/Thingworx/Things/PiThingRobot/Properties/Output_Presse_runter", "Output_Presse_runter", Output_Presse_runter)
        if GPIO.input(13) != Output_Presse_hoch:
            Output_Presse_hoch= GPIO.input(13)
            _send_raw_http_request( "PUT", "/Thingworx/Things/PiThingRobot/Properties/Output_Presse_hoch", "Output_Presse_hoch", Output_Presse_hoch)

        
        
        time.sleep(0.02)
        
        
except KeyboardInterrupt:
    # Programm wird beendet wenn CTRL+C gedrückt wird.
    print(Interrupt)   
except Exception as e:
    print(str(e))
    sys.exit(1)
finally:
    # Das Programm wird hier beendet, sodass kein Fehler in die Console geschrieben wird.
    print('Programm wird beendet.')
    sys.exit(0)