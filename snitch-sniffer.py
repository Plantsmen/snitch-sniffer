class Main():

	def __init__(self):
		print(self.answer())

	def answer(self):
		sum = 0
		for i in range(1000):
			if i % 3 == 0 or i % 5 == 0:
				sum += i
		return sum


Main()
