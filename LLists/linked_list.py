import random


class Node:
	def __init__(self, value, next_node=None):
		self.value = value
		self.next = next_node

	def set_next(self, next_node):
		self.next = next_node

def create_ll(num_nodes):

	last = Node(random.randint(0,9))
	while num_nodes > 1:
		current = Node(random.randint(0,9), last)
		last = current
		num_nodes -=1
	return last

def print_ll(head):
	ind = head
	while ind != None:
		print("| %s |->"%ind.value)
		ind = ind.next

