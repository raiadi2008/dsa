class Node:
	def __init__(self, value, next_node = None):
		self.value = value
		self.next_node = next_node

	def get_next_node(self):
		return self.next_node

	def get_value(self):
		return self.value

	def set_value(self, value):
		self.value = value
		
	def set_next_node(self, next_node):
		self.next_node = next_node

class  LinkedList:
	def __init__(self, value = None):
		self.head_node, self.tail_node = value, value

	def insert_beginning(self, value = None):
		if self.head_node == None:
			self.head_node = self.tail_node = Node(value,self.head_node)
		else :
			self.head_node = Node(value,self.head_node)
		
	def insert_end(self, value = None):
		if self.head_node == None:
			self.head_node = self.tail_node = Node(value,self.head_node)
		else :
			self.tail_node.set_next_node(Node(value))
			self.tail_node = self.tail_node.get_next_node()

	def traverse_list(self):
		cur_node = self.head_node
		while cur_node:
			print(str(cur_node.get_value()))
			cur_node = cur_node.get_next_node()
		

	def insert_after(self,key, value):
		cur_node = self.head_node
		while cur_node:
			if cur_node.get_value() == key:
				cur_node.set_next_node(Node(value,cur_node.get_next_node()))
				break
			else :
				cur_node = cur_node.get_next_node()

	def insert_before(self, key, value):
		if self.head_node:
			if self.head_node.get_value() == key:
				self.head_node = Node(value, self.head_node)
			else:
				cur_node = self.head_node
				while cur_node.get_next_node():
					if cur_node.get_next_node().get_value() == key:
						cur_node.set_next_node(Node(value,cur_node.get_next_node()))
						break
					else :
						cur_node = cur_node.get_next_node()
	
	def delete_node(self, key):
		if self.head_node:
			if self.head_node.get_value() == key:
				self.head_node = self.head_node.get_next_node()
			else:
				cur_node = self.head_node
				while cur_node.get_next_node():
					if cur_node.get_next_node().get_value() == key:
						cur_node.set_next_node(cur_node.get_next_node().get_next_node())
						break
					else:
						cur_node = cur_node.get_next_node()

	def search_value(self, target_value):
		cur_node = self.head_node
		while cur_node:
			if cur_node.get_value() == target_value:
				return True
			else :
				cur_node = cur_node.get_next_node()
		return False


if __name__ == "__main__" :
	ll = LinkedList()
	print("Printing List : ")
	ll.traverse_list()
	ll.insert_beginning(5)
	print("Printing List : ")
	ll.traverse_list()
	ll.insert_beginning(2345234)
	print("Printing List : ")
	ll.traverse_list()
	ll2 = LinkedList()
	ll2.insert_end(44)
	print("Printing List : ")
	ll2.traverse_list()
	ll2.insert_end(2341234)
	print("Printing List : ")
	ll2.traverse_list()
