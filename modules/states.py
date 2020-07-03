#from communication import WnR, txtRnW, ComRobo
#from gpio_in_and_out import GPIOwaitforEdge, GPIOifHigh

# Zustandsmaschine ohne Klasse
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
    return state
#######################################################
#Funktionen/ Schritte
def f0():
    print("f0 Startanweisungen")
    #x = WnR("Move", "0", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)
    if (responce == "1 0"):
        print("Sub ZERO!")

def f1():
    print("f1 Platinenstapel anfahren")
    WnR("Move", "1", "1")
    print (WnR("waitForEom", "", ""))
    
def f2():
    print("f2 Greifer absetzen/ ansaugen")
    WnR("Move", "2", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)
    if responce == "1 0":
        print("Well, hello there two!")
    
def f3():
    print("f3 Greifer anheben")
    WnR("Move", "3", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)
    if (responce == "1 0"):
        print("There are 3 of us!")
    
def f4():
    print("f4 Fahren bis vor die Presse/ Lichtschranke")
    WnR("Move", "4", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)
    if (responce == "1 0\n"):
        print("for 4!")
    
def f5():
    print("f5 In die Presse einfahren")
    WnR("Move", "5", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)
    if (responce == "1 0\n"):
        print("Well, hello there feif!")
    
def f6():
    print("f6 Greifer absetzen/ Heizplatte")
    WnR("Move", "6", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)
    
def f7():
    print("f7 Ablegen/ Greifer anheben")
    WnR("Move", "7", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)
    
def f8():
    print("f8 Aus Presse fahren")
    WnR("Move", "8", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)
    
def f9():
    print("f9 In Presse fahren")
    WnR("Move", "9", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)
    
def f10():
    print("f10 Greifer absetzen/ ansaugen")
    WnR("Move", "10", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)
    
def f11():
    print("f11 Greifer anheben")
    WnR("Move", "11", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)
    
def f12():
    print("f12 Biegestation anfahren")
    WnR("Move", "12", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)
    
def f13():
    print("f13 Greifer absetzen")
    WnR("Move", "13", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)
    
def f14():
    print("f14 Ablegen/ Greifer anheben")
    WnR("Move", "14", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)
    
def f15():
    print("f15 Aus Presse fahren")
    WnR("Move", "15", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)
    
def f16():
    print("f16 In Presse fahren")
    WnR("Move", "16", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)
    
def f17():
    print("f17 Greifer absetzen/ ansaugen")
    WnR("Move", "17", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)
    
def f18():
    print("f18 Aus Presse fahren")
    WnR("Move", "18", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)
    
def f19():
    print("f19 Zur Messstelle fahren")
    WnR("Move", "19", "1")
    responce = WnR("waitForEom", "", "")
    print (responce)

    

# Klasse mit Methoden (Aufruf über self.metode())
class StateMachine():
    def __init__(self,state = 0):
        self.state = state

    def propagate(self):
        if self.state == 0:
            self.f0()
            self.state = 1
        elif self.state == 1:
            self.f1()
            self.state = 2
        elif self.state == 2:
            self.f2()
            self.state = 0

    def f0(self):
        print("f0")

    def f1(self):
        print("f1")

    def f2(self):
        print("f2")


# nutzt externe Funktionen von oben 
class StateMachine2():
    def __init__(self,state = 0):
        self.state = state

    def propagate(self):
        if self.state == 0:
            f0()
            self.state = 1
        elif self.state == 1:
            f1()
            self.state = 2
        elif self.state == 2:
            f2()
            self.state = 0





