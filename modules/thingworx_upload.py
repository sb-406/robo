#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        thingworx_upload
# Purpose:
#
# Author:      Simon Bohn Bachelorarbeit 
#
# Created:     12.04.2020
# Links:       https://community.ptc.com/t5/ThingWorx-Developers/can-someone-point-me-to-a-sample-python-script-that-sets/td-p/516106
#              https://www.programcreek.com/python/example/2253/requests.put Tintri
# Funktionen:  _send_raw_http_requests, _send_step, _send_temp
#-------------------------------------------------------------------------------

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
        
##testing
#_send_raw_http_request("PUT", "/Thingworx/Things/PiThingRobot/Properties/Bewegungsschritt", "Bewegungsschritt", "f202")
####################################################################

def _send_step(stepNr): _send_raw_http_request("PUT", "/Thingworx/Things/PiThingRobot/Properties/Bewegungsschritt", "Bewegungsschritt", stepNr)
##testing
#_send_step("f55")

#####################################################################

def _send_temp(temp1): _send_raw_http_request("PUT", "/Thingworx/Things/PiThingRobot/Properties/Temperatur", "Temperatur", temp1)

##testing
#_send_temp(55.5)
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
