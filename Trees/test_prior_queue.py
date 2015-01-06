#Tests for max_queue

import unittest
from max_queue import PriorityQ
from random import randint

class TestPriorityQueue(unittest.TestCase):

	def setUp(self):
		self.arr = [randint(-100, 100) for i in range(10)]
		self.maxq = PriorityQ(self.arr, "MAX")
		self.minq = PriorityQ(self.arr, "MIN")

	def test_root(self):
		self.assertEqual(self.minq.get_root(), min(self.arr))
		self.assertEqual(self.maxq.get_root(), max(self.arr))

	def test_change_key(self):
		print(self.minq.q.heap)
		self.minq.change_key(3, -500)
		print(self.minq.q.heap)

		print(self.maxq.q.heap)
		self.maxq.change_key(3, 500)
		print(self.maxq.q.heap)

	def test_insert(self):
		print(self.minq.q.heap)
		self.minq.insert_item(-1000)
		print(self.minq.q.heap)
		self.assertEqual(self.minq.get_root(), -1000)

		print(self.maxq.q.heap)
		self.maxq.insert_item(1000)
		print(self.maxq.q.heap)
		self.assertEqual(self.maxq.get_root(), 1000)

if __name__ == '__main__':
	unittest.main()





