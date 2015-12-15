class Turing():
    def __init__(self, pos, tape, inp, state, axiom):
        self.state = state
        self.pos = pos
        self.inp = inp
        self.steps = 0
        self.axiom = axiom
        self.tape = tape
        
    def r(self):
        if self.pos == len(self.tape)-1:
            self.tape.append(self.inp[0])
            self.pos += 1 
        else:
            self.pos += 1

    def l(self):
        if self.pos == 0 :
            self.tape.insert(0, self.inp[0])
        else: 
            self.pos -= 1
    
    def w(self, inp):
        self.tape[self.pos] = inp

    def reader(self):
        for i in self.axiom:
            if str(self.tape[self.pos]) == i[1] and self.state == i[0]:
                for x in self.axiom[i]:
                    if 'h' in x:
                        return self.tape
                    if x == 'r':
                        self.r()
                    if x == 'l':
                        self.l()
                    if x == 'w':
                        self.w(self.inp[1])
                    if x == 'b':
                        self.w(self.inp[0])
                self.state = self.axiom[i][-1]
                self.reader()

#     def __init__(self, pos, tape, inp, state, axiom):
busy_3_state = Turing(0, [0], (0, 1), 'A', {'A0': 'wrB', 'A1': 'wlC', 'B0': 'wlA', 'B1': 'wrB', 'C0': 'wlB', 'C1': 'wlh'})
busy_4_state = Turing(0, [0], (0, 1), 'A', {'A0': 'wrB', 'A1': 'wlB', 'B0': 'wlA', 'B1': 'blC', 'C0': 'wrh', 'C1': 'wlD', 'D0': 'wrD', 'D1': 'brA'})
busy_5_state = Turing(0, [0], (0, 1), 'A', {'A0': 'wrB', 'A1': 'wlC', 'B0': 'wrC', 'B1': 'wrB', 'C0': 'wrD', 'C1': 'blE', 'D0': 'wlA', 'D1': 'wlD', 'E0': 'wrh', 'E1': 'blA'})



busy_4_state.reader()
