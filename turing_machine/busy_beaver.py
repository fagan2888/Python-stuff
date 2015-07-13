import turing_machine as tm


class Busy(tm.Turing):


#Initialize the tape using the turing initializer
    def __init__(self, start_pos, tape, blank):
        tm.Turing.__init__(self, start_pos, tape, blank)

#State A:
    def A(self):
        if self.tape[self.pos] == 0:
            tm.Turing.w(self, 1)
            tm.Turing.r(self)
            Busy.B(self)
        elif self.tape[self.pos] == 1:
            tm.Turing.w(self, 1)
            tm.Turing.l(self)
            Busy.C(self)
#State B:
    def B(self):
        if self.tape[self.pos] == 0:
            tm.Turing.w(self, 1)
            tm.Turing.l(self)
            Busy.A(self)
        elif self.tape[self.pos] == 1:
            tm.Turing.w(self, 1)
            tm.Turing.r(self)
            Busy.B(self)
#State C:
    def C(self):
        if self.tape[self.pos] == 0:
            tm.Turing.w(self, 1)
            tm.Turing.l(self)
            Busy.B(self)
        if self.tape[self.pos] == 1:
            tm.Turing.w(self, 1)
            tm.Turing.l(self)


busy = Busy(0, [0], 0)
busy.A()
