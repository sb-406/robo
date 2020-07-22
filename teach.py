#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        teach
# Purpose:
#
# Author:      Simon Bohn Bachelorarbeit 
#
# Created:     30.06.2020
# Links:       
# Funktionen:  
#-------------------------------------------------------------------------------
from modules.communication import WnR, txtRnW

import sys

try:
    while True :
        #mode = input("Modus auswählen (Positionen: 1 anzeigen 2 an Roboter geben 3 anfahren und teachen 4 justieren):\n")
        mode = 3
        Lemon = txtRnW(mode)
        print(Lemon)      
        
except KeyboardInterrupt:
    # Programm wird beendet wenn CTRL+C gedrückt wird.
    print("Abbruch durch User.")
    
except Exception as e:
    print(str(e))
    sys.exit(1)
finally:
    # Das Programm wird hier beendet, sodass kein Fehler in die Console geschrieben wird.
    print('Programm wird beendet.')
    sys.exit(0)