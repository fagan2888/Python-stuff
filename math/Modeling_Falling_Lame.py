import matplotlib.pyplot as plt
#       No air resist
class Falling:
    def __init__(self, increment, mass, height_ini, velocity_ini):
        self.top = height_ini
        self.height = height_ini
        self.increment = increment
        self.G_acel = 9.81
        self.mass = mass
        self.velocity = velocity_ini
        self.heights = []
        self.times = []


    def speed_calc(self):
        for t in range(21):
            self.time = t*0.1
            self.times.append(self.time)
            self.height_change = self.velocity*self.increment
#       Define new variables:
            self.force = self.mass * self.G_acel
            self.T_acel = self.force/self.mass
            self.velocity = self.G_acel * t
            self.height = self.top - self.height_change
            self.heights.append(self.height)
            print("height: ", self.height, "accelaration: ", self.T_acel, "velocity: ", self.velocity, "time: ", self.time)





test = Falling(0.1, 15, 10, 5)
test.speed_calc()
print(test.heights, test.times)
plt.plot(test.heights, test.times)
plt.show()
