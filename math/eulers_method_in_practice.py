from math import *
import matplotlib.pyplot as plt 
class Approximate:
    def __init__(self, Dt, x_init, y_init, t_init, t_final):
        self.Dt = Dt
        self.x = x_init
        self.y = y_init
        self.t = t_init
        self.limit = t_final
        self.initial = self.t
        self.initial_x = self.x
        self.vs = []
        self.times = [] 
        self.positions = []
        self.xs = []
        self.ys = []

    def run(self):
        constant = float(input("constant of proportionality> "))
        velocity = float(input("initial velocity> "))
        self.mass = float(input("self.mass> "))
        initial_angle = eval(input("initial angle> "))
#More desirable configuration are asked

        Fg = -(9.81*self.mass)
#Define the force of gravity and make it negative

        Vx = cos(initial_angle)*velocity
        Vy = sin(initial_angle)*velocity
#Define velocity with respect to x and y

        while self.t < self.limit:
            self.xs.append(self.x)
            self.ys.append(self.y)
            self.vs.append(velocity)
            self.times.append(self.t)
#Plotting stuff

            Fa = constant*(velocity**2)
#Force of Air resistance

            Fx = -(Fa*Vx/velocity)
            Fy = -(Fa*Vy/velocity)+Fg

#Define force in x and y
            Ax = Fx/self.mass
            Ay = Fy/self.mass

            Vx = Vx + self.Dt*Ax
            Vy = Vy + self.Dt*Ay

            self.t = self.t + self.Dt
            self.x = self.x + self.Dt*Vx
            self.y = self.y + self.Dt*Vy
            velocity = sqrt(Vx**2 + Vy**2)

#Basic syntax: Approximate(steps, x init, y_init, t_init, t_final)
running = Approximate(.01, 0, 0, 0, 100)
running.run()

plt.subplot(3,1,1)
plt.plot(running.times,running.ys)
plt.ylabel('Y distance')

plt.subplot(3,1,2)
plt.plot(running.xs, running.ys)
plt.ylabel('Y distance')

plt.subplot(3,1,3)
plt.plot(running.times,running.vs)
plt.xlabel('Time')
plt.ylabel('Velocity')

plt.show()
