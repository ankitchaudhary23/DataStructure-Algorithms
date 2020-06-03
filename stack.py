# Stack is LIFO (last-in-first-out).
# Func's: empty(), size(), push(n), pop() [deletes the topmost element]
# 				and peek [get topmost element of the stack]


class stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.size() == 0

	def size(self):
		return len(self.items)

	def push(self, value):
		if value not in self.items:
			self.items.append(value)
			return True
		else:
			return False

	def pop(self):
		if len(self.items) <= 0:
			return 'No Elements in the stack'
		else:
			return self.items.pop()

	def peek(self):
		if self.isEmpty():
			raise Exception('Stack empty!')
		# view element at top of the stack
		return self.items[-1]

	def printStack(self):
		return self.items



myStack = stack()

print(myStack.isEmpty())

myStack.push(3)
myStack.push(2)
myStack.push(4)
myStack.push(5)

print(myStack.isEmpty())
print(myStack.printStack())
print(myStack.peek())
print(myStack.pop())
