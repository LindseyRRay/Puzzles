#test reverse ll
import unittest
import linked_list
import reverse_ll

class TestReverse(unittest.TestCase):
	def setUp(self):
		self.ll1 = linked_list.create_ll(8)
		self.ll2 = linked_list.create_ll(8)
		

	def test_iterative(self):
		print("Ll 1 not reversed")
		linked_list.print_ll(self.ll1)
		new_head = reverse_ll.iterative_reverse(self.ll1)
		print("Ll 1 reversed")
		linked_list.print_ll(new_head)

	def test_recursive(self):
		print("Ll 2 not reversed")
		linked_list.print_ll(self.ll2)
		new_head = reverse_ll.recursive_reverse(self.ll2)
		print("Ll 2 reversed")
		linked_list.print_ll(new_headN)


if __name__ == '__main__':
	unittest.main()
