class Node: 

	def __init__(self, val):
		self.val = val
		self.nextval = None

class SLinkedList:
	def __init__(self):
		self.headval = None

	def printList(self):
		printVal = self.headval
		while printVal is not None:
			value = printVal.val
			print(value)
			printVal = printVal.nextval


example = SLinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

example.headval = n1
n1.nextval = n2
n2.nextval = n3
n3.nextval = n4
n4.nextval = n5

example.printList()

