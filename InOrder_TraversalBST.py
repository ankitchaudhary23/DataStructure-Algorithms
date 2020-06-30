class node:
	def __init__(self, data = None):
		self.data = data
		self.left = None
		self.right = None

	def insert(self, data):

		if self.data:
			if data<self.data:
				if self.left is None:
					self.left = node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = node(data)
				else:
					self.right.insert(data)

		else:
			self.data = data

	# Inorder Traversal
	# left -> root -> right
	def inorderTraversal(self, root):
		result = []
		if root:
			result = self.inorderTraversal(root.left)
			result.append(root.data)
			result = result + self.inorderTraversal(root.right)
		return result



root = node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print(root.inorderTraversal(root))
