#Q Implement a Priority Queue with A Max Heap
from heap import Heap

class PriorityQ:
	def __init__(self, array, q_type="MAX"):
		self.q = Heap(array, q_type)

	def get_root(self):
		#return itsm with largest/smalles key
		return self.q.heap[0]

	def change_key(self, element, new_value):
		#increase value of element x's key to new value
		#exchanges key with parent is key violates heap property
		if not self.q.compare_to(new_value, self.q.heap[element]):
			raise Exception("New Key Smaller than Current Key")
		else:
			self.q.heap[element] = new_value
			parent_index = self.q.parent(element)
			while element >= 0 and not self.q.compare_to(self.q.heap[parent_index], self.q.heap[element]):
				temp = self.q.heap[parent_index]
				self.q.heap[parent_index] = self.q.heap[element]
				self.q.heap[element] = temp
				parent_index = self.q.parent(parent_index)
			self.q.re_heapify()


	def extract_root(self):
		#gets and removes element with largest key
		if self.q.heapsize < 1:
			raise Exception("Heap Underflow")
		else:
			to_return = self.q[0]
			self.q.heap[0] = self.q.heap[self.q.heapsize]
			self.q.heapsize -= 1
			self.q.heapify(0, self.q.heap)
			self.q.re_heapify()
			return to_return


	def insert_item(self, item):
		#Add item to the end with key -inf then call the increase key fnc with real val
		if self.q.htype == "MAX":
			add_val = -2000
		else:
			add_val = 2000
		self.q.heapsize += 1
		self.q.heap.append(add_val)
		self.change_key(self.q.heapsize, item)


	
