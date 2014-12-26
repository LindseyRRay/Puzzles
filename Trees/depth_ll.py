#Question: Given a bin search tree, create a linked list for all nodes at each depth
from tree import Node, tree1, tree2, tree3
import pdb 

class Node_ll:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def create_ll(root):
	if root == None:
		return 
	else:
		depth = 0
		final_ll = list()
		to_search = [(root,0)]
		while to_search:
			current, depth = to_search.pop(0)	
			print("depth is %s"%depth)
			if len(final_ll) <= depth:
				final_ll.append(Node_ll(current.value))
			else:
				head = final_ll[depth]
				while head.next != None:
					head = head.next
				head.next= Node_ll(current.value)
			if current.left != None:
				to_search.append((current.left, depth+1))
			if current.right != None:
				to_search.append((current.right, depth+1))
		
	return final_ll



if __name__ =='__main__':

	head1 = create_ll(tree1)
