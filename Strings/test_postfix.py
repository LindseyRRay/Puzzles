import unittest 
from postfix import is_number, postfix

class TestPostfix(unittest.TestCase):


	def test_is_number(self):
		self.assertEqual(is_number('1')[0], True)
		self.assertEqual(is_number('a')[0], False)
		self.assertEqual(is_number('12')[0], True)
		self.assertEqual(is_number('!')[0], False)

	def test_postix(self):
		test_cases = ["2+7*5", "3*3/(7+1)", "5+(6-2)*9+3^(7-1)"]
		solutions = ["275*+", "33*71+/", "562-9*+371-^+"]
		for index, case in enumerate(test_cases):
			print(postfix(case))
			self.assertEqual(postfix(case), solutions[index])


if __name__ == '__main__':
	unittest.main()
