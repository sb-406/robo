from modules.states import state_machine, StateMachine

print("Version mit Funktionen")
state = 0
for k in range(10):
    state = state_machine(state)

print("Version mit Klasse")
s = StateMachine()
for k in range(10):
    s.propagate()
    print(s.state)