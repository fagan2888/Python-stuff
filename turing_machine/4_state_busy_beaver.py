import turing_machine as tm
class Busy(tm.Turing):
#Initialize the tape using the turing initializer
    def __init__(self, start_pos, tape, blank, state):
        tm.Turing.__init__(self, start_pos, tape, blank, state)
        self.run = {
                "A0":("1RB"),
                "A1":("1LB"),
                "B0":("1LA"),
                "B1":("0LC"),
                "C0":("1RH"),
                "C1":("1LD"),
                "D0":("1RD"),
                "D1":("0RA")
                }
        self.ones = 0
    def reader(self):
        while self.state.find('H') < 0:
            command = self.run[self.state]
            tm.Turing.w(self, int(command[0]))
            right = command.find('R')
            left = command.find('L')
            if right > -1:
                tm.Turing.r(self)
            if left > -1:
                tm.Turing.l(self)
            self.state = command[2] + str(self.tape[self.pos])
        for item in self.tape:
            if item == 1:
                self.ones += 1
        print("ones: ", self.ones)

#import pdb; pdb.set_trace()
busy_beaver = Busy(0, 0, 0, "A0")
busy_beaver.reader()
