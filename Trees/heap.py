#Q:implement a priority queue using a max heap 
import pdb 

class Heap:
	def __init__(self, array, htype="MAX"):
		self.htype = htype
		self.heapsize = len(array)-1
		self.array = array
		self.heap = self.build_heap()

	def compare_to(self, a, b):
		if self.htype == "MAX":
			return (a > b)
		return (a < b)
	
	def define_array(self, array):
		if array is None:
			return (self.array, self.heapsize)
		return (array, len(array) - 1)

	def parent(self, index):
		if index > 0:
			return int((index-1)/2)
		return None

	def left_child(self, index):
		if index >= int(self.heapsize/2):
			return None
		return 2*index + 1

	def right_child(self, index):
		if index >= int(self.heapsize/2):
			return None
		return 2*index + 2

	@staticmethod
	def heapsize(self):
		return self.heapsize

	def heapify(self, index, array):
		if index > self.heapsize:
			return 
		else:
			l = self.left_child(index)
			r = self.right_child(index)
			item = index
			if l and l < self.heapsize and self.compare_to(array[l], array[item]):
				item = l
			if r and r < self.heapsize and self.compare_to(array[r], array[item]):
				item = r
			if item != index:
				temp = array[index]
				array[index] = array[item]
				array[item] = temp

				self.heapify(item, array)

	def re_heapify(self):
		i = int(self.heapsize/2) + 1
		while i >= 0:
			self.heapify(i, self.heap)
			i -= 1

	def build_heap(self):
		arr_copy = self.array[:]
		i = int(self.heapsize/2)
		while i >= 0:
			self.heapify(i, arr_copy)
			i -= 1
		return arr_copy







