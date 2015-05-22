class sterling_calc:
    def __init__(self):
        self.num = input("form {n:k}\n")
        self.triangle = []
    def reader(self):
        colon = self.num.find(":")
        self.n = int(self.num[1:colon])
        self.k = int(self.num[colon+1:-1])
    def triangle_constructor(self):
        counter = 0
        for row in range(self.n+1):
            counter = counter + row
        self.pos = counter+self.k
        while len(triangle) != self.pos:
# make the triangle into a matrix where i insert a new n value then give k terms from 0 to n, then insert another
            for x in range(
sterling = sterling_calc()
sterling.reader()
sterling.triangle_constructor()
