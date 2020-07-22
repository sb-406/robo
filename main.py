#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        Robot Controll
# Purpose:
#
# Author:      Simon Bohn Bachelorarbeit 
#
# Created:     12.04.2020
# Links:       
# Funktionen:  
#-------------------------------------------------------------------------------


from modules.states import state_machine, StateMachine
from modules.communication import WnR, txtRnW, WaitforEom, getTemp #,ComRobo
from modules.gpio_in_and_out import GPIOwaitforEdge, GPIOifHigh, GPIOsetOutput
from modules.thingworx_upload import _send_raw_http_request, _send_step, _send_temp

#import time#
import sys
#import threading#

        

###main
#Startup
"""
WnR("attach", "1", "")
WnR("hp", "1", "10")
WnR("attach", "1", "")
WnR("home", "", "")
Bewegungsprofil = WnR("Profile", "1", "")
print(Bewegungsprofil)
txtRnW("2")
"""
"""# Testen der Kommandos an Roboter
mode = input("Modus auswählen (Positionen: 1 anzeigen 2 an Roboter geben 3 anfahren und teachen 4 justieren):\n")
Lemon = txtRnW(mode)
print(Lemon)
while True:      
    Command= input("Kommando eingeben:")
    arg1= input("Argument 1 eingeben:")
    arg2_n= input("Argument 2 bis n eingeben:")
    Robosaid= WnR(Command, arg1, arg2_n)
    print("erhalten: "+Robosaid)
    if arg1 == "x":
        break
"""

#####################################################
#Loop
#Statusabfage/ Ablaufsteuerung
def state_machine(state):
    if state == 0:
        f0()
        state = 1
    elif state == 1:
        f1()
        state = 2
    elif state == 2:
        f2()
        state = 3
    elif state == 3:
        f3()
        state = 4
    elif state == 4:
        f4()
        state = 5
    elif state == 5:
        f5()
        state = 6
    elif state == 6:
        f6()
        state = 7
    elif state == 7: 
        f7()
        state = 8
    elif state == 8: 
        f8()
        state = 9
    elif state == 9: 
        f9()
        state = 10
    elif state == 10: 
        f10()
        state = 11  
    elif state == 11: 
        f11()
        state = 12
    elif state == 12: 
        f12()
        state = 13
    elif state == 13: 
        f13()
        state = 14
    elif state == 14: 
        f14()
        state = 15
    elif state == 15: 
        f15()
        state = 16
    elif state == 16: 
        f16()
        state = 17
    elif state == 17: 
        f17()
        state = 18
    elif state == 18: 
        f18()
        state = 19
    elif state == 19: 
        f19()
        state = 1
    elif state == 20: 
        f20()
        state = 21
    elif state == 21: 
        f21()
        state = 22
    elif state == 22: 
        f22()
        state = 23
    elif state == 23: 
        f23()
        state = 24
        
        
    elif state == 999:
        fx()
    return state
#######################################################
#Funktionen/ Schritte
def f0():
    print("f0 Startanweisungen")
    _send_step("f0")
    WnR("attach", "1", "")
    WnR("hp", "1", "10")
    WnR("attach", "1", "")
    WnR("home", "", "")
    Bewegungsprofil = WnR("Profile", "1", "")
    print(Bewegungsprofil)
    txtRnW("2")

def f1():
    print("f1 Platinenstapel anfahren")
    _send_step("f1")
    #ok = GPIOifHigh(25)#Checked ob eine Platine auf Stapel 1
    if GPIOifHigh(25) != True: #Checked ob eine Platine auf Stapel 1
        GPIOwaitforEdge(25, "Stapel 1 Platine eingelegt?")
    if GPIOifHigh(26) == True:#Checked ob Stapel 2 frei ist
        GPIOwaitforEdge(26, "Stapel 2 leer?", False)
    WnR("Move", "1", "1")
    WaitforEom()
    
def f2():
    print("f2 Greifer absetzen/ ansaugen")
    _send_step("f2")
    WnR("Move", "2", "1")
    WaitforEom()
    WnR("Sig", "33", "1") #Durchgang für Vakuumpumpe frei, Saugnapf zieht an
    
def f3():
    print("f3 Greifer anheben")
    _send_step("f3")
    WnR("Move", "3", "1")
    WaitforEom()
    
def f4():
    print("f4 Fahren bis vor die Presse/ Lichtschranke")
    _send_step("f4")
    WnR("Move", "4", "1")
    GPIOwaitforEdge(17, "Lichtschranke vor Presse")
    WaitforEom()
    
