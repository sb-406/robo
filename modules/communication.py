# Communication to robot and sending of data

# Klasse mit Methoden (Aufruf über self.methode())
class ComRobo():
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
