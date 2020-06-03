class node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class linkedList:
	def __init__(self):
		self.head = node()

	def append(self,data):
		new_node = node(data)
		cur = self.head

		while cur.next != None:
			cur = cur.next

		cur.next = new_node

	def length(self):
		cur = self.head
		total = 0
		while cur.next != None:
			total += 1
			cur = cur.next
		return total

	def get(self,index):
		if index >= self.length():
			print('ERROR: "Get" Index out of range')
			return None
		cur_idx = 0
		cur_node = self.head
		while True:
			cur_node = cur_node.next
			if cur_idx == index: return cur_node.data
			cur_idx +=1

	def deleteIndex(self, index):
		if index >= self.length():
			print('ERROR: "Delete" Index out of range')
			return
		cur_idx = 0
		cur_node = self.head
		while True:
			last_node = cur_node
			cur_node = cur_node.next
			if cur_idx == index:
				last_node.next = cur_node.next
				return
			cur_idx += 1

	def deleteNode(self, node):
		cur_node = self.head

		if cur_node == None:
			return
		#if head node itself holds the key to be deleted
		if cur_node != None:
			if cur_node.data == node:
				self.head = cur_node.next
				cur_node = None
				return
		# search for node to be deleted, keep track of last node
		while cur_node != None:
			if cur_node.data == node:
				break
			last_node = cur_node
			cur_node = cur_node.next

		last_node.next = cur_node.next
		cur_node = None
		

	def printList(self):
		cur_node = self.head
		elems = []

		while cur_node.next != None:
			cur_node = cur_node.next
			elems.append(cur_node.data)

		print(elems)


mylist = linkedList()
mylist.printList()

mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)
mylist.append(6)

mylist.printList()

print('Element at 2nd index is {}'.format(mylist.get(6)))

mylist.deleteIndex(1)
mylist.printList()

mylist.deleteNode(4)
mylist.printList()



'''
# Inserts the node 'node' at index 'index'. Indices begin at 0.
	# If the 'index' is greater than or equal to the length of the linked 
	# list the 'node' will be appended.
	def insert_node(self,index,node):
		if index<0:
			print("ERROR: 'Erase' Index cannot be negative!")
			return
		if index>=self.length(): # append the node
			cur_node=self.head
			while cur_node.next!=None:
				cur_node=cur_node.next
			cur_node.next=node
			return
		cur_node=self.head
		prior_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index: 
				prior_node.next=node
				return
			prior_node=cur_node
			cur_idx+=1

	# Sets the data at index 'index' equal to 'data'.
	# Indices begin at 0. If the 'index' is greater than or equal 
	# to the length of the linked list a warning will be printed 
	# to the user.
	def set(self,index,data):
		if index>=self.length() or index<0:
			print("ERROR: 'Set' Index out of range!")
			return
		cur_node=self.head
		cur_idx=0
		while True:
			cur_node=cur_node.next
			if cur_idx==index: 
				cur_node.data=data
				return
			cur_idx+=1
'''