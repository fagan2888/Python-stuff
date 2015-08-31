import graphviz 
from useful_stuff import convert_base as convert
from collatz_manual import collatz

dot = graphviz.Digraph()

current = [1.0]
overall = []
move = 0
new = []

lim = 30
total = [x for x in range(1, lim+1)]

for i in total:
	if collatz(i) > 2:
		total.pop(total.index(i))

while True:
	nex = []
	if len(new) == len(total):
		break
	for x in current:
		if x in total:
			dot.node(str(x), str(int(x)), color='green', shape='polygon', sides=str(x))
		else:
			dot.node(str(x), str(int(x)))
		if x in total and x not in new:
			new.append(x)
		overall.append(x)
		if (x-1)/3 % 1 == 0 and (x-1)/3 not in overall and (x-1)/3 % 2 == 1:
			dot.node(str((x-1)/3), str(int((x-1)/3)), color='red')
			dot.edge(str((x-1)/3), str(x), arrowhead='ediamond')
			nex.append((x-1)/3)
		dot.node(str(x*2), str(int(x*2)), color='blue')
		dot.edge(str(x*2), str(x), arrowhead='diamond')
		nex.append(x*2)
	move += 1
	current = nex
print(total, new)
dot.render('Downloads/collatz_tree')
