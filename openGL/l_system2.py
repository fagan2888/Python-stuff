class Lsystem:
    def __init__(self, alphabet, axiom, rules, params):
        self.word = axiom
        self.rules = rules
        self.alphabet = alphabet
        self.params = params
    
    def get_param(self, index):
        if self.word[index+1] == '(':
            open_bracket = index+1
            closed_bracket = self.word[open_bracket:].find(')')+open_bracket
            return eval(self.word[open_bracket+1:closed_bracket])
        return False

    def rewrite(self):
        index = 0
        for symbol in self.word:
            if symbol == '(' or symbol == ')' or symbol.isdigit(): 
                continue

            if symbol in self.rules:
                if type(self.rules[symbol]) == tuple:
                    for rule in self.rules[symbol]:

                        param = self.get_param(index)
                        if not param:
                            raise ValueError('error at '+str(index)+': '+symbol+', no parameters provided')

                        if eval(rule[0], {rule[0][0] : param}):
                            new_word += ''.join([parma if x == 
                            break
                else:
                    new_word += self.rules[symbol]
            else:
                new_word += symbol

            index += 1

#    def Ru(self, alpha):
#        self.head = self.head*np.matrix([[cos(alpha), sin(alpha), 0], [-sin(alpha), cos(alpha), 0], [0, 0, 1]])
#
#    def Rl(self, alpha):
#        self.head = self.head*np.matrix([[cos(alpha), 0, -sin(alpha)], [0, 1, 0], [sin(alpha), 0, cos(alpha)]])
#
#    def Rh(self, alpha):
#        self.head = self.head*np.matrix([[1, 0, 0], [0, cos(alpha), -sin(alpha)], [0, sin(alpha), cos(alpha)]])
#
#    def turtle(self, ):
#        evaluated_word = 
#
#    def reader(self, string):
#        self.position = self.position_init
#        self.head = self.head_init
#        stack = []
#        index = 0
#        for symbol in string:
#            if symbol == '+':
#                if string[index+1] == '(':
#                    open_bracket = index+1
#                    closed_bracket = string[open_bracket:].find(')')+open_bracket
#                    self.Ru(eval(string[open_bracket+1:closed_bracket]))
#                else:
#                    self.Ru(pi/2)
#            elif symbol == '-':
#                if string[index+1] == '(':
#                    open_bracket = index+1
#                    closed_bracket = string[open_bracket:].find(')')+open_bracket
#                    self.Ru(-eval(string[open_bracket+1:closed_bracket]))
#                else:
#                    self.Ru(-pi/2)
#            elif symbol == '&':
#                if string[index+1] == '(':
#                    open_bracket = index+1
#                    closed_bracket = string[open_bracket:].find(')')+open_bracket
#                    self.Rl(eval(string[open_bracket+1:closed_bracket]))
#                else:
#                    self.Rl(pi/2)
#            elif symbol == '^':
#                if string[index+1] == '(':
#                    open_bracket = index+1
#                    closed_bracket = string[open_bracket:].find(')')+open_bracket
#                    self.Rl(-eval(string[open_bracket+1:closed_bracket]))
#                else:
#                    self.Rl(-pi/2)
#            elif symbol == '\\':
#                if string[index+1] == '(':
#                    open_bracket = index+1
#                    closed_bracket = string[open_bracket:].find(')')+open_bracket
#                    self.Rh(eval(string[open_bracket+1:closed_bracket]))
#                else:
#                    self.Rh(pi/2)
#            elif symbol == '/':
#                if string[index+1] == '(':
#                    open_bracket = index+1
#                    closed_bracket = string[open_bracket:].find(')')+open_bracket
#                    self.Rh(-eval(string[open_bracket+1:closed_bracket]))
#                else:
#                    self.Rh(-pi/2)
#            elif symbol == '|':
#                self.Ru(pi)
#            elif symbol == '[':
#                stack.append((self.position, self.head))
#            elif symbol == ']':
#                top = stack.pop()
#                self.position = top[0]
#                self.head = top[1]
#            elif symbol == 'F' or symbol == 'R' or symbol == 'L' or symbol == 'G':
#                if string[index+1] == '(':
#                    open_bracket = index+1
#                    closed_bracket = string[open_bracket:].find(')')+open_bracket
#                    d = float(string[open_bracket+1:closed_bracket])
#                    new_position = self.position + d * self.head
#                    self.moves.append((self.position, new_position, 'draw')) 
#                    self.position = new_position
#                else:
#                    new_position = self.position + self.head
#                    self.moves.append((self.position, new_position, 'draw')) 
#                    self.position = new_position
#            elif symbol == 'f' or symbol == 'g':
#                if string[index+1] == '(':
#                    open_bracket = index+1
#                    closed_bracket = string[open_bracket:].find(')')+open_bracket
#                    d = float(string[open_bracket+1:closed_bracket])
#                    new_position = self.position + d * self.head
#                    self.moves.append((self.position, new_position, 'no draw')) 
#                    self.position = new_position
#                else:
#                    new_position = self.position + self.head
#                    self.moves.append((self.position, new_position, 'no draw')) 
#                    self.position = new_position
#            index += 1
#
