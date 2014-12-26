#remove duplicates from an unsorted linked list
#method 1:
#use a hash table to store already seen values
#method 2:
#no temporary buffer is allowed, so use two pointers, 
#one to go through the list and one to check all following nodes
import random, pdb 

class Node:
	def __init__(self, value, next_node=None):
		self.value = value
		self.next = next_node

	def set_next(self, next_node):
		self.next = next_node

def create_ll(num_nodes):

	last = Node(random.randint(0,10000))
	while num_nodes > 1:
		current = Node(random.randint(0,10000), last)
		last = current
		num_nodes -=1
	return last

def duplicate_node(ll_head, num_nodes):
	dup = random.randint(1,num_nodes)
	point=1
	pointer = ll_head
	while point < dup:
		pointer = pointer.next
		point +=1 
	value = pointer.value 
	while pointer.next!=None:
		pointer = pointer.next
	pointer.next = Node(value)
	return value


def hash_dups(ll_head):
	seen_values = list()
	dups = list()
	previous = ll_head
	current = ll_head.next
	while current != None:
		if current.value in seen_values:
			dups.append(current.value)
			previous.next = current.next
		else:
			seen_values.append(current.value)
		current= current.next
		previous=current
	return dups

def pointer_dups(ll_head):
	current=ll_head
	runner=ll_head.next
	while current != None:
		while runner!= None:
			if runner.value == current.value:
				return runner.value
			runner= runner.next
		current= current.next
		runner = current.next 
	return None 


def main_hash_dups(num_nodes):
	ll1 = create_ll(num_nodes)
	dup = duplicate_node(ll1, num_nodes)
	print(dup)
	ll_dup = hash_dups(ll1)
	print(ll_dup)
	assert dup == ll_dup[0]

def main_pointer_dups(num_nodes):
	ll1 = create_ll(num_nodes)
	dup = duplicate_node(ll1, num_nodes)
	print(dup)
	ll_dup = pointer_dups(ll1)
	print(ll_dup)
	assert dup == ll_dup


def main(num_nodes):
	main_hash_dups(num_nodes)
	main_pointer_dups(num_nodes)

main(5)


