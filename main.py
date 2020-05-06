from modules.states import state_machine, StateMachine
from modules.communication import ComRobo

print("Übergabe der Befehle testen")
s = ComRobo()
s.Command = "1 attach\n"
answer = s.WnR()
print("Der Befehl war %s und die Antwort ist %s", (s.Command, answer))

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