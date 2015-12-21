import random
from useful_stuff import *

class Perceptron:
	def __init__(self, n):
		self.weights = [0 for x in range(n)]
		self.learn = 0.01 
		for i in range(len(self.weights)):
			self.weights[i] = round(random.uniform(-1, 1), 4)
	
	def feedforward(self, inputs):
		total = 0.0
		for i in range(len(self.weights)):
			total += inputs[i] + self.weights[i]
		if is_positive(total) == False:
			return -1
		return 1
	
	def train(self, inputs, desired):
		self.guessed = self.feedforward(inputs)
		self.error = desired - self.guessed
		for i in range(len(self.weights)):
			self.weights[i] += self.error * inputs[i] * self.learn
	
class Trainer:
	def __init__(self, x, y, a):
		self.inputs = [x, y, 1]
		self.answer = a
				
def f(x):
	return 2*x + 3

ptron = Perceptron(3)
x = 5.0
y = 20.0
for x in range(20):
	for y in range(5):
		yline = f(x)
		answer = -1
		if y < yline:
			answer = 1

		t = Trainer(x, y, answer)
		while True:
			ptron.train(t.inputs, t.answer)
			if ptron.error == 0:
				break
		print(ptron.weights)

