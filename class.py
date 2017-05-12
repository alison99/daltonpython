#new variable type or class
class Point:
	#pass
	#pass = blank return
	def _init_(self, x=0, y=0):
		self.x=x
		self.y=y

	def distance_from_origin(self):
		#the pythagorean theorem
		return ((self.x**2) + (self.y **2)) ** 0.5

p = Point()
p.x = 5
p.y = 12
print(p.x)
print p.distance_from_origin()