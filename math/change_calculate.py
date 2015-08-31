class Payout:
	def __init__(self, total):
		self.total = 100*total	
		currencies = [['dollar', 100], ['quater', 25], ['dime', 10], ['nickel', 5], ['penny', 1]]
		for i in currencies:
			self.up(i[0], i[1])
		
	def up(self, currency, amount):
		m = 0
		while m*amount <= self.total:
			m += 1
		m -= 1
		self.total -= m*amount
		print(str(m) + '*' + currency + 's')
	
Payout(17.67)
