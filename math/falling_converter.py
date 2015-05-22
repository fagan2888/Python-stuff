def reader():
    equation = input("equation, eg: x^2_ + x^3_\n")
    equation = list(equation)
    counter = -1
    xs = []
    for i in equation:
        counter += 1 
        if i == "^":
            caret = counter
        if i == "_":
            xs.append(equation[caret-1:counter])
    for x in xs:
        x = ''.join(x)
        print(x)
reader()
            

        

