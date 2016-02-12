import graphviz 
from collatz_manual import collatz

dot = graphviz.Digraph()

current = [1.0]
overall = []
move = 0
new = []

lim = 5000
total = [x for x in range(1, lim+1)]

while True:
    if len(total) <= len(overall):
        break
    nex = []
    for x in current:
        if x in overall:
            continue
        if x in total:
            dot.node(str(x), str(int(x)), color='green', shape='polygon', sides=str(x))
            if x not in new:
                new.append(x)
        else:
            dot.node(str(x), str(int(x)))
        if (x-1)/3 % 1 == 0 and (x-1)/3 and (x-1)/3 % 2 == 1 and (x-1)/3 != 0:
            dot.node(str((x-1)/3), str(int((x-1)/3)), color='red')
            dot.edge(str((x-1)/3), str(x), arrowhead='ediamond')
            nex.append((x-1)/3)
        dot.node(str(x*2), str(int(x*2)), color='blue')
        dot.edge(str(x*2), str(x), arrowhead='diamond')
        nex.append(x*2)
        move += 1
        overall.append(x)
    current = nex[:]

print("done")
dot.render('/home/jhazelden/Downloads/pdfs/collatz')
