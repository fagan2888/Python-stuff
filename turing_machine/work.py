fl = open("turing_example")
fl = fl.read()
print(fl)
fl = list(fl)
counter = 0
import pdb; pdb.set_trace()
for i in fl:
    counter += 1
    if i == ":":
        fl.insert(counter+1, "'")
        fl.insert(counter-1, "'")
fl = ''.join(fl)
print(fl)
