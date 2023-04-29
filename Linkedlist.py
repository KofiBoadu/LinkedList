
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

	def remove(self,value):
		if self.head== None:
			return None 
		if self.head.value == value:
			self.head=self.head.next
		else:
			current= self.head
			prev= None
			while current.value != value and current.next != None:
				prev= current
				current= current.next
			prev.next= current.next

	def reverse(self):
		if self.head== None:
			return None 
		elif self.size() <= 1:
			return self.head.value
		else:
			current= self.head
			previous= None 
			while current:
				forward= current.next 
				current.next= previous 
				previous= current
				current= forward 
		self.head= previous
		return self.display()





	def display(self):
		current = self.head
		while current != None:
			print(f"{current.value}---->", end="")
			current= current.next







