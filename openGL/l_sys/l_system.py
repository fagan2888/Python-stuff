class l_system:
    def __init__(self, fl):
        self.fl = open(fl, 'r').readlines()
        self.rules = []
        for line in self.fl:
            if 'axiom' in line:
                self.word = line[line.find(':')+1:]
            if line[0] == 'p':
                rules.append(line[line.find(':')+1:])

    def rewrite(self):
        index = 0
        new_word = ''
        for symbol in self.word:
            if symbol.isdigit() or symbol == ')' or symbol == '(':
                continue
            
            if self.word[index+1] == '(':
                var = self.word[index+1:self.word.find(')')]
            
            new_string = False
            for production in self.rules:
                if symbol == production[0]: 
                    new_string = list(self.rules[production])
                    param = production[2]
                    break
            
            if not new_string:
                new_word += symbol
                continue

            for n in range(len(new_string)):
                if new_string[n] == param:
                    new_string[n] = var 

            new_word += ''.join(new_string)

            index += 1

l_system('config')
