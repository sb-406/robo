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
        state = 0
    return state

def f0():
    print("f0")

def f1():
    print("f1")

def f2():
    print("f2")

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





