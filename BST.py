class Node(object):
	
	def __init__(self, value, parent=None):
		self.value = value
		self.right = None
		self.left = None
		self.parent = parent

	def getRightChild(self):
		return self.right

	def getLeftChild(self):
		return self.left

	def insert(self, value):
		currentNodeVal = self.value
		if value < currentNodeVal:
			if self.left == None:
				self.left = Node(value, self)
			else: 
				self.left.insert(value)
		else:
			if self.right == None:
				self.right = Node(value, self)
			else:
				self.right.insert(value)

	def numberOfChildren(self):
		children = 0
		if self.left is not None:
			children += 1
		if self.right is not None:
			children += 1
		return children

	def isRightChild(self):
		parent = self.parent
		if parent.right.value == self.value:
			return True
		else:
			return False

	def getSingleChild(self):
		if self.right is not None:
			return self.right
		else:
			return self.left

	def delete(self, value):
		toRemove = self.find(value)
		children = toRemove.numberOfChildren()
		if children == 0:
			if toRemove.isRightChild() is True:
				toRemove.parent.right = None
			else:
				toRemove.parent.left = None
		elif children == 1:
			child = toRemove.getSingleChild()
			child.parent = toRemove.parent
			if toRemove.isRightChild() is True:
				toRemove.parent.right = child
			else:
				toRemove.parent.left = child
		elif children == 2:
			minToRight = toRemove.right.minimum()
			minToRightValue = minToRight.value
			self.delete(minToRightValue)
			toRemove.value = minToRightValue

	def find(self, value):
		if value == self.value:
			return self
		elif value < self.value:
			if self.left is None:
				return None
			else:
				return self.left.find(value)
		else:
			if self.right is None:
				return None
			else:
				return self.right.find(value)

	def minimum(self):
		current = self
		while current.left is not None:
			current = current.left
		return current

	def maximum(self):
		current = self
		while current.right is not None:
			current = current.right
		return current

	def inorder_traversal(self):
		nodes_list = []
		if self.left is not None:
			nodes_list.extend(self.left.inorder_traversal())
		nodes_list.append(self.value)
		if self.right is not None:
			nodes_list.extend(self.right.inorder_traversal())
		return nodes_list



root = Node(5)

root.insert(2)
root.insert(7)
root.insert(6)
root.insert(8)
root.insert(4)
root.insert(3)
print(root.right.value)
print(root.right.right.value)
print(root.right.left.value)
print(root.left.value)
print(root.left.right.value)
print(root.left.right.left.value)
print('\n --delete-- \n')
root.delete(8)
print(root.right.value) 
# print(root.right.right.value)
print(root.right.left.value)
print(root.left.value)
print(root.left.right.value)
print(root.left.right.left.value)
print(root.inorder_traversal())

