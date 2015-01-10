#Q: find the nth highest node in a BST
#Example: highest node is rightmost node
#2nd highest node is parent of rightmost node
#this is equivalent to finding the max if it is the highest node
from tree import tree1
def find_nth(root, nth, visited = list()):
	if root == None:
		return 
	else:
		find_nth(root.right, nth, visited)
		print("root val is %s " %(root.value))
		visited.append(root.value)
		if len(visited) == nth:
			print("%s th most node is %s"%(nth, root.value))
		find_nth(root.left, nth, visited)

def test_nth():
	find_nth(tree1, 2)

test_nth()
