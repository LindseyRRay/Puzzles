#find route between two nodes on a graph
#use breadth first search or depth first search to find target node 
#DFS uses recursion to iterate completely down each subtree 
#BFS searches each level completely before iterating to next level
from tree import Node, tree1, tree2, tree3

def DFS(root, target):
	if root == None:
		return False
	elif root.value == target:
		print("Found value")
		return True
	else:
		print("Searching %d"%root.value)
		foundl = DFS(root.left, target)
		foundr = DFS(root.right, target)
		return foundr or foundl

def DFS_main():
	print(DFS(tree1, 8))
	print(DFS(tree1, 6))

	print(DFS(tree3, 3))
	print(DFS(tree3, 8))

def BFS(root, target):
	if root == None:
		return False
	to_search = list()
	to_search.append(root)
	while to_search:
		current = to_search.pop(0)
		if current.value == target:
			return True
		else:
			if current.left != None:
				to_search.append(current.left)
			if current.left != None:
				to_search.append(current.right)
	return False


def BFS_main():
	print(BFS(tree1, 8))
	print(BFS(tree1, 6))
	print(BFS(tree3, 3))
	print(BFS(tree3, 8))

if __name__ == '__main__':

	DFS_main()
	BFS_main()

