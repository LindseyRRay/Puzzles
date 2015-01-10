#test BST
import unittest
from random import randint
from BSTree import Node, BSTree



class test_BST(unittest.TestCase):

	def setUp(self):
		root = Node(15, Node(6, Node(3, Node(2), Node(4)), \
			Node(7, None, Node(13, Node(9)))), \
		Node(18, Node(17), Node(20)))
		self.tree1 = BSTree(root)

	def test_search(self):
		self.assertEqual(self.tree1.search(root, 19, True), False)
		self.assertEqual(self.tree1.search(root, 7, False), True)


