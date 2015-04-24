fl = open('./write_file.dot')
for line in fl:
    if line.find("digraph") > -1:
        print(fl)
    else:
        print("no")

        
