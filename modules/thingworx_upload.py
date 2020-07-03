#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        thingworx_upload
# Purpose:
#
# Author:      Simon Bohn Bachelorarbeit 
#
# Created:     12.04.2020
# Links:       https://community.ptc.com/t5/ThingWorx-Developers/can-someone-point-me-to-a-sample-python-script-that-sets/td-p/516106
#              https://www.programcreek.com/python/example/2253/requests.put
# Funktionen:  
#-------------------------------------------------------------------------------
"""
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
"""
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
        
        #print(url)
        #print (data)
        #httpresp = requests.put(url, headers=headers, json=data, verify=False)
        #print (httpresp)

##testing
#_send_raw_http_request("PUT", "/Thingworx/Things/PiThingRobot/Properties/Bewegungsschritt", "Bewegungsschritt", "f202")
####################################################################

def _send_step(stepNr): _send_raw_http_request("PUT", "/Thingworx/Things/PiThingRobot/Properties/Bewegungsschritt", "Bewegungsschritt", stepNr)
##testing
#_send_step("f55")

#####################################################################
#Warnung zur unsicheren Verbindung unterdrücken
#import urllib3
#urllib3.disable_warnings()

#url = "https://twxhsaalen01.inneo.cloud"
#Upload
#headers = { "Content-Type": "application/json", "appKey": "6a65119c-5819-4ca2-b043-048aff006c19" }


##Create new Thing for the tests
#payload = {"name": "PiThingRobot","thingTemplateName": "GenericThing"}
#response = requests.post(url+ "/Thingworx/Resources/EntityServices/Services/CreateThing", headers=headers, json=payload, verify=False)

##Enable the new created Thing
#response = requests.post(url+ "/Thingworx/Things/PiThingRobot/Services/EnableThing", headers=headers, verify=False)

##Restart the new Thing
#response = requests.post(url+ "/Thingworx/Things/PiThingRobot/Services/RestartThing", headers=headers, verify=False)

##Add Properties
#payload = {"name" : "Temperatur", "type" : "NUMBER"}
#response = requests.post(url+ "/Thingworx/Things/PiThingRobot/Services/AddPropertyDefinition", headers=headers, json=payload, verify=False)

##Restart the new Thing with the new Property
#response = requests.post(url+ "/Thingworx/Things/PiThingRobot/Services/RestartThing", headers=headers, verify=False)

##Set the value of the new Prop
#payload = {"IR_Sensor_1" : True}
#response = requests.put(url+ "/Thingworx/Things/PiThingRobot/Properties/IR_Sensor_1", headers=headers, json=payload, verify=False)

##Get the value of the Prop
#headers = { "appKey": "6a65119c-5819-4ca2-b043-048aff006c19" }
#response = requests.get(url+ "/Thingworx/Things/SomeTestThing/Properties/SomeNumber", headers=headers, verify=False)

#print(response)



#Inhalt der config.json
"""
{ 
    "ws_servers":   [{
                "host": "twxhsaalen01.inneo.cloud",
                "port": 443
        }],
    "appKey":   "3886bd95-ff2c-4049-9f55-2e59874105d9",
    "http_server" : {
        "host": "192.168.178.50",
        "port": 8080,
        "use_default_certificate" : true,
        "ssl" : false,
        "authenticate" : false
        },
    "logger":{
        "level":"INFO"
    },
    "certificates":{
        "validate": false
    }
}
"""
"""
Beispiel von Tintri
def _send_raw_http_request(self, method, url, data=None):
        self.__logger.debug('%s %s' % (method, url))
        if method in ['POST', 'PUT', 'PATCH']:
            self.__logger.log(TINTRI_LOG_LEVEL_DATA, 'Data: %s' % data)

        headers = {'content-type': 'application/json'}
        if self.__session_id:
            headers['cookie'] = 'JSESSIONID=%s' % self.__session_id

        if method in ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']:
            if method == 'GET': httpresp = requests.get(url, headers=headers, verify=False)
            elif method == 'POST': httpresp = requests.post(url, data, headers=headers, verify=False)
            elif method == 'PUT': httpresp = requests.put(url, data, headers=headers, verify=False)
            elif method == 'PATCH': httpresp = requests.patch(url, data, headers=headers, verify=False)
            elif method == 'DELETE': httpresp = requests.delete(url, headers=headers, verify=False)
            self._httpresp = httpresp # self._httpresp is for debugging only, not thread-safe
            return httpresp
        else:
            raise TintriError(None, message='Invalid HTTP method: ' + method) # This should never happen
"""