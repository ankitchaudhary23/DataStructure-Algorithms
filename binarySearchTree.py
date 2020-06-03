class node:
	def __init__(self, value = None):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None		# pointer to parent node in tree

class binarySearchTree:
	def __init__(self):
		self.root = None

	def insert(self, value):
		if self.root == None:
			self.root = node(value)

		else:
			self._insert(value, self.root)

	def _insert(self, value, cur_node):
		if value < cur_node.value:

			if cur_node.left == None:
				cur_node.left = node(value)
				cur_node.left.parent = cur_node		#set parent

			else:
				self._insert(value, cur_node.left)

		elif value > cur_node.value:

			if cur_node.right == None:
				cur_node.right = node(value)
				cur_node.right.parent = cur_node	# set parent

			else:
				self._insert(value, cur_node.right)
		
		else:
			print("Value already in tree")

	def printTree(self):
		if self.root is not None:
			self._printTree(self.root)

	def _printTree(self, cur_node):
		if cur_node != None:
			# Inorder Traversal
			self._printTree(cur_node.left)
			print(cur_node.value)
			self._printTree(cur_node.right)

	def height(self):
		if self.root != None:
			return self._height(self.root,0)
		else:
			return 0

	def _height(self, cur_node, cur_height):
		if cur_node == None:
			return cur_height
		left_height = self._height(cur_node.left, cur_height+1)
		right_height = self._height(cur_node.right, cur_height+1)
		return max(left_height, right_height)

	# return the node with specified input value
	def find(self, value):
		if self.root != None:
			return self._find(value, self.root)
		else:
			return None

	def _find(self, value, cur_node):
		if value == cur_node.value:
			return cur_node
		elif value < cur_node.value and cur_node.left != None:
			return self._find(value, cur_node.left)
		elif value > cur_node.value and cur_node.right != None:
			return self._find(value, cur_node.right)
		else:
			return None

	def delete_value(self,value):
		return self.delete_node(self.find(value))

	def delete_node(self, node):
		if node == None or self.find(node.value) == None:
			print('Node to be deleted not found in the tree!')
			return None

		def min_value_node(n):
			current = n
			while current.left != None:
				current = current.left
			return current

		def num_children(n):
			num_children = 0
			if n.left != None:
				num_children += 1
			if n.right != None:
				num_children += 1
			return num_children

		node_parent = node.parent
		node_children = num_children(node)

		# Case 1 (node has no children)
		if node_children == 0:
			if node_parent != None:
				# remove reference to the node from the parent
				if node_parent.left == node:
					node_parent.left = None
				else:
					node_parent.right = None
			else:
				self.root = None

		# Case 2 (node has 1 child)
		if node_children == 1:
			# get single child node
			if node.left != None:
				child = node.left
			else:
				child = node.right

			if node_parent != None:
				# replace the node to be deleted with its child
				if node_parent.left==node:
					node_parent.left = child
				else:
					node_parent.right = child
			else:
				self.root = child

			# correct the parent pointer in node
			child.parent = node_parent

		# Case 3 (node has 2 children)
		if node_children == 2:
			# get inorder successor of the deleted node
			successor = min_value_node(node.right)

			# copy inorder successor now to the node formerly
			# holding the value we wished to delete
			node.value = successor.value

			# delete inorder successor now
			self.delete_node(successor)


	# return true if the value exists in the tree
	def search(self, value):
		if self.root != None:
			return self._search(value, self.root)
		else:
			return False

	def _search(self, value, cur_node):
		if value == cur_node.value:
			return True
		elif value < cur_node.value and cur_node.left != None:
			return self._search(value, cur_node.left)
		elif value > cur_node.value and cur_node.right != None:
			return self._search(value, cur_node.right)
		else:
			return False



def fillTree(tree, nums = 20, max_int = 100):
	from random import randint
	for _ in range(nums):
		cur_elem = randint(0, max_int)
		tree.insert(cur_elem)
	return tree

tree = binarySearchTree()
#tree = fillTree(tree)
tree.insert(5)
tree.insert(1)
tree.insert(3)
tree.insert(2)
tree.insert(7)
tree.insert(10)
tree.insert(0)
tree.insert(20)

tree.printTree()

print('tree height: '+str(tree.height()))

print (tree.search(10))
print (tree.search(30))

tree.delete_value(5)
tree.printTree()





