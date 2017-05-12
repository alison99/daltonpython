class Stack: #at bottom

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items==[]

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

class StackFIFO: #at top

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.itmes == []

	def push(self, item):
		self.items.insert(0,item)

	def pop(self):
		return self.items.pop(0)

	def peek(self):
		return self.items[0]

	def size(self):
		return len(self.items)

s = Stack()
s.push("hi")
s.push("too much")
s.push("coding")
s.push("every single day")
print s.peek()


s.pop()
print s.peek()
print s.isEmpty()
print s.size()