def f5():
    print("f5 In die Presse einfahren")
    _send_step("f5")
    if GPIOifHigh(20) != True:
        GPIOwaitforEdge(20, "Endschalter_oben drücken")
    GPIOifHigh(20)
    WnR("Move", "5", "1")
    WaitforEom()
    
def f6():
    print("f6 Greifer absetzen Heizplatte/ ablegen")
    _send_step("f6")
    WnR("Move", "6", "1")
    WaitforEom()
    WnR("Sig", "33", "0")
    
def f7():
    print("f7 Greifer anheben")
    _send_step("f7")
    WnR("Move", "7", "1")
    WaitforEom()
    
def f8():
    print("f8 Aus Presse fahren")
    _send_step("f8")
    WnR("Move", "8", "1")
    GPIOwaitforEdge(17, "Lichtschranke vor Presse")
    WaitforEom()
    GPIOsetOutput(12, 21, "Presse fährt runter")
    GPIOsetOutput(13, 20, "Presse fährt hoch")
    
def f9():
    print("f9 In Presse fahren")
    _send_step("f9")
    if GPIOifHigh(20) != True:
        GPIOwaitforEdge(20, "Endschalter_oben drücken")
    WnR("Move", "9", "1")
    WaitforEom()
    
def f10():
    print("f10 Greifer absetzen/ ansaugen")
    _send_step("f10")
    WnR("Move", "10", "1")
    WaitforEom()
    WnR("Sig", "33", "1")
    
def f11():
    print("f11 Greifer anheben")
    _send_step("f11")
    WnR("Move", "11", "1")
    WaitforEom()
    
def f12():
    print("f12 Biegestation anfahren")
    _send_step("f12")
    WnR("Move", "12", "1")
    WaitforEom()
    
def f13():
    print("f13 Greifer absetzen/ ablegen")
    _send_step("f13")
    WnR("Move", "13", "1")
    WaitforEom()
    WnR("Sig", "33", "0")
    
def f14():
    print("f14 Greifer anheben")
    _send_step("f14")
    WnR("Move", "14", "1")
    WaitforEom()
    
def f15():
    print("f15 Aus Presse fahren")
    _send_step("f15")
    WnR("Move", "15", "1")
    GPIOwaitforEdge(17, "Lichtschranke vor Presse")
    WaitforEom()
    GPIOsetOutput(12, 21, "Presse fährt runter")
    GPIOsetOutput(13, 20, "Presse fährt hoch")
    
def f16():
    print("f16 In Presse fahren")
    _send_step("f16")
    if GPIOifHigh(20) != True:
        GPIOwaitforEdge(20, "Endschalter_oben drücken")
    WnR("Move", "16", "1")
    WaitforEom()
    
def f17():
    print("f17 Greifer absetzen/ ansaugen")
    _send_step("f17")
    WnR("Move", "17", "1")
    WaitforEom()
    WnR("Sig", "33", "1")
    
def f18():
    print("f18 Aus Presse fahren")
    _send_step("f18")
    WnR("Move", "18", "1")
    WaitforEom()
    
def f19():
    print("f19 Zur Messstelle fahren")
    _send_step("f19")
    WnR("Move", "19", "1")
    GPIOwaitforEdge(18, "Lichtschranke an Messstelle")
    WaitforEom()
    _send_temp(getTemp())
    
def f20():
    print("f20 Zum Ablegestapel fahren")
    _send_step("f20")
    WnR("Move", "20", "1")
    WaitforEom() 

def f21():
    print("f21 Greifer absetzen/ ablegen")
    _send_step("f21")
    WnR("Move", "21", "1")
    WaitforEom()
    WnR("Sig", "33", "0")

def f22():
    print("f22 Greifer anheben")
    _send_step("f22")
    WnR("Move", "22", "1")
    WaitforEom()

def f23():
    print("f23 Fahren in Ausgangsposition")
    _send_step("f23")
    WnR("Move", "23", "1")
    WaitforEom()
#    
#
#
def fx():
    print('Loop wird beendet')
    _send_step("fx")
    WnR("hp", "0", "10")
############################################################    
#MAIN FUNKTION 
try:
    state = state_machine(0)
    while True :
        state =1
        while state<24:
            state = state_machine(state)
        
except KeyboardInterrupt:
    # Programm wird beendet wenn CTRL+C gedrückt wird.
    state = 999
    state_machine(state)
    
except Exception as e:
    print(str(e))
    sys.exit(1)
finally:
    # Das Programm wird hier beendet, sodass kein Fehler in die Console geschrieben wird.
    print('Programm wird beendet.')
    sys.exit(0)







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