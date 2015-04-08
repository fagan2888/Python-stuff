class Turing():
    def __init__(self, start_pos, tape, blank):
        self.pos = start_pos
        self.tape = tape
        self.blank = blank

    def right(self):
        if self.pos == len(self.tape)-1:
            self.tape.append(self.blank)
            self.pos += 1
        else:
            self.pos += 1
    def left(self):
        if self.pos == 0:
            self.tape.insert(0, self.blank)
        else:
            self.pos -= 1
    def write(self, inp):
        self.tape[self.pos] = inp
        print(self.tape)

class example():
    def __init__(self, start_pos, tape, blank):
        Turing.__init__(self, start_pos, tape, blank)
#Look in busy_beaver.py for help on how to define states
