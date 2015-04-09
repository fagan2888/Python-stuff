class Turing():
    #Constructor method:
    def __init__(self, start_pos, tape, blank, state):
        self.state = state
        self.pos = start_pos
        self.tape = [tape]
        self.blank = blank
        self.counter = 0
    
#Right method:
    def r(self):
        if self.pos == len(self.tape)-1:
            self.tape.append(self.blank)
            self.pos += 1
            self.counter -= 1
        else:
            self.pos += 1

#Left method:
    def l(self):
        if self.pos == 0:
            self.tape.insert(0, self.blank)
            self.counter += 2
        else:
            self.pos -= 1

#Write method:
    def w(self, inp):
        self.tape[self.pos] = inp
        print(str(self.tape).center(40-self.counter))

