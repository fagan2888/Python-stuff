import turing_machine as tm
class Busy(tm.Turing):

#Initialize the tape using the turing initializer
    def __init__(self, start_pos, tape, blank, state):
        tm.Turing.__init__(self, start_pos, tape, blank, state)
        self.run = {
                "A0":("1rB"),
                "A1":("1lC"),
                "B0":("1lA"),
                "B1":("1rB"),
                "C0":("1lB"),
                "C1":("1lh")
                }

    def reader(self):
        while self.state.find('h') < 0:
            command = self.run[self.state]
            tm.Turing.w(self, int(command[0]))
            right = command.find('r')
            left = command.find('l')
            if right > -1:
                tm.Turing.r(self)
            if left > -1:
                tm.Turing.l(self)
            self.state = command[2] + str(self.tape[self.pos])

busy_beaver = Busy(0, 0, 0, "A0")
busy_beaver.reader()
