class Node:
	def __init__(self,value):
		self.value= value
		self.next= None

class ListNode:
	def __init__(self):
		self.head= None


	def add_first(self,value):
		new_node= Node(value)
		new_node.next= self.head
		self.head= new_node


	def add_last(self,value):
		new_node= Node(value)
		current= self.head
		while current.next != None:
			current= current.next
		current.next= new_node


	def size(self):
		current= self.head
		count= 0
		while current.next != None:
			count+=1
			current= current.next
		count+=1
		return count


	def display(self):
		current = self.head
		while current != None:
			print(f"{current.value}---->", end="")
			current= current.next












ll= ListNode()
ll.add_first(10)
ll.add_first(100)
ll.add_first(15)
print(ll.display())
print(ll.size())


