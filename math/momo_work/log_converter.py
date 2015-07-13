from sys import argv
def converter(equation):
    if equation.find("log") > -1:
        #log_a_b=c
        underscore = 0
        underscores = []
        while underscore != -1:
            underscore = equation.find("_", underscore + 1)
            underscores.append(underscore)
        equals = equation.find("=")
        a = equation[underscores[0]+1:underscores[1]] 
        b = equation[underscores[1]+1:equals]
        c = equation[equals+1:]
        equation = str(a + "^" + c + "=" + b)
        print(equation)
    elif equation.find("^") > -1:
        #a^b=c
        upper = equation.find("^") 
        equals = equation.find("=")
        a = equation[:upper]
        b = equation[upper+1:equals]
        c = equation[equals+1:]
        equation = str("log_" + a + "_" + b + "=" + c)
        print(equation)
        
converter(argv[1])
