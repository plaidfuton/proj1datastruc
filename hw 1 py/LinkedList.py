#Name: Ryan Nielson
#ID: 86219673
#Email: rnielson@unomaha.edu
class LinkedList():
	class Node:
		def __init__(self, data):
			## data of the node
			self.data = data

			## next pointer
			self.next = None

	def __init__(self):
		## initializing the head with None
		self.head = None
		self.n = 0

	###########################################################
	# Implement three functions below.
	# You are not allowed to change any function declaration, e.g., name, parameters, and return value.
	###########################################################
	def insertTail(self, value):
		if self.head is None:
			new_node = self.Node(value)
			self.head = new_node
			self.head.next = None
		else:
			new_node = self.Node(value)
			current = self.head
			while current.next:
				current = current.next
			current.next = new_node
			new_node.next = None
		self.n += 1

	def insert(self, idx, value):
		if self.head is None:
			new_node = self.Node(value)
			self.head = new_node
			self.head.next = None
		else:
			new_node = self.Node(value)
			current = self.head
			temp = 0
			while current is not None and temp < idx-1:
				current = current.next
				temp += 1
			new_node.next = current.next
			current.next = new_node
		self.n += 1

	def get(self, idx):
		current = self.head
		temp = 0
		while current is not None and temp < idx-1:
			current = current.next
			temp += 1
		return current.next.data
	###########################################################
	# Given implemented code below.
	###########################################################
	def display(self):
		## variable for iteration
		temp_node = self.head

		## iterating until we reach the end of the linked list
		while temp_node != None:
			## printing the node data
			print(temp_node.data, end=' ')

			## moving to the next node
			temp_node = temp_node.next

		print("\n")

	def insertHead(self, value):
		if(self.head == None):
			self.head = self.Node(value)
			self.head.next = None
		else:
			new_node = self.Node(value)
			new_node.next = self.head
			self.head = new_node

		self.n = self.n + 1

	def getSize(self):
		return self.n

	def getName(self):
		return "LinkedList"