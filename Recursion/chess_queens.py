#Q: print all ways of arranging eight queens on a chess board so that
# none of them share the same row, column or diagonal.
#Something weird is going on here need to troubleshoot
import numpy 

class Node:
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.children = list()

def check_space(row, col, board):
	if row >= board.shape[0] or row < 0 or col >= board.shape[1] or col < 0 \
	or sum(board[row,:])>0 or sum(board[:,col])>0:
		return False
	return True

def check_diag(row, col, board):
	if row >= board.shape[0] or row < 0 or col >= board.shape[1] or col < 0:
		return True
	
	elif board[row][col] != 0:
			return False
	else:
		return check_diag(row+1, col+1, board) or check_diag(row-1, col-1, board)

def print_tree(root, currents= list()):
	if not root.children:
		return
	else:
		currents.append((root.row, root.col))

		for tup in currents:
			print("row is %s and col is %s"%(root.row, root.col))	
		for child in root.children:
			print_tree(child)


def arrange_queens(row, col, board, queens, parent):
	if queens <= 0:
		return 
	else:
		parent_node = parent 
		current = Node(row, col)
		if check_space(row, col, board) and check_diag(row, col, board):
			print("checking row %s col %s"%(row, col))
			#place queen
			board[row][col] = 1
			#append space to the current's children node		
			parent.children.append(current)
			print(parent.children)
			parent_node = current
			#call arrange queen on surrounding cells
		arrange_queens(row - 1, col, numpy.copy(board), queens - 1, parent_node)
		arrange_queens(row, col - 1, numpy.copy(board), queens - 1, parent_node)
		arrange_queens(row + 1, col, numpy.copy(board), queens - 1, parent_node)
		arrange_queens(row, col + 1, numpy.copy(board), queens - 1, parent_node)
		arrange_queens(row - 1, col + 1, numpy.copy(board), queens - 1, parent_node)
		arrange_queens(row - 1, col - 1, numpy.copy(board), queens - 1, parent_node)
		arrange_queens(row + 1, col + 1, numpy.copy(board), queens - 1, parent_node)
		arrange_queens(row + 1, col - 1, numpy.copy(board), queens - 1, parent_node)

if __name__ == '__main__':

	board = numpy.zeros((8,8))
	root = Node(None, None)
	arrange_queens(2, 3, board, 8, root)
	print_tree(root)






