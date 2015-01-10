#implementing a tree in python

class Node(object):

	def __init__(self, key, left=None, right=None, parent=None):
		self.key = key
		self.left = left
		self.right = right
		self.parent = parent 
	


class BSTree():

	def __init__(self, root):
		self.root = root

	def inorder(self, root):
		if root == None:
			return 
		else:
			if root.left:
				self.inorder(root.left)
			if root.parent != None:
				print("parent is %s"%root.parent.key)
			print(root.key)
			if root.right:
				self.inorder(root.right)

	def set_parents(self, root):
		if root == None:
			return 
		if root.left:
			root.left.parent = root
		if root.right:
			root.right.parent = root
		self.set_parents(root.left)
		self.set_parents(root.right) 

	def _search(self, root, key):
		if root == None or root.key == key:
			return root
		else:
			if key < root.key:
				return self._search(root.left, key)
			else:
				return self._search(root.right, key)

	def _iter_search(self, root, key):
		while root != None and root.key != key:
			if key < root.key:
				root = root.left
			else:
				root = root.right
		return root

	def search(self, root, key, itersearch=False):
		search_func = (self._iter_search if itersearch else self._search)
		output = search_func(root, key)
		if output:
			return (output.key == key, output)
		return False, output

	def min(self, root):
		while root.left != None:
			root=root.left
		return root

	def max(self, root):
		while root.right != None:
			root = root.right
		return root


	def successor(self, root):
		#successor is the node with smallest key greater than x
		#if a node has a right child, then successor is left most node
		#of the right subtree
		#otherwise it is the node whose left child is ancestor of node
		#go up tree until we find a node who is a left child
		if root.right != None:
			return self.min(root.right)
		else:
			y=root.parent
			while y != None and root != y.left:
				root = y
				y = root.parent
			return y

	def predecessor(self, root):
		#predecessr is the node with the greatest key < x
		#if a node has a left child, then it is max of left subtree
		#otherwise we want ancestor that is a right child 
		if root.left != None:
			return self.max(root.left)
		else:
			y = root.parent
			while y != None and root != y.right:
				root = y
				y = root.parent
			return y 

	def insert(self, root, key):
		parent = root.parent
		while root != None:
			if root.key > key:
				parent = root
				root = root.left
			elif root.key < key:
				parent = root
				root = root.right
			else:
				raise Exception("Duplicate Key")
		new_Node = Node(key, None, None, parent)
		if parent == None:
			#tree was empty
			return new_Node
		if key < parent.key:
			parent.left = new_Node
		else:
			parent.right = new_Node
		return new_Node

	def delete(self, root, key):
		#if to_delete has no children, we replace parent links with None
		#if 1 child then replace to_delete with the child 
		#if to_delete has 2 children, then we need to find sucessor node in 
		#right sbtree, replace it with to_delete and then attach links for left child
		


if __name__ == '__main__':
	root = Node(15, Node(6, Node(3, Node(2), Node(4)), \
	Node(7, None, Node(13, Node(9)))), \
	Node(18, Node(17), Node(20)))
	tree1 = BSTree(root)
	
	print(tree1.search(root, 19, True))
	assert tree1.min(root).key == 2

	tree1.set_parents(root)
	#tree1.inorder(root)

	assert tree1.successor(tree1.search(root, 15)[1]).key == 17
	assert tree1.successor(tree1.search(root, 13)[1]).key == 15

	new_node = tree1.insert(root, 1)
	tree1.inorder(root)


